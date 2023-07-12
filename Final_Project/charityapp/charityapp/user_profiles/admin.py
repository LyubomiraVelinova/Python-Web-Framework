from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from charityapp.user_profiles.forms import UserEditForm, UserCreateForm
from charityapp.user_profiles.models import SponsorUser, VolunteerUser, MemberUser

UserModel = get_user_model()


# @admin.register(UserModel)
# class UserModelAdmin(auth_admin.UserAdmin):
#     form = UserEditForm
#     add_form = UserCreateForm
#     fieldsets = (
#         (
#             None,
#             {
#                 "fields": (
#                     "username",
#                     "password"
#                 ),
#             }
#         ),
#         (
#             "Personal info",
#             {
#                 "fields": (
#                     "first_name",
#                     "last_name",
#                     "email"
#                 ),
#             }
#         ),
#         (
#             "Permissions",
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (
#             "Important dates",
#             {
#                 "fields": (
#                     "last_login",
#                     "date_joined"
#                 )
#             }
#         ),
#     )


# NOT SURE WHETER NEED THESE
@admin.register(SponsorUser)
class SponsorUserAdmin(admin.ModelAdmin):
    pass


@admin.register(VolunteerUser)
class SponsorUserAdmin(admin.ModelAdmin):
    pass


@admin.register(MemberUser)
class SponsorUserAdmin(admin.ModelAdmin):
    pass
