from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cidedes"

    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField()
    email = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f'{self.nome, self.cpf, self.email}'
    
class Genero(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Genêros"

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Editoras"

    def __str__(self):
        return f'{self.nome} {self.site} {self.Cidade}'
    

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return f'{self.nome} {self.Cidade}'

    
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    datapublicao = models.DateField(max_length=8)
    Genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Livros"

    def __str__(self):
        return f'{self.nome} {self.Genero} {self.Autor} {self.preco} {self.datapublicao}'
    

class emprestimo(models.Model):
    dataemprestimo = models.DateField(max_length=8)
    datadevolucao = models.DateField(max_length=8)
    Livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Emprestimos"

    def __str__(self):
       return f'{self.dataemprestimo} {self.Livro} {self.datadevolucao} {self.Usuario}'
    