from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Account

class AccountTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'medo@testemail.com'
        password = 'Testpassword12!'
        username= 'testuser'
        user = Account.objects.create_user(
            email=email,
            password=password,
            username=username
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'medo@TESTUSER.COM'
        user = Account.objects.create_user(email, 'test123!Wtest')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            Account.objects.create_user(None, 'test123')

    def test_create_superuser(self):
        user = Account.objects.create_superuser(
        email='testsuperuser@adminemail.com',
        password ='Testadmin123!',
        username= 'testadmin'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff) 


