from django.contrib import admin

from .models import ContactForm, Newsletter

# Register your models here.


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_phone', 'message_subject', 'sent_at')
    list_filter = ('sent_at', 'sender_name', 'sender_phone', 'message_subject')
    search_fields = ('sender_name', 'sender_phone', 'message_subject', 'message_text')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'registered_at')
    list_filter = ('user_email', 'registered_at')
    search_fields = ('user_email',)
