from django.contrib import admin
from .models import Users, Organization
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = "HMS's Admin"
admin.site.index_title = 'Teja'
# admin.site.name = 'Teja'

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'is_active', 'valid_until')
    list_filter = ('is_active', 'valid_until')
    search_fields = ('first_name', 'last_name', 'phone')
    # exclude = ['password']

    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'is_active', 'valid_until')
    list_filter = ('company_name', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'company_name')

    def has_delete_permission(self, request, obj=None):
        return False
# admin.site.unregister(Organization)
admin.site.unregister(Group)