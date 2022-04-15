from datetime import date
from factory import Factory, Sequence, Faker, LazyFunction
from factory.fuzzy import FuzzyChoice, FuzzyDate
from models.account import Account

class AccountFactory(Factory):
    """ Creates fake Accounts """

    class Meta:
        model = Account
