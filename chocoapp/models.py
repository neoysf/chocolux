from django.db import models

class Chocolate(models.Model):
    name = models.CharField(max_length = 255)
    price = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

class SocialLinks(models.Model):
    facebook = models.URLField(default="https://facebook.com/")
    tiktok = models.URLField(default="https://tiktok.com/")
    linkedin = models.URLField(default="https://linkedin.com/")

    def __str__(self):
        return "Social Media Links"

class SiteInfo(models.Model):
    location = models.CharField(max_length=255, default="Səbail rayonu, H.Z.Tağıyev 10 (Fəvvarələr Meydanı)")
    contact_email = models.EmailField(default="chocolux@gmail.com")
    contact_phone = models.CharField(max_length=20, default="+994 51 651 09 09")

    def __str__(self):
        return "Sayt Məlumatları"

class UserEmail(models.Model):
    email = models.EmailField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



