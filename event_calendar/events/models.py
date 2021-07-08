from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings

# tell users what type of form it is


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    starts_at = models.DateTimeField(
        default=timezone.now, blank=False, null=False)
    ends_at = models.DateTimeField(
        default=timezone.now, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"""
            Name: {self.name}
            Description: {self.description}
            Starts at: {self.starts_at}
            Ends at: {self.ends_at}
            Created at: {self.created_at}        
        """

    def clean(self):
        super().clean()  # calling the default validators and other things that clean() does
        if self.ends_at < self.starts_at:
            raise ValidationError(
                "An event cannot end before it even started!")
