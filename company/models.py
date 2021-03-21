from django.db import models
from django.urls import reverse

class Company(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField()
    active  = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("company:company-detail", kwargs={"id": self.id})
