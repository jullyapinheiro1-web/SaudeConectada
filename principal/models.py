from django.db import models


class Vacina(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    lote = models.CharField(max_length=50)
    tipo_dose = models.CharField(max_length=50)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class LocalVacinacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Local de Vacinação'
        verbose_name_plural = 'Locais de Vacinação'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Campanha(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    vacinas = models.ManyToManyField(Vacina)
    locais = models.ManyToManyField(LocalVacinacao)

    class Meta:
        verbose_name = 'Campanha'
        verbose_name_plural = 'Campanhas'
        ordering = ['nome']

    def __str__(self):
        return self.nome