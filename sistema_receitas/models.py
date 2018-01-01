from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

ESTADO_CHOICE = (('T', 'Tratada'), ('ET', 'Em tratamento'), ('R', 'Receitada'))
ESTADO_CHOICE_AUTORIZACAO = (('A', 'Autorizado'), ('NA', 'Nao autorizado'))
GENERICO = (('S', 'Sim'), ('N', 'Nao'))


class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True, null=False, unique=True)
    nome_generico = models.CharField(max_length=50)
    nome_medicamento = models.CharField(max_length=100)
    forma_farmaceutica = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=100)
    estado_autorizacao = models.CharField(max_length=2, choices=ESTADO_CHOICE_AUTORIZACAO)
    generico = models.CharField(max_length=1, choices=GENERICO)
    titular_AM = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.nome_generico


ESPECIALIDADES = (('ORT', 'Ortopedia'), ('CGE', 'Clinica Geral'), ('OFT', 'Oftalmologia'),
                  ('GNC', 'Ginecologia'))


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=3, choices=ESPECIALIDADES)
    cedula = models.CharField(max_length=6, primary_key=True, null=False, unique=True)

    def __str__(self):
        return self.cedula


class Utente(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=100)
    cc = models.CharField(max_length=8, primary_key=True, null=False, unique=True)
    tel = models.CharField(max_length=9)

    def __str__(self):
        return self.cc

class Receita(models.Model):
    id_receita = models.AutoField(max_length=6, primary_key=True, null=False, unique=True)
    id_utente = models.ForeignKey(Utente, null=True, on_delete=models.CASCADE)
    id_medico = models.ForeignKey(Medico, null=True, on_delete=models.CASCADE)
    data_da_receita = models.DateField(default=timezone.now)
    validade = models.DateField(blank=False, null=False)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICE)
    medicamento1 = models.ForeignKey(Medicamento, related_name="medA", null="False")
    quant1 = models.IntegerField(default=1)
    desc1 = models.CharField(max_length=100,blank="True")
    medicamento2 = models.ForeignKey(Medicamento, related_name="medB",blank="True")
    quant2 = models.IntegerField(default="0",blank="True")
    desc2 = models.CharField(max_length=100,blank="True")
    medicamento3 = models.ForeignKey(Medicamento, related_name="medC",blank="True")
    quant3 = models.IntegerField(default="0",blank="True")
    desc3 = models.CharField(max_length=100,blank="True")
    medicamento4 = models.ForeignKey(Medicamento, related_name="medD",blank="True")
    quant4 = models.IntegerField(default="0",blank="True")
    desc4 = models.CharField(max_length=100,blank="True")
    medicamento5 = models.ForeignKey(Medicamento, related_name="medE",blank="True")
    quant5 = models.IntegerField(default="0",blank="True")
    desc5 = models.CharField(max_length=100,blank="True")

    def __str__(self):
        return str(self.id_receita)