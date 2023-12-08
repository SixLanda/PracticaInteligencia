from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

class Login(APIView):
    template_name='index.html'
    def get(self,request):
       return render(request,self.template_name)
    
class Home(APIView):
    template_name='indexuno.html'
    def get(self,request):
       return render(request,self.template_name)
    
class Formulario(APIView):

    template_name='formulario.html'     
    def get(self, request):
        return render(request, 'formulario.html')

class APIUsuario(APIView):

    def post(self, request):
        data = request.data
        print(data)
        new_User = User( username= data.get('email'), email = data.get('email'), password = data.get('contrasena'))

        new_User.first_name = data.get("nombre")
        new_User.save()

        try:
                subject = 'Bienvenido. Tu registro ha sido exitoso'
                message = f'Sea usted bienvenido {new_User.first_name}, ¡Su registro se realizo de manera correcta!, tus datos para iniciar sesion son: Username: {new_User.username} Contraseña: {new_User.password}'
                from_email = 'aulavirtual@gmail.com'
                recipient_list = [new_User.email]
                new_User.save() 
        
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'Correo de confirmación enviado correctamente.')          
                # return Response({'message': 'Correo de confirmación enviado correctamente'}, status=status.HTTP_201_CREATED)
                return Response({'msg': 'Usuario registrado'}, status=status.HTTP_201_CREATED)
             
        except Exception as e:
            messages.error(request, 'Error al enviar el correo de confirmación.')
            return Response({'error': 'Error al enviar el correo de confirmación'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class Preguntas(APIView):
    template_name='preguntas.html'
    def get(self,request):
       return render(request,self.template_name)
        
class Tareas(APIView):
    template_name='registro_tareas.html'
    def get(self,request):
        return render(request,self.template_name)