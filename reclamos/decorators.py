from .models import *
def get_consulta_permisos(function):

    def permisos(request):
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
            mayores_25 = Reclamo.objects.filter(categoria__nombre='INGRESO MAYORES DE 25 AÑOS')
            mayores_25_pendientes = Reclamo.objects.filter(categoria__nombre='INGRESO MAYORES DE 25 AÑOS').exclude(
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

        if request.user.has_perm('reclamos.alumno_vocacional'):
            alumno_vocacional = Reclamo.objects.filter(categoria__nombre='ALUMNO VOCACIONAL')
            alumno_vocacional_pendientes = Reclamo.objects.filter(categoria__nombre='ALUMNO VOCACIONAL').exclude(
                estado='CERRADO')
        else:
            alumno_vocacional = Reclamo.objects.filter(categoria__nombre='Ninguno')
            alumno_vocacional_pendientes = Reclamo.objects.filter(categoria__nombre='NINGUNO')

        consultas = trabajo_final_pendientes | equivalencia_pendientes | certificacion_pendientes | examen_pendientes \
                    | cursada_pendientes | ingreso_pendientes | mayores_25_pendientes | egreso_pendientes | alumno_vocacional_pendientes | cambio_plan_pendientes

        consultas_totales = trabajo_final | equivalencia | certificacion | examen | cursada | ingreso | mayores_25 | egreso | alumno_vocacional | cambio_plan

        return (consultas, consultas_totales)
    return permisos