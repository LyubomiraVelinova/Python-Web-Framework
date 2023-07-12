from django.views import generic as views

from charityapp.charity.models import CharityCampaigns, DonationCampaigns


# Implement at least 10 web pages, where 5 of them should use class-based views.


class CampaignDetailsView(views.DetailView):
    model = CharityCampaigns
    template_name = 'charity/campaign-details-page.html'
    context_object_name = 'campaigns'


class DonationListView(views.ListView):
    template_name = 'charity/donations-page.html'
    model = DonationCampaigns
