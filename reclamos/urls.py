from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns =[
    #Usuarios
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/login.html'), name='logout'),

    #ADMIN PANEL
    path('dashboard', dashboard, name='home'),
    #USERPANEL
    path('userpanel/', userPanel, name='user_pnale'),

    #conusltas
    path('', consultaCreate, name='consulta_create'),
    path('consulta/<uuid:pk>/', consulta_detalle, name='consulta_detalle'),
    path('consulta/iniciar/<uuid:pk>/', iniciarConsulta, name='consulta_iniciar'),
    path('consulta/cerrar/<uuid:pk>/', cerrarConsulta, name='consulta_cerrar'),
    path('consulta/enviada/', ConsultaEnviada.as_view(), name='consulta_enviada'),


    #respuestas
    path('respuesta/create/<uuid:pk>', respuestaCreate, name='respuesta_create'),
    path('respuesta/create/denied', AccessDenied.as_view(), name='acceso_denegado'),


    #categorias
    path('categorias/<uuid:pk>', categoriaList, name='categoria_list'),
    path('categorias/',CategoriaListar.as_view(), name='categoria_listar'),


    #Resultados de busquedas
    path('consulta/estado/', ConsultaEstado.as_view(), name='consulta_estado'),
    path('consulta/estado/ticket', ConsultaTicket.as_view(), name='consulta_ticket'),
    path('consulta/estadopordni/', ConsultaPorDni.as_view(), name='consulta_dni'),


]