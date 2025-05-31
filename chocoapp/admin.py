from django.contrib import admin
from chocoapp.models import Chocolate
from .models import ContactMessage
from .models import SocialLinks
from .models import SiteInfo
from .models import UserEmail

admin.site.register(Chocolate)
admin.site.register(SocialLinks)
admin.site.register(SiteInfo)
admin.site.register(UserEmail)
@admin.register(ContactMessage)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number')
    ordering = ('-created_at',)


