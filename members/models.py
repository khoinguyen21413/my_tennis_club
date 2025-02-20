from django.db import models

# Create your models here.
class Member(models.Model):
    # Define field
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    join_date = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"