from django.contrib import admin
from django.contrib.auth import get_user_model

from charityapp.common.models import AboutUsInfo
from charityapp.user_profiles.models import SponsorUser, VolunteerUser, MemberUser

# UserModel = get_user_model()
#
#
# @admin.register(AboutUsInfo)
# class UserModelAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ('Info', {
#             'fields': ('header', 'description')
#         }),
#         ('Updated on', {
#             'fields': ('last_updated',)
#         }),
#     )
