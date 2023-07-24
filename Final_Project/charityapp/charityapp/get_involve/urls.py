from django.urls import path

from charityapp.common.views import AboutUsView, index
from charityapp.get_involve.views import volunteers, ways_to_help, ReportToUsView

urlpatterns = [
    path('volunteers/', volunteers, name='volunteers-page'),
    path('how-to-help/', ways_to_help, name='how-to-help-page'),
    path('report-to-us/', ReportToUsView.as_view(), name='report-to-us'),
]
