from django.urls import path, include

from charityapp.charity.views import index, charity_campaigns_details, donation_campaigns_details, user_profile, \
    sponsor_profile, benefactor_profile, helper_profile, register_user, login_user

urlpatterns = [
    path('', index, name='home-page'),
    path('charity/', charity_campaigns_details, name='charity-campaigns-page'),
    path('donation/', donation_campaigns_details, name='donation-campaigns-page'),
    path('user/<int:user_id>/', include([
        path('', user_profile, name='user-profile-page'),
        path('sponsor/<int:sponsor_id>', sponsor_profile, name='sponsor-profile-page'),
        path('benefactor/<int:benefactor_id>', benefactor_profile, name='benefactor-profile-page'),
        path('helper/<int:helper_id>', helper_profile, name='helper-profile-page'),
    ])),
    path('signup/', register_user, name='signup-user-page'),
    path('login/', login_user, name='login-user-page'),

]
