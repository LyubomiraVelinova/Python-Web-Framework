from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from charityapp.charity.models import DonationCampaigns, CharityCampaigns


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class ChoicesStringsMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Gender(ChoicesStringsMixin, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'


class UserType(ChoicesStringsMixin, Enum):
    SPONSOR = "Sponsor"
    VOLUNTEER = "Volunteer"
    MEMBER = "Member"


# class CareerFields(ChoicesStringsMixin, Enum):
#     ARCHITECTURE_AND_CONSTRUCTION = "ARCHITECTURE AND CONSTRUCTION"
#     ACCOUNTING_BANKING_AND_FINANCE = "ACCOUNTING, BANKING AND FINANCE"
#     AGRICULTURE_FARMING_AND_FOOD = "AGRICULTURE, FARMING AND FOOD"
#     ARTS_CULTURE_AND_ENTERTAINMENT = "ARTS, CULTURE AND ENTERTAINMENT"
#     BUSINESS_MANAGEMENT_AND_ADMINISTRATION = "BUSINESS, MANAGEMENT AND ADMINISTRATION"
#     COMMUNICATIONS = "COMMUNICATIONS"
#     COMPUTER_TECHNOLOGY = "COMPUTER TECHNOLOGY"
#     CUSTOMER_SERVICE_AND_SALES = "CUSTOMER SERVICE AND SALES"
#     EDUCATION_AND_TRAINING = "EDUCATION AND TRAINING"
#     ENVIRONMENT = "ENVIRONMENT"
#     GOVERNMENT_AND_MILITARY = "GOVERNMENT AND MILITARY"
#     HEALTH_AND_MEDICAL = "HEALTH AND MEDICAL"
#     HOSPITALITY_TRAVEL_AND_TOURISM = "HOSPITALITY, TRAVEL AND TOURISM"
#     INSTALLATION_MAINTENANCE_AND_REPAIR = "INSTALLATION, MAINTENANCE AND REPAIR"
#     LAW_PUBLIC_POLICY_ENFORCEMENT_AND_SAFETY = "LAW, PUBLIC POLICY, ENFORCEMENT AND SAFETY"
#     MANUFACTURING_AND_PRODUCTION = "MANUFACTURING AND PRODUCTION"
#     MEDIA_AND_BROADCAST = "MEDIA AND BROADCAST"
#     STEM = "STEM"
#     SOCIAL_CHARITY_AND_COMMUNITY_SERVICE = "SOCIAL, CHARITY AND COMMUNITY SERVICE"
#     TRANSPORT_AND_DISTRIBUTION = "TRANSPORT AND DISTRIBUTION"
#     OTHER = "OTHER"


class CharityUser(auth_models.AbstractUser):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        # Required field
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    gender = models.CharField(
        max_length=MAX_LEN_NAME,
        choices=Gender.choices(),
        default=Gender.DO_NOT_SHOW,
    )

    user_type = models.CharField(
        max_length=MAX_LEN_NAME,
        choices=UserType.choices(),
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    interests = models.TextField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class SponsorUser(models.Model):
    MAX_LEN_NAME = 100
    MAX_LEN_CAREER = 100

    sponsor = models.OneToOneField(
        CharityUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    company_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )
    contact_name = models.CharField(
        max_length=MAX_LEN_NAME,
    )
    contact_email = models.EmailField()
    website = models.URLField()
    # DO I REALLY NEED IT?
    # logo = models.ImageField(upload_to='sponsor_logos')
    career_field = models.CharField(
        max_length=MAX_LEN_CAREER,
        null=True,
        blank=True,
    )
    donation_history = models.ManyToManyField(DonationCampaigns)

    def __str__(self):
        return self.company_name


class VolunteerUser(models.Model):
    volunteer = models.OneToOneField(
        CharityUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone_number = models.IntegerField(
        null=False,
        blank=False,
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )
    charity_history = models.ManyToManyField(CharityCampaigns)
    donation_history = models.ManyToManyField(DonationCampaigns)


class CharityInterests(ChoicesStringsMixin, Enum):
    ENVIRONMENTAL_CAUSES = "Environmental causes"
    HUMANITARIAN_CAUSES = "Humanitarian causes"
    DISASTERS_AND_ACCIDENTS_CAUSES = "Causes of disasters and accidents"
    ANIMAL_CAUSES = "Animal causes"
    OTHER = "Other"


class RoleTypes(ChoicesStringsMixin, Enum):
    CHAIRMAN = "Chairman"
    VICE_CHAIRMAN = "Vice Chairman"
    SECRETARY = "Secretary"
    ADMINISTRATOR = "Administrator"
    MODERATOR = "Moderator"
    CASHIER = "Cashier"
    PR = "Public Relations (PR)"
    # NOT SURE ABOUT THIS???
    VOLUNTEER = "Volunteer"
    FIELD_VOLUNTEER = "Field volunteer"
    MEMBER = "Member of the Club"


class MemberUser(models.Model):
    MAX_LENGTH_INTERESTS = 50
    MAX_LENGTH_ROLE = 50

    member = models.OneToOneField(
        CharityUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone_number = models.IntegerField(
        null=False,
        blank=False,
    )
    strengths = models.TextField(
        null=True,
        blank=True,
    )
    interests = models.CharField(
        max_length=CharityInterests.max_length(),
        choices=CharityInterests.choices(),
    )
    role = models.CharField(
        max_length=RoleTypes.max_length(),
        choices=RoleTypes.choices(),
    )
    contribution_history = models.ManyToManyField(CharityCampaigns)
