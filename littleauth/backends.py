from django.contrib.auth import get_user_model


class NoPasswordBackend(object):
    def authenticate(self, email):
        try:
            user = get_user_model().objects.get(email=email)
        except User.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

