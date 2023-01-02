from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from .decorators import get_consulta_permisos


# DASHBOARD ADMINISTRADOR>>>>>>
@login_required(login_url='consulta_create')
def dashboard(request):
    if request.user.has_perm('reclamos.admin'):
        reclamosTotales = Reclamo.objects.all()
        reclamos = Reclamo.objects.all().order_by('-fecha_creada').exclude(estado='CERRADO')
        respuestas = Respuesta.objects.all()
        categorias = Categoria.objects.all()
        total_reclamos = reclamosTotales.count()
        reclamos_resueltos = reclamosTotales.filter(estado='CERRADO').count()
        reclamos_pendientes = reclamos.filter(estado='PENDIENTE').count() + reclamos.filter(estado='EN PROCESO').count()
        ultimosCinco = reclamos[:5]

        # cantidad por categoria
        catExamen = reclamosTotales.filter(categoria__nombre='EXAMEN').count()
        catIngreso = reclamosTotales.filter(categoria__nombre='INGRESO').count()
        catCursada = reclamosTotales.filter(categoria__nombre='CURSADA').count()
        catMayores = reclamosTotales.filter(categoria__nombre='INGRESO MAYORES DE 25 AÑOS').count()
        catEquivalencia = reclamosTotales.filter(categoria__nombre='EQUIVALENCIA').count()
        catCertificacion = reclamosTotales.filter(categoria__nombre='CERTIFICACION DE PROGRAMAS y PLANES').count()
        catEgreso = reclamosTotales.filter(categoria__nombre='EGRESO').count()
        catTFinal = reclamosTotales.filter(categoria__nombre='TRABAJO FINAL').count()

        context = {'reclamos': reclamos, 'respuestas': respuestas, 'categorias': categorias,
                   'total_reclamos': total_reclamos,
                   'resueltos': reclamos_resueltos, 'pendientes': reclamos_pendientes,
                   'ultimos': ultimosCinco, 'cursada': catCursada, 'ingreso': catIngreso,
                   'examen': catExamen, 'mayores25': catMayores, 'equivalencia': catEquivalencia,
                   'certificacion': catCertificacion, 'egreso': catEgreso, 'trabajo_final': catTFinal,

                   }

        return render(request, 'dashboard.html', context)



