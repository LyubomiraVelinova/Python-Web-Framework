from django.urls import path

from charityapp.common.views import AboutUsView, index, our_people, mission_and_values, our_work, our_history

urlpatterns = [
    path('', index, name='home-page'),
    path('about/', AboutUsView.as_view(), name='about-us-page'),
    path('people/', our_people, name='our-people-page'),
    path('mission/', mission_and_values, name='mission-and-values-page'),
    path('work/', our_work, name='our-work-page'),
    path('history/', our_history, name='our-history-page'),
]
