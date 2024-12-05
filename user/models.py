from django.db import models
import uuid
import joblib
from pathlib import Path
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import logging
logger = logging.getLogger(__name__)
# Caminho para o modelo .pkl
MODEL_PATH = Path('decision_tree_model.pkl')



loaded_model = None
class Teacher(models.Model):
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    nome = models.CharField(max_length=200, null=False)

class Plan(models.Model):
    plan_types = [
        ("Basic", "Basic"),
        ("Plus", "Plus")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(choices=plan_types, max_length=10)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    signDate = models.DateField(auto_now_add=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True)  # Associe um contrato a um aluno

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField("dd/mm/yyyy", default="0000-00-00")
    months_as_member = models.PositiveIntegerField(default=0)  # Meses como membro
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)  # Peso em kg
    days_before = models.PositiveIntegerField(default=0)  # Dias antes da aula
    day_of_week = models.CharField(max_length=10, null=True)  # Dia da semana (por exemplo: 'Monday')
    time = models.TimeField(null=True)  # Horário da aula
    attended = models.BooleanField(default=False)  # Se o aluno compareceu ou não
    password = models.CharField(max_length=20,default='abcd1234')
    is_adm = models.BooleanField(default=False)
class Payment(models.Model):
    payment_methods = [
        ("PIX", "PIX"),
        ("DEBIT", "DEBIT"),
        ("CREDIT", "CREDIT")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True)
    method = models.CharField(choices=payment_methods, max_length=40)
    plans = models.ManyToManyField(Plan)  # Relação M:N com Planos

class Lecture(models.Model):
    lecture_types = [
        ("CrossFit", "CrossFit"),
        ("Musculação", "Musculação"),
        ("Gap", "Gap"),
        ("Fisioterapia", "Fisioterapia"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField(null=True)
    finish_time = models.DateTimeField(null=True)
    type = models.CharField(choices=lecture_types, max_length=40)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(User)  # Relação M:N com Alunos



@receiver(post_migrate)
def load_model(sender, **kwargs):
    global loaded_model
    try:
        logger.debug(f"Tentando carregar o modelo do caminho: {MODEL_PATH}")  # Verifique o caminho
        loaded_model = joblib.load(MODEL_PATH)
        logger.info("Modelo carregado com sucesso.")
    except FileNotFoundError:
        logger.error(f"Erro: Modelo não encontrado. Verifique o caminho: {MODEL_PATH}")
    except Exception as e:
        logger.error(f"Erro ao carregar o modelo: {e}")
