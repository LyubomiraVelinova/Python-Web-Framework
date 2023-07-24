from django.shortcuts import render
from django.views import generic as views


def volunteers(request):
    return render(request, 'get-involved/volunteers-page.html')


def ways_to_help(request):
    return render(request, 'get-involved/how-to-help-page.html')


class ReportToUsView(views.TemplateView):
    template_name = 'get-involved/report-to-us.html'
