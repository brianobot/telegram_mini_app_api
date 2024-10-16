from django.contrib.auth.models import UserManager as DjangoUserManager
from django.contrib.auth.hashers import make_password


class UserManager(DjangoUserManager):
    """
    Custom user manager for managing users based on the `id` field only.
    """
    def create_user(self, id, password=None, **extra_fields):
        """
        Create and return a regular user with a given `id`.
        """
        if not id:
            raise ValueError('The User ID must be set')

        user = self.model(id=id, **extra_fields)
        # user.set_password(password)
        user.password = make_password(password)
        user._password = password

        user.save(using=self._db)
        return user

    def create_superuser(self, id: str, password: str, **extra_fields):
        """
        Create and return a superuser with a given `id` and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(id=id, password=password, **extra_fields)
