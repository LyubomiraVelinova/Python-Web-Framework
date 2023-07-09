from django.urls import path, include

from charityapp.charity.views import DonationCampaignsView, CharityCampaignsView

urlpatterns = [
    path('charity/', CharityCampaignsView.as_view(), name='charity-campaigns-page'),
    path('donation/', DonationCampaignsView.as_view(), name='donation-campaigns-page'),
]
