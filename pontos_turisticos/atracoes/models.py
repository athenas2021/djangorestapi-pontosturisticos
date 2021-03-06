from django.db import models

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    foto = models.ImageField(upload_to='imgs_atracoes', null=True, blank=True)

    class Meta:
        verbose_name_plural = "atracoes"

    def __str__(self):
        return self.nome