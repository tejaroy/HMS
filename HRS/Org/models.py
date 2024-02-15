from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator


#Model for all users detials
class Users(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=10, null=False, blank=False, unique=True)
    password = models.CharField(max_length=500, null=False, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=False)
    valid_until = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_now_add= True, blank=False)
    updated_at = models.DateTimeField(auto_now_add= True, blank=False)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users Details'

    def __str__(self):
        return self.first_name + ' '+ self.last_name 
        
    
# Model for Organization
class Organization(models.Model):
    first_name = models.CharField(max_length= 250, null= False, blank= False)
    last_name = models.CharField(max_length= 250, null= False, blank= False)
    company_name = models.CharField(max_length= 250, null=False, blank= False)
    phone = models.CharField(max_length=500, null=False, blank=True)
    email = models.EmailField(null= False, blank= False)
    address = models.TextField(null= False, blank= False)
    valid_until = models.DateTimeField(null= False, blank= False)
    is_active = models.BooleanField(null=False, blank=False, default=False)
    org_id = models.CharField(max_length=10, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add= True, blank=False)
    updated_at = models.DateTimeField(auto_now_add= True, blank=False)
    created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=False)
    # updated_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Client Details'
    
    def __str__(self):
        return self.company_name


