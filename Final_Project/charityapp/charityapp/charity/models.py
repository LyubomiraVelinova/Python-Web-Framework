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

# def validate_only_alphanumeric(value):
#     for ch in value:
#         if not ch.isalnum():
#             raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
