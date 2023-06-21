from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, login, password=None):
        user=self.model(login=login)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password):
        user=self.create_user(login=login, password=password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.role=1
        user.save(using=self._db)
        return user