from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
from .models import Reservacion, Habitacion
from .serializers import ReservacionSerializer, HabitacionSerializer
from .tasks import confirmar_reserva, enviar_correo_confirmacion
from rest_framework.decorators import api_view

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservacionViewSet(viewsets.ModelViewSet):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                habitacion_id = request.data.get('habitacion')
                habitacion = Habitacion.objects.select_for_update().get(pk=habitacion_id)

                version_usuario = request.data.get('version')
                if version_usuario is None or int(version_usuario) != habitacion.version:
                    return JsonResponse({'error': 'La habitación ha sido reservada por otro usuario.'}, status=400)

                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)

                reserva = serializer.instance

                confirmar_reserva.delay(reserva.id)
                enviar_correo_confirmacion.delay(reserva.cliente_email)

                return JsonResponse(serializer.data, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def update(self, request, *args, **kwargs):
        habitacion_id = request.data.get('habitacion')
        habitacion = Habitacion.objects.get(pk=habitacion_id)

        version_usuario = request.data.get('version')
        if version_usuario is None or int(version_usuario) != habitacion.version:
            return JsonResponse({'error': 'La habitación ha sido reservada por otro usuario.'}, status=400)

        return super().update(request, *args, **kwargs)

