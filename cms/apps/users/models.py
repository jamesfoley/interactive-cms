from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email).lower()
        user = self.model(
            email=email,
            is_staff=is_staff,
            last_login=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField(
        max_length=128,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=128,
        blank=True,
        null=True
    )

    email = models.EmailField(
        max_length=255,
        unique=True
    )

    is_staff = models.BooleanField(
        'Staff status',
        default=False
    )

    is_active = models.BooleanField(
        'Active',
        default=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return '{} {}'.format(
            self.first_name,
            self.last_name
        )

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
