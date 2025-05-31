from .models import SiteInfo

def site_info(request):
    site_info = SiteInfo.objects.first()
    return {
        "location": site_info.location if site_info else "Məlumat tapılmadı",
        "contact_email": site_info.contact_email if site_info else "Məlumat tapılmadı",
        "contact_phone": site_info.contact_phone if site_info else "Məlumat tapılmadı",
    }
