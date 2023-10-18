from django.db import models

class categoria(models.Model):
    descricao = models.CharField(max_length=40)

    def __str__(self):
        return self.descricao
    
class pais(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome
    
class tipoAtucao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class produtora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(pais, on_delete=models.PROTECT)

    def __str__(self):
        return f"({self.nome}) ({self.pais})"
    
class membros(models.Model):
    nome = models.CharField(max_length=100)
    dataNas = models.DateField()
    pais = models.ForeignKey(pais, on_delete=models.PROTECT)

    def __str__(self):
        return f"({self.nome}) ({self.pais})"
    
class filme(models.Model):
    titulo = models.CharField(max_length=40)
    ano = models.IntegerField()
    sinops = models.TextField()
    classificacao = models.IntegerField()
    duracao = models.TimeField()
    produtora = models.ForeignKey(produtora, on_delete=models.PROTECT)
    categorias = models.ManyToManyField(categoria) 

    def __str__(self):
        return f"({self.titulo}) ({self.classificacao})"
    
class atuacao(models.Model):
    filme = models.ForeignKey(filme, on_delete=models.PROTECT)
    membros = models.ForeignKey(membros, on_delete=models.PROTECT)
    tipoAtucao = models.ForeignKey(tipoAtucao, on_delete=models.PROTECT)
    personagens = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.filme} ({self.personagens}) ({self.tipoAtucao})"

