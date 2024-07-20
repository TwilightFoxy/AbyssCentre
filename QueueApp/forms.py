from django import forms
from .models import Queue

class QueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = ['queue_type', 'comment']
