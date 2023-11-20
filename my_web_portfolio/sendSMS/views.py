from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .models import IncomingSMS
#from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
import logging

logger = logging.getLogger(__name__)
@csrf_exempt
@require_POST

def receive_sms(request):
    twilio_signature = request.headers.get('X-Twilio-Signature')
    if twilio_signature:
        incoming_message = request.POST.get('Body', '')
        sender_number = request.POST.get('From', '')
        twilio_number = request.POST.get('To', '')
        message_sid = request.POST.get('MessageSid', '')
        num_media = int(request.POST.get('NumMedia', 0))
        try:
            sms = IncomingSMS(
                sender_number=sender_number,
                twilio_number=twilio_number,
                message_body=incoming_message,
                message_sid=message_sid,
                num_media=num_media,)
            sms.save()
        except Exception as e:
            logger.error(f"Error processing incoming SMS: {e}")
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)


def send_sms(request):
    sms_messages = IncomingSMS.objects.all()
    if request.method == 'POST':
        try:
            twilio_account_sid = 'AC64fd9e4f482a213ba4162eb1405a3b62'
            twilio_auth_token = 'd363edbacf444c0547aa81dee1b09ed5'
            twilio_phone_number = '+16509008240'
            recipient_number = request.POST.get('recipient_number')
            message_text = request.POST.get('message_body')
            client = Client(twilio_account_sid, twilio_auth_token)
            message = client.messages.create(
                body=message_text,
                from_=twilio_phone_number,
                to=recipient_number)
        except Exception as e:
            return render(request, 'send_sms.html', {'error_message': str(e)})
        return redirect('send_sms')
    return render(request, 'send_sms.html', {'sms_messages': sms_messages})
