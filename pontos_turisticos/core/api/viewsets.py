from rest_framework.decorators import action
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


    # Aqui, define-se uma nova acao: Denunciar ponto turistico
    # Decorator @action permite que receba a um evento (get)
    # o parametro detail=True, exige que o endpoint receba um parametro de ponto turistico
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
        # TODO: mudar verbo para post para que envie uma denuncia