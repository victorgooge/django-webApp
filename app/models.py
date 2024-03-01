from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Account:
    pass

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    caption = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        quarter_cap = len(self.caption) // 4 
        return f"{self.caption[0:quarter_cap]}... | {self.owner.username}"