# PANEL DE USUARIO>>>>>
@login_required(login_url='consulta_create')
def userPanel(request):
    if request.user.has_perm('empleado'):
        # Permisos
        if request.user.has_perm('reclamos.ver_trabajo_final'):
            trabajo_final = Reclamo.objects.filter(categoria__nombre='TRABAJO FINAL')
            trabajo_final_pendientes = Reclamo.objects.filter(categoria__nombre='TRABAJO FINAL').exclude(
                estado='CERRADO')
        else:
            trabajo_final_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')
            trabajo_final = Reclamo.objects.filter(categoria__nombre='NINGUNO')

        if request.user.has_perm('reclamos.ver_equivalencia'):
            equivalencia = Reclamo.objects.filter(categoria__nombre='EQUIVALENCIA')
            equivalencia_pendientes = Reclamo.objects.filter(categoria__nombre='EQUIVALENCIA').exclude(estado='CERRADO')
        else:
            equivalencia_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')
            equivalencia = Reclamo.objects.filter(categoria__nombre='NINGUNO')

        if request.user.has_perm('reclamos.ver_programas_planes'):
            certificacion = Reclamo.objects.filter(categoria__nombre='CERTIFICACION DE PROGRAMAS Y PLANES')
            certificacion_pendientes = Reclamo.objects.filter(
                categoria__nombre='CERTIFICACION DE PROGRAMAS Y PLANES').exclude(estado='CERRADO')
        else:
            certificacion_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')
            certificacion = Reclamo.objects.filter(categoria__nombre='NINGUNO')

        if request.user.has_perm('reclamos.ver_examen'):
            examen = Reclamo.objects.filter(categoria__nombre='EXAMEN')
            examen_pendientes = Reclamo.objects.filter(categoria__nombre='EXAMEN').exclude(estado='CERRADO')
        else:
            examen_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')
            examen = Reclamo.objects.filter(categoria__nombre='NINGUNO')

        if request.user.has_perm('reclamos.ver_cursada'):
            cursada = Reclamo.objects.filter(categoria__nombre='CURSADA')
            cursada_pendientes = Reclamo.objects.filter(categoria__nombre='CURSADA').exclude(estado='CERRADO')
        else:
            cursada_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')
            cursada = Reclamo.objects.filter(categoria__nombre='NINGUNO')

        if request.user.has_perm('reclamos.ver_ingreso'):
            ingreso = Reclamo.objects.filter(categoria__nombre='INGRESO')
            ingreso_pendientes = Reclamo.objects.filter(categoria__nombre='INGRESO').exclude(estado='CERRADO')
        else:
            ingreso_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')
            ingreso = Reclamo.objects.filter(categoria__nombre='Ninguno')

        if request.user.has_perm('reclamos.ver_mayores_25'):
            mayores_25 = Reclamo.objects.filter(categoria__nombre='INGRESO MAYORES 25')
            mayores_25_pendientes = Reclamo.objects.filter(categoria__nombre='INGRESO MAYORES 25').exclude(
                estado='CERRADO')
        else:
            mayores_25_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')
            mayores_25 = Reclamo.objects.filter(categoria__nombre='Ninguno')

        if request.user.has_perm('reclamos.ver_egreso'):
            egreso = Reclamo.objects.filter(categoria__nombre='EGRESO')
            egreso_pendientes = Reclamo.objects.filter(categoria__nombre='EGRESO').exclude(estado='CERRADO')
        else:
            egreso = Reclamo.objects.filter(categoria__nombre='Ninguno')
            egreso_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')

        if request.user.has_perm('reclamos.ver_cambio_plan'):
            cambio_plan = Reclamo.objects.filter(categoria__nombre='CAMBIO DE PLAN')
            cambio_plan_pendientes = Reclamo.objects.filter(categoria__nombre='CAMBIO DE PLAN').exclude(
                estado='CERRADO')
        else:
            cambio_plan = Reclamo.objects.filter(categoria__nombre='Ninguno')
            cambio_plan_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')

        if request.user.has_perm('reclamos.ver_alumno_vocacional'):
            alumno_vocacional = Reclamo.objects.filter(categoria__nombre='ALUMNO VOCACIONAL')
            alumno_vocacional_pendientes = Reclamo.objects.filter(categoria__nombre='ALUMNO VOCACIONAL').exclude(
                estado='CERRADO')
        else:
            alumno_vocacional = Reclamo.objects.filter(categoria__nombre='Ninguno')
            alumno_vocacional_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')

        consultas = trabajo_final_pendientes | equivalencia_pendientes | certificacion_pendientes | examen_pendientes \
                    | cursada_pendientes | ingreso_pendientes | mayores_25_pendientes | egreso_pendientes | alumno_vocacional_pendientes | cambio_plan_pendientes

        consultas_totales = trabajo_final | equivalencia | certificacion | examen | cursada | ingreso | mayores_25 | egreso | alumno_vocacional | cambio_plan

        total_reclamos = consultas_totales.count()
        reclamos_resueltos = consultas_totales.filter(estado='CERRADO').count()
        reclamos_pendientes = consultas_totales.filter(estado='PENDIENTE').count() + consultas.filter(
            estado='EN PROCESO').count()

        context = {'consultas': consultas, 'total_reclamos': total_reclamos,
                   'resueltos': reclamos_resueltos, 'pendientes': reclamos_pendientes, }

        return render(request, 'user_panel.html', context)


# VISTAS Y DETALLES>>>>>
# DETALLE DEL TICKET
def consulta_detalle(request, pk):
    consulta = Reclamo.objects.get(id=pk)
    respuestas = consulta.respuesta_set.all()

    context = {'detalle': consulta, 'resp': respuestas}

    return render(request, 'reclamos/consulta_detalle.html', context)


# Consulta del TICKET
class ConsultaEstado(ListView):
    model = Reclamo
    context_object_name = 'consulta'
    template_name = 'reclamos/consulta_estado.html'

    def get_queryset(self):
        query = self.request.GET.get('t')
        query2 = self.request.GET.get('e')
        resultado = Reclamo.objects.filter(Q(tiket__exact=query) & Q(email__exact=query2))

        return resultado


# BARRA DE BUSQUEDA

class ConsultaPorDni(LoginRequiredMixin, ListView):
    model = Reclamo
    context_object_name = 'consulta'
    template_name = 'reclamos/consulta_estado.html'
    login_url = 'consulta_create'

    def get_queryset(self):
        query = self.request.GET.get('d')
        resultado = Reclamo.objects.filter(Q(dni__exact=query))

        return resultado


