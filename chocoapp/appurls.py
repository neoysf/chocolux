from django.urls import path
from .views import home_view, about_view, chocolate_view, testimonial_view, contact_view, footer_email_view

app_name = 'chocoapp'

urlpatterns = [
    path('', home_view, name='home'),
    path('index', home_view, name = 'home'),
    path('about', about_view, name='about'),
    path('chocolate', chocolate_view, name='chocolate'),
    path('testimonial', testimonial_view, name='testimonial'),
    path('contact', contact_view, name='contact'),
    path('footer-email/', footer_email_view, name='footer_email'),
]


