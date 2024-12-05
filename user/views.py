# views.py
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from pathlib import Path
from .models import User, Plan, Contract, Payment, Lecture, Teacher
from .serializers import UserSerializer, PlanSerializer, ContractSerializer, PaymentSerializer, LectureSerializer, TeacherSerializer


from .models import loaded_model

MODEL_PATH = Path('decision_tree_model.pkl')


categorical_features = ['day_of_class', 'time_of_class', 'category']
numerical_features = ['months_as_member', 'weight', 'days_before_class']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()  # Obtém todos os usuários
        user_id = self.kwargs.get('id')  # Pega o id passado na URL

        if user_id:
            queryset = queryset.filter(id=user_id)  # Filtra para um único usuário
        
        return queryset

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

@api_view(['POST'])
def login_view(request):
    cpf = request.data.get('cpf')
    password = request.data.get('password')

    try:
        user = User.objects.get(cpf = cpf)

        if(user.password == password):
            user_serializer = UserSerializer(user)
            
            return Response({
                "user":user_serializer.data
            },status=status.HTTP_200_OK)
        else:
            return Response({"error":"Credenciais inválidas"},status = status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['POST'])
def predict(request):
    if loaded_model is None:
        return JsonResponse({'error': 'Modelo não carregado.'}, status=500)

    try:
        # Valida se as features estão presentes nos dados de entrada
        data = request.data
        if 'feature1' not in data or 'feature2' not in data:
            return JsonResponse({'error': 'Faltando dados de entrada.'}, status=400)

        # Realiza o pré-processamento dos dados
        input_data = [float(data['feature1']), float(data['feature2'])]  # Ajuste conforme necessário

        # Faz a previsão
        prediction = loaded_model.predict([input_data])[0]  # [0] para obter o valor da previsão

        return JsonResponse({'prediction': prediction})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)