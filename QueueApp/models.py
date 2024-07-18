from django.db import models
from AuthApp.models import CustomUser

class Queue(models.Model):
    QUEUE_TYPES = [
        ('ABYSS', 'Abyss'),
        ('THEATRE', 'Theatre'),
        ('REVIEW', 'Review'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('DELATED', 'Delayed'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    queue_type = models.CharField(max_length=20, choices=QUEUE_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} – {self.queue_type} – {self.status}"