# coding=utf-8
import json
import logging
from time import sleep

import requests
from requests.cookies import RequestsCookieJar

from pynYNAB.KeyGenerator import generateuuid
from pynYNAB.schema.Entity import ComplexEncoder
from pynYNAB.utils import rate_limited

LOG = logging.getLogger(__name__)


class NYnabConnectionError(Exception):
    pass


# noinspection PyPep8Naming
class nYnabConnection(object):
    url = 'https://app.youneedabudget.com/users/login'
    urlCatalog = 'https://app.youneedabudget.com/api/v1/catalog'

    def _init_session(self):
        self.session.cookies = RequestsCookieJar()

        self.session.headers['X-YNAB-Device-Id'] = self.id
        self.session.headers['User-Agent'] = 'python nYNAB API bot - rienafairefr rienafairefr@gmail.com'

        firstlogin = self.dorequest({"email": self.email, "password": self.password, "remember_me": True,
                                     "device_info": {"id": self.id}}, 'loginUser')
        if firstlogin is None:
            raise NYnabConnectionError('Couldnt connect with the provided email and password')
        self.sessionToken = firstlogin["session_token"]
        self.session.headers['X-Session-Token'] = self.sessionToken
        self.user_id = firstlogin['user']['id']

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.session = requests.Session()
        self.sessionToken = None
        self.id = str(generateuuid())
        self.lastrequest_elapsed = None
        self._init_session()

    @rate_limited(maxpersecond=5)
    def dorequest(self, request_dic, opname):
        """
        :param request_dic: a dictionary containing parameters for the request
        :param opname: An API operation name, available are: loginUser,getInitialUserData,logoutUser,createNewBudget,
        freshStartABudget,cloneBudget,deleteTombstonedBudgets,syncCatalogData,syncBudgetData,getInstitutionList,
        getInstitutionLoginFields,getInstitutionAccountList,registerAccountForDirectConnect,
        updateDirectConnectCredentials,poll,createFeedback,runSqlStatement
        :return: the dictionary of the result of the request
        """
        # Available operations :

        json_request_dict = json.dumps(request_dic, cls=ComplexEncoder)
        params = {u'operation_name': opname, 'request_data': json_request_dict}
        LOG.debug('%s  ... %s ' % (opname, params))
        r = self.session.post(self.urlCatalog, params, verify=False)
        self.lastrequest_elapsed = r.elapsed
        js = r.json()
        if r.status_code != 200:
            LOG.debug('non-200 HTTP code: %s ' % r.text)
        if js['error'] is None:
            return js
        else:
            error = js['error']
            if r.status_code == 500:
                raise NYnabConnectionError('Uunrecoverable server error, sorry YNAB')
            if 'id' not in error:
                LOG.error('API error, %s' % error['message'])
            if error['id'] == 'user_not_found':
                LOG.error('API error, User Not Found')
            elif error['id'] == 'id=user_password_invalid':
                LOG.error('API error, User-Password combination invalid')
            elif error['id'] == 'request_throttled':
                LOG.debug('API Rrequest throttled')
                retyrafter = r.headers['Retry-After']
                LOG.debug('Waiting for %s s' % retyrafter)
                sleep(float(retyrafter))
                return self.dorequest(request_dic, opname)
            else:
                LOG.debug('Unknown API error')
                LOG.debug('Request data:')
                LOG.debug(params)
                raise NYnabConnectionError(
                    'Unknown Error \"%s\" was returned from the API when sending request (%s)' % (error['id'], params))
