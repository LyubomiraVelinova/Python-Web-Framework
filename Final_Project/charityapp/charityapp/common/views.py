from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from charityapp.charity.models import CharityCampaigns
from charityapp.common.forms import AboutUsInfoForm
from charityapp.common.models import AboutUsInfo


def index(request):
    campaigns = CharityCampaigns.objects.all()
    context = {
        'campaigns': campaigns
    }
    return render(request, 'common/home-page.html', context)


def our_people(request):
    return render(request, 'common/our-people.html')

# Only admins can make changes in the form info-DECORATOR IS NOT WORKING
# @user_passes_test(lambda u: u.is_superuser)
class AboutUsView(views.CreateView):
    template_name = 'common/about-us-page.html'
    form_class = AboutUsInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = AboutUsInfo.objects.first()
        context['info'] = self.form_class(instance=context['info'])
        return context

    def post(self, request, *args, **kwargs):
        info = AboutUsInfo.objects.first()
        form = self.form_class(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('about-us-page')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)
