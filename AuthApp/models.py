from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    twitch_id = models.CharField(max_length=100, unique=True)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    token_expires = models.DateTimeField(null=True)
    profile_image_url = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=False)
    description = models.TextField(blank=True, null=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
