from django.db import models

# Create your models here.
from django.urls import reverse


class Bike (models.Model):
    bike_no = models.CharField(unique=True, max_length=50, null=False)
    device_id = models.IntegerField(unique=True)
    bike_status = models.IntegerField(null=False)
    last_full_maintainance_date = models.DateField(null=False)



    def get_absolute_url(self):
        return reverse("bike:bike-detail", kwargs={"id": self.id})  # f"/bikes/{self.id}/"