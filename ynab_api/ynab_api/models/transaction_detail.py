# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ynab_api.models.sub_transaction import SubTransaction  # noqa: F401,E501
from ynab_api.models.transaction_summary import TransactionSummary  # noqa: F401,E501


class TransactionDetail(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'date': 'date',
        'amount': 'float',
        'cleared': 'str',
        'approved': 'bool',
        'account_id': 'str',
        'subtransactions': 'list[SubTransaction]'
    }

    attribute_map = {
        'id': 'id',
        'date': 'date',
        'amount': 'amount',
        'cleared': 'cleared',
        'approved': 'approved',
        'account_id': 'account_id',
        'subtransactions': 'subtransactions'
    }

    def __init__(self, id=None, date=None, amount=None, cleared=None, approved=None, account_id=None, subtransactions=None):  # noqa: E501
        """TransactionDetail - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date = None
        self._amount = None
        self._cleared = None
        self._approved = None
        self._account_id = None
        self._subtransactions = None
        self.discriminator = None

        self.id = id
        self.date = date
        self.amount = amount
        self.cleared = cleared
        self.approved = approved
        self.account_id = account_id
        self.subtransactions = subtransactions

    @property
    def id(self):
        """Gets the id of this TransactionDetail.  # noqa: E501


        :return: The id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionDetail.


        :param id: The id of this TransactionDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def date(self):
        """Gets the date of this TransactionDetail.  # noqa: E501


        :return: The date of this TransactionDetail.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TransactionDetail.


        :param date: The date of this TransactionDetail.  # noqa: E501
        :type: date
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def amount(self):
        """Gets the amount of this TransactionDetail.  # noqa: E501

        The transaction amount in milliunits format  # noqa: E501

        :return: The amount of this TransactionDetail.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionDetail.

        The transaction amount in milliunits format  # noqa: E501

        :param amount: The amount of this TransactionDetail.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def cleared(self):
        """Gets the cleared of this TransactionDetail.  # noqa: E501

        The cleared status of the transaction  # noqa: E501

        :return: The cleared of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._cleared

    @cleared.setter
    def cleared(self, cleared):
        """Sets the cleared of this TransactionDetail.

        The cleared status of the transaction  # noqa: E501

        :param cleared: The cleared of this TransactionDetail.  # noqa: E501
        :type: str
        """
        if cleared is None:
            raise ValueError("Invalid value for `cleared`, must not be `None`")  # noqa: E501
        allowed_values = ["cleared", "uncleared", "reconciled"]  # noqa: E501
        if cleared not in allowed_values:
            raise ValueError(
                "Invalid value for `cleared` ({0}), must be one of {1}"  # noqa: E501
                .format(cleared, allowed_values)
            )

        self._cleared = cleared

    @property
    def approved(self):
        """Gets the approved of this TransactionDetail.  # noqa: E501

        Whether or not the transaction is approved  # noqa: E501

        :return: The approved of this TransactionDetail.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this TransactionDetail.

        Whether or not the transaction is approved  # noqa: E501

        :param approved: The approved of this TransactionDetail.  # noqa: E501
        :type: bool
        """
        if approved is None:
            raise ValueError("Invalid value for `approved`, must not be `None`")  # noqa: E501

        self._approved = approved

    @property
    def account_id(self):
        """Gets the account_id of this TransactionDetail.  # noqa: E501


        :return: The account_id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TransactionDetail.


        :param account_id: The account_id of this TransactionDetail.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def subtransactions(self):
        """Gets the subtransactions of this TransactionDetail.  # noqa: E501

        If a split transaction, the sub-transactions.  # noqa: E501

        :return: The subtransactions of this TransactionDetail.  # noqa: E501
        :rtype: list[SubTransaction]
        """
        return self._subtransactions

    @subtransactions.setter
    def subtransactions(self, subtransactions):
        """Sets the subtransactions of this TransactionDetail.

        If a split transaction, the sub-transactions.  # noqa: E501

        :param subtransactions: The subtransactions of this TransactionDetail.  # noqa: E501
        :type: list[SubTransaction]
        """
        if subtransactions is None:
            raise ValueError("Invalid value for `subtransactions`, must not be `None`")  # noqa: E501

        self._subtransactions = subtransactions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransactionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
