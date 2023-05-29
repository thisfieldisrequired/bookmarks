from django.contrib.auth.models import User


class EmailAuthBackend:
    def authenticate(self, request, username=None, password=None):
        user = User.objects.get(email=username)
        try:
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None
