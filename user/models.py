from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    """custom user manager class"""
    use_in_migration = True

    def _create_user(self, phone, email, password, **extra_fields):
        """
        Creates and saves a User without default required username field.
        """
        if not phone:
            raise ValueError('The given phone must be set')
        if email:
            email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.phone = phone
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, email, password, **extra_fields)


class User(AbstractBaseUser):
    username        = None
    email           = models.EmailField(_('Email'), null=True, blank=True, unique=True, max_length=120)
    first_name      = models.CharField(_('First Name'), max_length=100)
    last_name       = models.CharField(_('Last Name'), max_length=100)
    is_active       = models.BooleanField(_('Active'), default=False)
    is_staff        = models.BooleanField(_('Admin Access'), default=False)
    is_superuser    = models.BooleanField(_('Superuser'), default=False)
    phone           = PhoneNumberField(_('phone'), blank=False, null=False, max_length=16, unique=True)
    department      = models.ForeignKey('timetable.Department', related_name='lecturers', on_delete = models.DO_NOTHING, blank=False, null=True)    
    courses         = models.ManyToManyField('timetable.Course', blank=True)
    last_login      = models.DateTimeField(_('last_login'), auto_now=True)
    date_joined     = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}".strip().title()

    def __str__(self):
        return self.get_full_name()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
