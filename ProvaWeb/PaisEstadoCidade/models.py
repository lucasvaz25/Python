from django.db import models
class Pai(models.Model):
    codigo = models.SmallIntegerField(auto_created=True)
    dataCad = models.DateTimeField(auto_created=True)
    dataUpdate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Paises(Pai):
    pais = models.CharField(max_length=50)
    sigla = models.CharField(max_length=3)
    ddi = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.pais

class Estados(Pai):
    pais = models.ForeignKey(Paises, related_name='estados', on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.estado


class Cidades(Pai):
    estado = models.ForeignKey(Estados, related_name='cidades', on_delete=models.CASCADE)
    cidade = models.CharField(max_length=50)
    ddd = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.cidade