import factory
from datetime import date
from factory.fuzzy import FuzzyChoice, FuzzyDate
from models.account import Account

class AccountFactory(factory.Factory):
    """ Creates fake Accounts """

    class Meta:
        model = Account

    # Add attributes here...