def succes(request):
    return HttpResponse('Enviado')


# VIstas de formularios>>>>>>>>>>>>

def consultaCreate(request):
    form = ConsultaForm()
    consultas = Reclamo.objects.all()

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()

            # send Mail
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            subject = form.cleaned_data['categoria']
            email = form.cleaned_data['email']
            tiket = form.instance.tiket

            mensaje = loader.render_to_string(
                'mails/consulta.html',
                {
                    'nombre': nombre,
                    'apellido': apellido,
                    'ticket': tiket
                }
            )
           # try:
              #  send_mail(subject, mensaje, 'admin@email.com', [email], html_message=mensaje)
           # except BadHeaderError:
             #   return HttpResponse('Invalid header found.')
            return redirect('consulta_enviada')

    context = {'form': form, 'consultas': consultas}
    return render(request, 'reclamos/consulta_form.html', context)


class ConsultaEnviada(TemplateView):
    template_name = 'reclamos/success.html'


class ConsultaTicket(TemplateView):
    template_name = 'reclamos/consulta_ticket.html'


def respuestaCreate(request, pk):
    consulta = Reclamo.objects.get(id=pk)
    form = RespuestaForm(initial={'reclamo': consulta})

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        if form.is_valid():
            consulta.estado = "EN PROCESO"
            consulta.save()
            form.instance.reclamo = consulta
            form.instance.user = user
            form.save()

            # send Mail
            if request.user.is_authenticated:
                firma = request.user.get_full_name
            else:
                firma = ''
            subject = consulta.categoria
            nombre = consulta.nombre
            apellido = consulta.apellido
            email = consulta.email
            tiket = consulta.tiket
            respuesta = form.cleaned_data['respuesta']

            mensaje = loader.render_to_string(
                'mails/respuesta.html',
                {
                    'ticket': tiket,
                    'nombre': nombre,
                    'apellido': apellido,
                    'respuesta': respuesta,
                    'firma': firma
                }
            )

            try:
                send_mail(subject, mensaje, 'admin@email.com', [email], html_message=mensaje)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('consulta_detalle', pk)

    context = {'form': form, 'consulta': consulta}
    return render(request, 'reclamos/respuesta_form.html', context)


@login_required(login_url='consulta_create')
def iniciarConsulta(request, pk):
    consulta = Reclamo.objects.filter(id=pk).first()
    contexto = {}

    if not consulta:
        return redirect('home')

    if request.method == 'GET':
        contexto = {'obj': consulta}
        return render(request, 'reclamos/consulta_iniciar.html', contexto)

    if request.method == 'POST':
        consulta.estado = "EN PROCESO"
        consulta.save()

        return redirect('home')

    return render(request, 'reclamos/consulta_iniciar.html', contexto)


@login_required(login_url='consulta_create')
def cerrarConsulta(request, pk):
    consulta = Reclamo.objects.filter(id=pk).first()
    contexto = {}

    if not consulta:
        return redirect('home')

    if request.method == 'GET':
        contexto = {'obj': consulta}
        return render(request, 'reclamos/consulta_cerrar.html', contexto)

    if request.method == 'POST':
        consulta.estado = "CERRADO"
        consulta.save()

        subject = consulta.categoria
        nombre = consulta.nombre
        apellido = consulta.apellido
        email = consulta.email
        tiket = consulta.tiket

        mensaje = loader.render_to_string(
            'mails/cerrado.html',
            {
                'ticket': tiket,
                'nombre': nombre,
                'apellido': apellido,
            }
        )
        try:
            send_mail(subject, mensaje, 'admin@email.com', [email], html_message=mensaje)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return redirect('home')

    return render(request, 'reclamos/consulta_cerrar.html', contexto)


# CAtegorias>>>>>>
@login_required(login_url='consulta_create')
def categoriaList(request, pk):
    reclamos = Reclamo.objects.filter(categoria_id=pk)
    categoria = Categoria.objects.get(id=pk)

    contexto = {'reclamo': reclamos, 'categoria': categoria}

    return render(request, 'categorias/categoria_list.html', contexto)


class CategoriaListar(LoginRequiredMixin, ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'categorias/categoria_listar.html'
    login_url = 'consulta_create'


class AccessDenied(TemplateView):
    template_name = 'reclamos/denegado.html'


# Usuarios>>>>>>>

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

    context = {}

    return render(request, 'accounts/login.html', context)


def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
