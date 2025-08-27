from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=120)
    profile_pic = models.ImageField(upload_to='profileapp/')  # -> /media/profiles/
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
