from django.contrib.auth import get_user_model
from django.test import TestCase

from littleauth.forms import RegisterForm, LoginForm


class RegisterFormTest(TestCase):
    def test_valid(self):
        data = {"email": "user@email.com"}
        form = RegisterForm(data)
        self.assertTrue(form.is_valid())
        user = form.save()
        user.refresh_from_db()
        self.assertIsNotNone(user.id)

    def test_email_exists(self):
        data = {"email": "user@email.com"}

        get_user_model().objects.create(email=data["email"])

        form = RegisterForm(data)
        self.assertFalse(form.is_valid())


class LoginFormTest(TestCase):
    def test_valid(self):
        data = {"email": "user@email.com", "password": "test"}
        get_user_model().objects.create_user(
            email=data["email"], password=data["password"]
        )

        form = LoginForm(data)
        self.assertTrue(form.is_valid())

    def test_user_inactive(self):
        data = {"email": "user@email.com", "password": "test"}
        user = get_user_model().objects.create_user(
            email=data["email"], password=data["password"]
        )
        user.is_active = False
        user.save()

        form = LoginForm(data)
        self.assertFalse(form.is_valid())

    def test_user_does_not_exist(self):
        data = {"email": "user@email.com", "password": "test"}
        form = LoginForm(data)
        self.assertFalse(form.is_valid())
