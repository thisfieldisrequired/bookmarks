from django.contrib.auth.models import User
from .models import Profile


class EmailAuthBackend:
    """Аутентификация по имейлу"""

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


def create_profile(backend, user, *args, **kwargs):
    """Создание профиля пользователя при регистрации"""
    Profile.objects.get_or_create(user=user)
