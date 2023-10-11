# ajax/models.py
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    is_accepted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    changed_by_admin = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']
