from django.http import JsonResponse
from django.utils.html import escape

from .models import ContactForm, Newsletter

# Create your views here.


def save_contact_form(request):
    if request.method == 'POST':
        sender_name = escape(request.POST.get('sender_name'))
        sender_phone = escape(request.POST.get('sender_phone'))
        message_subject = escape(request.POST.get('message_subject'))
        message_text = escape(request.POST.get('message_text'))

        contact_form = ContactForm(
            sender_name=sender_name,
            sender_phone=sender_phone,
            message_subject=message_subject,
            message_text=message_text,
        )
        contact_form.save()

        return JsonResponse({'success': 'true'})


def save_newsletter_signup(request):
    if request.method == 'POST':
        user_email = escape(request.POST.get('user_email'))

        newsletter = Newsletter(user_email=user_email)
        newsletter.save()

        return JsonResponse({'success': 'true'})
