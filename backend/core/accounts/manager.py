from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        
        email=self.normalize_email(email=email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_validator",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_admin",True)

        if extra_fields.get("is_validator") is not True:
            raise ValueError("Superuser must have is_validator=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        
        return self.create_user(email=email,password=password,**extra_fields)
