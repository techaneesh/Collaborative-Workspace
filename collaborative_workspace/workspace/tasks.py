from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_document_edit_notification(document_id, user_email):
    # Send an email notifying the user that their document has been edited
    send_mail(
        'Your document has been updated',
        f'Document ID: {document_id} has been updated.',
        'noreply@collaborativeworkspace.com',
        [user_email],
        fail_silently=False,
    )
