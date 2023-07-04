from django.urls import path

from charity_for_future.common.views import index

urlpatterns = [
    path('', index, name='home-page'),
]
