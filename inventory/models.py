from email.policy import default
from django.db import models
from django.contrib.auth.models import User

LOCATION = (
    ("1st Floor", "1st Floor"),
    ("2nd Floor", "2nd Floor"),
    ("3rd Floor", "3rd Floor"),
    ("1st Floor Closet", "1st Floor Closet"),
    ("Closet 1", "Closet 1"),
    ("Closet 2", "Closet 2"),
    ("Closet 3", "Closet 3"),
    ("Closet 4", "Closet 4"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    picture = models.ImageField(default="avatar.jpeg", upload_to="Pictures")

    def __str__(self) -> str:
        return self.user.username


class Product(models.Model):
    artist = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=20, choices=LOCATION, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.artist



