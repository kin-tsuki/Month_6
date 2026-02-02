from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is not found")
        email = self.normalize_email(email)
        if phone_number:
            phone_number = self.normalize_phone_number(phone_number)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number is required for superuser!')
        
        phone_number = self.normalize_phone_number(phone_number)

        if not (phone_number.startswith('996') and len(phone_number) == 12):
            raise ValueError('Phone number must be in format "996XXXXXXXXX"')

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True")
        
        return self.create_user(email, phone_number, password, **extra_fields)
    
    @classmethod
    def normalize_phone_number(cls, phone_number):
        
        phone_number = phone_number or ""

        cleaned_data = ''.join(filter(str.isdigit, phone_number.strip()))

        if len(cleaned_data) == 12 and cleaned_data.startswith('996'):
            return cleaned_data
        
        if len(cleaned_data) == 9:
            return "996" + cleaned_data
        
        return phone_number
    
