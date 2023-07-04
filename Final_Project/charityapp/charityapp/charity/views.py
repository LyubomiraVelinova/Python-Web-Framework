from django.shortcuts import render, get_object_or_404

from charityapp.charity.models import CharityCampaigns, DonationCampaigns, Users, SponsorsProfiles, HelperProfiles, \
    BenefactorsProfiles


# Implement at least 10 web pages, where 5 of them should use class-based views.

def index(request):
    return render(request, 'home-page.html')


def charity_campaigns_details(request):
    context = {
        'campaigns': CharityCampaigns.objects.all(),
    }
    return render(request, 'charity-campaigns-page.html', context)


def donation_campaigns_details(request):
    context = {
        'campaigns': DonationCampaigns.objects.all(),
    }
    return render(request, 'donation-campaigns-page.html', context)


def user_profile(request, user_id):
    context = {
        'user': get_object_or_404(Users, pk=user_id),
    }
    return render(request, 'user-profile-page.html', context)


def sponsor_profile(request, sponsor_id):
    context = {
        'sponsor': get_object_or_404(SponsorsProfiles, pk=sponsor_id),
    }
    return render(request, 'sponsor-profile-page.html', context)


def benefactor_profile(request, benefactor_id):
    context = {
        'benefactor': get_object_or_404(BenefactorsProfiles, pk=benefactor_id)
    }
    return render(request, 'benefactor-profile-page.html', context)


def helper_profile(request, helper_id):
    context = {
        'helper': get_object_or_404(HelperProfiles, pk=helper_id)
    }
    return render(request, 'helper-profile-page.html', context)


def register_user(request):
    return render(request, 'register-page.html')


def login_user(request):
    return render(request, 'login-page.html')
