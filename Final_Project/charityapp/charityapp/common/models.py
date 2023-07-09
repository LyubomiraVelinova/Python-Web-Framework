from django.db import models


class AboutUsInfo(models.Model):
    MAX_LENGTH_HEADER = 200

    header = models.CharField(
        max_length=MAX_LENGTH_HEADER,
    )
    description = models.TextField()
    last_updated = models.DateTimeField(
        auto_now=True,
    )
