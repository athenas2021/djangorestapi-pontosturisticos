from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        # Aqui, define-se que apenas pontos turiscos aprovados serao retornados
        # pelo esta viewset
        # Necessidade de passar o basename no arquivo urls.py
        return PontoTuristico.objects.filter(aprovado=True)