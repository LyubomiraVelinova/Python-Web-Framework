from django import views
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.views import generic as views

UserModel = get_user_model()


class ProfileDetailsView(views.DetailView):
    template_name = 'user_profiles/profile-details-page.html'
    model = UserModel

    # To work provide either 'model', 'queryset' or 'get_queryset'

    def get_context_data(self, **kwargs):
        # NOT WORKING
        profile_image = static('images/smile')

        if self.object.profile_picture is not None:
            profile_image = self.object.profile_picture

        context = super().get_context_data(**kwargs)
        context['profile_image'] = profile_image

        return context


class ProfileEditView(views.UpdateView):
    template_name = 'user_profiles/profile-edit-page.html'


class ProfileDeleteView(views.DeleteView):
    template_name = 'user_profiles/profile-delete-page.html'


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
