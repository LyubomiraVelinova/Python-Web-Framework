from django.urls import path

from charityapp.common.views import AboutUsView, index, our_people

urlpatterns = [
    path('', index, name='home-page'),
    path('about/', AboutUsView.as_view(), name='about-us-page'),
    path('people/', our_people, name='our-people-page'),
]
