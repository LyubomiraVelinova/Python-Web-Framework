from django.urls import path, include

from charityapp.charity.views import DonationListView, CampaignDetailsView

urlpatterns = [
    path('campaign/<int:pk>', CampaignDetailsView.as_view(), name='campaign-details-page'),
    path('donation/', DonationListView.as_view(), name='donation-campaigns-page'),
]
