from django.urls import path

from charity_for_future.club.views import about_us

urlpatterns = [
    path('about-us', about_us, name='about us'),
]
