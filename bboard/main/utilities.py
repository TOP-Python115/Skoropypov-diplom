from django.template.loader import render_to_string
from django.core.signing import Signer

from bboard.settings import ALLOWED_HOSTS

signer = Signer()


def create_host():
    if ALLOWED_HOSTS:
        return 'http://' + ALLOWED_HOSTS[0]
    return 'http://localhost:8000'


def send_activation_notification(user):
    host = create_host()
    contex = {
        'user': user,
        'host': host,
        'sign': signer.sign(user.username)
    }
    subject = render_to_string(
        'email/activation_letter_subject.txt',
        contex
    )
    body_text = render_to_string(
        'email/activation_letter_body.txt',
        contex
    )
    user.email_user(
        subject,
        body_text
    )
