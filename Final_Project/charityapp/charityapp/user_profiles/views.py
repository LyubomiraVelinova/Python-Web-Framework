from django.contrib.auth import get_user_model
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from charityapp.user_profiles.forms import VolunteerForm, SponsorForm, MemberForm


UserModel = get_user_model()


class ProfileView(views.CreateView):
    template_name = 'accounts/additional-info-page.html'
    form_class = None
    success_url = reverse_lazy('home-page')
    user_type = None

    def get_form_class(self):
        user_type = self.kwargs['user_type']
        print(user_type)
        if user_type == 'VOLUNTEER':
            return VolunteerForm
        elif user_type == 'SPONSOR':
            return SponsorForm
        elif user_type == 'MEMBER':
            return MemberForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_type = self.kwargs.get('user_type')
        context['user_type'] = user_type
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.form_class is not None:
            kwargs['prefix'] = self.form_class.__name__.lower()
        return kwargs

# FOR DELETE
# class ProfileDetailsView(views.DetailView):
#     template_name = 'user_profiles/profile-details-page.html'
#     model = UserModel
#
#     # To work provide either 'model', 'queryset' or 'get_queryset'
#
#     def get_context_data(self, **kwargs):
#         # NOT WORKING
#         profile_image = static('images/smile')
#
#         if self.object.profile_picture is not None:
#             profile_image = self.object.profile_picture
#
#         context = super().get_context_data(**kwargs)
#         context['profile_image'] = profile_image
#
#         return context


class ProfileEditView(views.UpdateView):
    template_name = 'user_profiles/profile-edit-page.html'


class ProfileDeleteView(views.DeleteView):
    template_name = 'user_profiles/profile-delete-page.html'


class VolunteerListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'user_profiles/volunteers-list-page.html'






# DO I REALLY NEED THIS??? AND THIS TEMPLATES???
# @login_required
# def sponsor_profile(request, sponsor_id):
#     context = {
#         'sponsor': get_object_or_404(SponsorsProfiles, pk=sponsor_id),
#     }
#     return render(request, 'sponsor-profile-page.html', context)
#
#
# @login_required
# def benefactor_profile(request, benefactor_id):
#     context = {
#         'benefactor': get_object_or_404(BenefactorsProfiles, pk=benefactor_id)
#     }
#     return render(request, 'benefactor-profile-page.html', context)
#
# @login_required
# def helper_profile(request, helper_id):
#     context = {
#         'helper': get_object_or_404(HelperProfiles, pk=helper_id)
#     }
#     return render(request, 'helper-profile-page.html', context)

