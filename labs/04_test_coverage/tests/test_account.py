"""
Test Cases TestAccountModel
"""
import json
from random import randrange
from unittest import TestCase
from models import db
from models.account import Account, DataValidationError

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        db.create_all()  # make our sqlalchemy tables
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnext from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        self.rand = randrange(0, len(ACCOUNT_DATA))
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_all_accounts(self):
        """ Test creating multiple Accounts """
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))

    def test_create_an_account(self):
        """ Test Account creation using known data """
        data = ACCOUNT_DATA[self.rand] # get a random account
        account = Account(**data)
        account.create()
        self.assertEqual(len(Account.all()), 1)

    def test_represent_as_string(self):
        """Test representing an account as a string"""
        account = Account(name = "Foo")
        self.assertEqual(str(account), "<Account 'Foo'>")

    def test_to_dict(self):
        """Test to dictionary"""
        data = ACCOUNT_DATA[self.rand] # get a random account
        account = Account(**data)
        result = account.to_dict()
        self.assertEqual(result["name"], account.name)
        self.assertEqual(result["email"], account.email)
        self.assertEqual(result["phone_number"], account.phone_number)
        self.assertEqual(result["disabled"], account.disabled)

    def test_from_dict(self):
        """Test from dictionary"""
        data = ACCOUNT_DATA[self.rand] # get a random account
        account = Account(**data)
        account.from_dict(data)
        self.assertEqual(data["name"], account.name)
        self.assertEqual(data["email"], account.email)
        self.assertEqual(data["phone_number"], account.phone_number)
        self.assertEqual(data["disabled"], account.disabled)

    def test_update_an_account(self):
        """Test update an account"""
        data = ACCOUNT_DATA[self.rand] # get a random account
        account = Account(**data)
        account.create()
        self.assertEqual(len(Account.all()), 1)
        account.name = "Foo"
        account.update()
        found = Account.find(account.id)
        self.assertEqual(found.name, account.name)

    def test_update_without_id(self):
        """Test update an account without id"""
        account = Account()
        account.id = None
        self.assertRaises(DataValidationError, account.update)

    def test_delete_an_account(self):
        """Test delete an account"""
        data = ACCOUNT_DATA[self.rand] # get a random account
        account = Account(**data)
        account.create()
        self.assertEqual(len(Account.all()), 1)
        account.delete()
        self.assertEqual(len(Account.all()), 0)
        