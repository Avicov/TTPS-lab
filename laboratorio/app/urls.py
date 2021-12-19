from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('estudios', views.estudios, name='Estudios'),
    path('estudios_paciente', views.estudios_paciente, name='Estudios_Paciente'),
    path('estudios/nuevo', views.nuevo_estudio, name='Crear_Estudio'),
    path('estudios/editar/<id>', views.editar_estudio, name='Editar_Estudio'),
    path('estudios/detalle/<id>', views.detalle_estudio, name='Detalle_Estudio'),
    path('estudios/ver_consentimiento/<id>', views.ver_consentimiento_firmado, name='Consentimiento_Firmado'),
    path('estudios/eliminar_consentimiento/<id>', views.eliminar_consentimiento_firmado, name='Eliminar_Consentimiento_Firmado'),
    path('estudios/ver_comprobante/<id>', views.ver_comprobante_pago, name='Comprobante_Pago'),
    path('estudios/eliminar_comprobante/<id>', views.eliminar_comprobante_pago, name='Eliminar_Comprobante_Pago'),
    path('estudios/pendientes', views.pendientes, name='Pendientes'),
    path('estudios/cargar_comprobante/<id>',
         views.cargar_comprobante, name='Cargar_Comprobante'),
    path('estudios/descargar_consentimiento/<id>',
         views.descargar_consentimiento, name='Descargar_Consentimiento'),
    path('estudios/cargar_consentimiento/<id>', views.cargar_consentimiento, name='Cargar_Consentimiento'),
    path('estudios/turno/<id>', views.seleccionar_turno, name='Seleccionar_Turno'),
    path('estudios/turno/buscar/<id>', views.buscar_turno_por_fecha, name='Buscar_Turno'),
    path('estudios/cargar_muestra/<id>', views.cargar_muestra, name='Cargar_Muestra'),
    path('estudios/retiro_muestra/<id>', views.retiro_muestra, name='Retiro_Muestra'),
    path('estudios/lista_lotes', views.lotes, name='Lotes'),
    path('estudios/finalizar_proceso/<id>', views.finalizar_proceso, name='Finalizar_Proceso'),
    path('estudios/lote/<id>/lista_muestras', views.listar_muestras, name='Listar_Muestras'),
    path('estudios/lote/<id>/ver_muestras', views.ver_muestras, name='Ver_Muestras'),
    path('estudios/cargar_interpretacion/<id>', views.cargar_interpretacion, name='Cargar_Interpretacion'),
    path('estudios/descargar_estudio/<id>', views.descargar_estudio, name='Descargar_Estudio'),
    path('estudios/resultado_entregado/<id>', views.resultado_entregado, name='Resultado_Entregado'),
    path('pagar', views.pagar_estudios, name="Pagar"),
    path('estudios/<lote_id>/marcar_falla/<muestra_id>', views.marcar_falla, name="Marcar_Falla"),
    path('pacientes', views.pacientes, name='Pacientes'),
    path('pacientes/nuevo', views.nuevo_paciente, name='Registrar Paciente'),
    path('pacientes/eliminar/<id>', views.eliminar_paciente),
    path('pacientes/editar/<id>', views.editar_paciente, name="Editar_Paciente"),
    path('pacientes/ver_perfil/<id>', views.ver_perfil, name="Ver_Perfil"),
    path('pacientes/estudio/<id>/cargar_comprobante', views.cargar_comprobante_paciente, name="Cargar_Comprobante_Paciente"),
    path('pacientes/estudio/<id>/cargar_consentimiento', views.cargar_consentimiento_paciente, name="Cargar_Consentimiento_Paciente"),
    path('pacientes/estudio/<id>/turno', views.seleccionar_turno_paciente, name='Seleccionar_Turno_Paciente'),
    path('pacientes/estudio/<id>/buscar', views.buscar_turno_por_fecha_paciente, name='Buscar_Turno_Paciente'),
    path('pacientes/<id>/turnos', views.ver_turnos, name="Ver_Turnos"),
    path('historial', views.historial, name='Historial'),
    path('historial/nuevo/<id>', views.nuevo_historial, name="Agregar Historial"),
    path('historial/paciente/<id>', views.historial_paciente),
    path('empleados', views.empleados, name='Empleados'),
    path('pendientes', views.pendientes, name='Pendientes'),
    path('login', views.login_paciente, name='Login_Paciente'),
    path('empleado/login', views.login, name='Login Empleado'),
    path('logout', views.logout, name='Logout'),
    path('graficos', views.graficos, name="Graficos"),
    path('graficos/cantidadPorTipo', views.cantXTipo, name="Graficos_Tipo"),
    path('graficos/cantidadPorMes', views.cantXMes, name="Graficos_Mes"),
    path('graficos/tiempoDeDemora', views.boxplot, name="Graficos_Boxplot")
]
