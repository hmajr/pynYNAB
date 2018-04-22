import random
import time
import json
from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from pynYNAB.schema import AccountTypes
from pynYNAB.schema.budget import Account, Payee


def rate_limited(maxpersecond):
    minInterval = 1.0 / float(maxpersecond)

    def decorate(func):
        lastTimeCalled = [None]

        def rateLimitedFunction(*args, **kargs):
            if lastTimeCalled[0] is not None:
                elapsed = time.clock() - lastTimeCalled[0]
                leftToWait = minInterval - elapsed
                if leftToWait > 0:
                    print('rate limiting, waiting %g...' % leftToWait)
                    time.sleep(leftToWait)
            ret = func(*args, **kargs)
            lastTimeCalled[0] = time.clock()
            return ret

        return rateLimitedFunction

    return decorate


def get_or_create_account(client, name):
    accounts = {a.account_name: a for a in client.budget.accounts if
                a.account_name == name}
    if name in accounts:
        return accounts[name]

    account = Account(
        account_type=AccountTypes.Checking,
        account_name=name
    )

    client.add_account(account, balance=random.randint(-10, 10), balance_date=datetime.now())
    return account


def get_or_create_payee(client, name):
    payees = {p.name: p for p in client.budget.payees if
              p.name == name}
    if name in payees:
        return payees[name]
    payee = Payee(
        name=name
    )

    client.budget.payees.append(payee)
    client.push(1)
    return payee


# https://stackoverflow.com/a/37757378/1685379
def pp_json(json_thing, sort=True, indents=4):
    def d(t):
        return json.dumps(t, sort_keys=sort, indent=indents)
    return d(json.loads(json_thing)) if type(json_thing) is str else d(json_thing)
