"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models.account import Account

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Connect and load data needed by tests """
        db.create_all()

        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        db.session.query(Account).delete()

    def tearDown(self):
        """Remove the session"""

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_an_account(self):
        """Test creating an account"""
        account = Account(**ACCOUNT_DATA[0])
        account.create()
        self.assertEqual(len(Account.all()), 1)

    def test_create_all_accounts(self):
        """Test creating all accounts"""
        for account_data in ACCOUNT_DATA:
            account = Account(**account_data)
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))