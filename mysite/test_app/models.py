from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def _create_user(self, email, password, firstname, lastname, phone_number, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            phone_number=phone_number,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, firstname, lastname, phone_number, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, firstname, lastname, phone_number, **extra_fields)

    def create_superuser(self, email, password, firstname, lastname, phone_number, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, firstname, lastname, phone_number, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=250)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=50)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_supervisor = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phone_number']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    website = models.TextField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
