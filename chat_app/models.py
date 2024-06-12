from django.db import models
from users.models import User


class Conversation(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conv_coaches')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conv_clients")
    start_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender')
    text = models.CharField(max_length=200)
    attachment = models.FileField(blank=True, null=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='message_conv')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
