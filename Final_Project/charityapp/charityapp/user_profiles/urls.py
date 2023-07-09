from django.urls import path

from charityapp.user_profiles.views import ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('', ProfileDetailsView.as_view(), name='profile-details-page'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit-page'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete-page'),
    # path('sponsor/', sponsor_profile, name='sponsor-profile-page'),
    # path('volunteer/', volunteer_profile, name='volunteer-profile-page'),
    # path('member/', member_profile, name='member-profile-page'),

]
