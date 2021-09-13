from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        # Aqui, sobrescrevemos o metodo get_queryset
        # parametrizando e filtrando
        # Necessidade de passar o basename no arquivo urls.py
        id = self.request.query_params.get('id',None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    # Aqui, define-se uma nova acao: Denunciar ponto turistico
    # Decorator @action permite que receba a um evento (get)
    # o parametro detail=True, exige que o endpoint receba um parametro de ponto turistico
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
        # TODO: mudar verbo para post para que envie uma denuncia