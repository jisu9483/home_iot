from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)

class MyUserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not name:
            raise ValueError('필수 입력 요소 입니다.')
            
        if not email:
            raise ValueError('필수 입력 요소 입니다.')
 
        user = self.model(
            name= name,
            email=MyUserManager.normalize_email(email),
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_admin = True
        user.save(using=self._db)
     
        return user
 
 
class MyUser(AbstractBaseUser):  
    name = models.CharField(max_length=64, blank=False, default='',verbose_name='ID', unique=True)  
    email = models.EmailField(
        verbose_name='email',
        max_length=128,
    )    
    is_admin = models.BooleanField(default=False,verbose_name="관리자확인")
    is_active = models.BooleanField(default=True,verbose_name="활동중")
 
    objects = MyUserManager()
 
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS =  ['email']
 
    def __str__(self):
        return self.name
 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin