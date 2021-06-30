from django.db import models
from django.utils import timezone

# add validator that checks if starts_at < ends_at


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    starts_at = models.DateTimeField(
        default=timezone.now, blank=False, null=False)
    ends_at = models.DateTimeField(
        default=timezone.now, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"""
            Name: {self.name}
            Description: {self.description}
            Starts at: {self.starts_at}
            Ends at: {self.ends_at}
            Created at: {self.created_at}        
        """
