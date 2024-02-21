from celery import shared_task
from django.core.mail import send_mail
from .models import Reservacion

@shared_task
def confirmar_reserva(reserva_id):
    # Lógica para confirmar la reserva
    reserva = Reservacion.objects.get(id=reserva_id)
    reserva.confirmada = True
    reserva.save()

@shared_task
def enviar_correo_confirmacion(email):
    # Lógica para enviar un correo electrónico de confirmación
    send_mail(
        'Confirmación de Reserva',
        'Su reserva ha sido confirmada exitosamente.',
        'from@example.com',
        [email],
        fail_silently=False,
    )