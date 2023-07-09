from django.views import generic as views

from charityapp.charity.models import CharityCampaigns, DonationCampaigns


# Implement at least 10 web pages, where 5 of them should use class-based views.


# CBV
class CharityCampaignsView(views.TemplateView):
    template_name = 'charity/campaigns-page.html'
    extra_context = {
        'campaigns': CharityCampaigns.objects.all(),
    }


class DonationCampaignsView(views.TemplateView):
    template_name = 'charity/donations-page.html'
    extra_context = {
        'campaigns': DonationCampaigns.objects.all(),
    }
