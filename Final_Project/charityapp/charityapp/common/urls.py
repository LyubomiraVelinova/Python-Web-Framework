from django.urls import path

from charityapp.common.views import AboutUsView, index

urlpatterns = [
    path('', index, name='home-page'),
    path('about/', AboutUsView.as_view(), name='about-us-page'),
]
