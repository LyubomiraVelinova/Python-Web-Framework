from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


# # Charities Model:
# # Name: A CharField to store the name of the charity.
# # Description: A TextField to store a detailed description of the charity.
# # Motivation: A TextField to store what are the motives of the campaign.
# # Type: A Charfield(drop-down list) to choose type of charity.
# # Logo: An ImageField to store the logo or image representing the charity.
# # Website: A URLField to store the website URL of the charity.
# # Contact Information: Fields like EmailField, CharField, or PhoneNumberField to store the contact information of the charity.
# # Many-to-Many Relationships: You can include many-to-many relationships with other models, such as categories or donation campaigns that the charity is associated with.


class CharityCampaigns(models.Model):
    MAX_LEN_NAME = 50
    MAX_LEN_TYPE = 50

    TYPE_CHOICES = (
        ("1", "Environmental Charity"),
        ("2", "Children’s Charity"),
        ("3", "Human Rights Charity"),
        ("4", "Disaster Relief Charity"),
        ("5", "Scientific Research Charity"),
        ("6", "Senior Citizen Charity"),
        ("7", "Cultural Charity"),
        ("8", "Animal-Based Charity"),
        ("9", "Sports-Based Charity"),
        ("10", "Education Charity"),
        ("11", "Other"),
    )

    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )
    description = models.TextField()
    motivation = models.TextField()
    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        choices=TYPE_CHOICES,
    )
    # logo = models.ImageField()
    website = models.URLField()
    # Check this
    period = models.DurationField()

    def __str__(self):
        return self.name


# DonationCampaigns Model:
# Title: A CharField to store the title or name of the donation campaign.
# Description: A TextField to store a description of the campaign and its purpose.
# Goal Amount: A DecimalField to store the target amount to be raised for the campaign.
# Current Amount: A DecimalField to store the current amount of donations received for the campaign.
# Start Date and End Date: DateFields to define the duration of the campaign.
# Many-to-One Relationship: You can include a foreign key to the Charities model to associate the campaign with a specific charity.
# Many-to-Many Relationships: You can include many-to-many relationships with other models, such as users who have donated to the campaign.


class DonationCampaigns(models.Model):
    MAX_LEN_TITLE = 100

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
    )
    description = models.TextField()
    motivation = models.TextField()
    goal_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    current_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    start_date = models.DateField()
    end_date = models.DateField()

    # Many to many fields

    def __str__(self):
        return self.title


# Users Model:
# Username: A CharField to store the username of the user.
# Password: A CharField to store the hashed password of the user.
# First Name: A CharField to store the first name of the user.
# Last Name: A CharField to store the last name of the user.
# Email: An EmailField to store the email address of the user.
# Role: A CharField or ForeignKey to store the role or type of user (e.g., sponsor, benefactor, helper).
# Many-to-One Relationships: You can include many-to-one relationships with other models, such as linking a user to their respective profile (SponsorsProfiles, BenefactorsProfiles, HelpersProfiles).


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum():
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Users(models.Model):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 20
    MAX_LEN_PASSWORD = 30
    MAX_LEN_USER_TYPE = 30

    USER_TYPE_CHOICES = (
        ("1", "Sponsor"),
        ("1", "Benefactor"),
        ("1", "Helper"),
    )

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
    username = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
            validate_only_alphanumeric,
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        null=False,
        blank=False,
    )
    # Check that
    user_type = models.CharField(
        max_length=MAX_LEN_USER_TYPE,
        choices=USER_TYPE_CHOICES,
    )
    # Do I really need this field???
    interests = models.TextField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


# SponsorsProfiles Model:
# User: A OneToOneField to link the sponsor's profile with the corresponding user.
# Company Name: A CharField to store the name of the sponsoring company.
# Contact Information: Fields like EmailField, CharField, or PhoneNumberField to store the contact information of the sponsor.
# Donation History: A ManyToManyField to store the donation campaigns the sponsor has contributed to.

# For business
class SponsorsProfiles(models.Model):
    MAX_LEN_NAME = 50
    MAX_LEN_CAREER = 100

    CAREER_FIELD_CHOICES = (
        ("1", "Architecture and Construction"),
        ("2", "Accounting, Banking and Finance"),
        ("3", "Agriculture, Farming and Food"),
        ("4", "Arts, Culture and Entertainment"),
        ("5", "Business, management and administration"),
        ("6", "Communications"),
        ("7", "Computer Technology"),
        ("8", "Customer Service and Sales"),
        ("9", "Education and Training"),
        ("10", "Environment"),
        ("11", "Government and Military"),
        ("12", "Health and Medical"),
        ("13", "Hospitality, Travel and Tourism"),
        ("14", "Installation, Maintenance and Repair"),
        ("15", "Law, Public Policy, Enforcement and Safety"),
        ("16", "Manufacturing and Production"),
        ("17", "Media and Broadcast"),
        ("18", "STEM (Science, Technology, Engineering and Mathematics)"),
        ("19", "Social, Charity and Community Service"),
        ("20", "Transport and Distribution"),
        ("21", "Other"),
    )

    sponsor = models.OneToOneField(
        Users,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    company_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )
    career_field = models.CharField(
        max_length=MAX_LEN_CAREER,
        choices=CAREER_FIELD_CHOICES,
        null=True,
        blank=True,
    )
    donation_history = models.ManyToManyField(DonationCampaigns)


# BenefactorsProfiles Model:
# User: A OneToOneField to link the benefactor's profile with the corresponding user.
# Contact Information: Fields like EmailField, CharField, or PhoneNumberField to store the contact information of the benefactor.
# Donation History: A ManyToManyField to store the donation campaigns the benefactor has contributed to.
# Wishlist: A ManyToManyField to store the charities or donation campaigns the benefactor has added to their wishlist.

# For every person
class BenefactorsProfiles(models.Model):
    user = models.OneToOneField(
        Users,
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


# HelpersProfiles Model:
# User: A OneToOneField to link the helper's profile with the corresponding user.
# Contact Information: Fields like EmailField, CharField, or PhoneNumberField to store the contact information of the helper.
# Role: A CharField to store the role or position of the helper in the campaign.
# Contribution History: A ManyToManyField to store the donation campaigns or charity projects the helper has contributed to.


# For those who helps during campaigns
class HelperProfiles(models.Model):
    MAX_LENGTH_INTERESTS = 50
    MAX_LENGTH_ROLE = 50

    INTERESTS_CHOICES = (
        ("1", "Environmental causes"),
        ("2", "Humanitarian causes"),
        ("3", "Causes of disasters and accidents"),
        ("4", "Animal causes"),
        ("5", "Other"),
    )
    ROLE_CHOICES = (
        ("1", "Chairman"),
        ("1", "Vice Chairman"),
        ("1", "Secretary"),
        ("1", "Administrator"),
        ("1", "Moderator"),
        ("1", "Cashier"),
        ("1", "Public Relations (PR)"),
        ("1", "Volunteer"),
        ("1", "Field volunteer"),
        ("1", "Member of the Club"),
    )

    user = models.OneToOneField(
        Users,
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
        max_length=MAX_LENGTH_INTERESTS,
        choices=INTERESTS_CHOICES,
        default="1",
    )
    role = models.CharField(
        max_length=MAX_LENGTH_ROLE,
        choices=ROLE_CHOICES,
    )
    contribution_history = models.ManyToManyField(CharityCampaigns)
