from django.db import models

# Create your models here.


class ContactForm(models.Model):
    sender_name = models.CharField(max_length=150)
    sender_phone = models.CharField(max_length=15)
    message_subject = models.CharField(max_length=150)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender_name


class Newsletter(models.Model):
    user_email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email
