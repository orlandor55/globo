from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from .models import (
    CtasContable, 
    SumasYSaldos,
    EmpresasClientes,
)
# Create your views here.

#<=====CRUD CtasContable======> 
class SuccessAddCtas(TemplateView):
    template_name = "plandectas/ctascontable/success-add-ctas.html"


class CtaContable(CreateView):
    model = CtasContable
    template_name = "plandectas/ctascontable/add-ctas.html"
    fields = fields = [ 
        'nombre_cliente',
        'codigo', 
        'descripcion', 
        'grupo', 
        'subgrupo',
        'rubro',
        'subrubro',
        'monetario',
    ]
    success_url = reverse_lazy('plandectas_app:success_add_ctas')

class UpdateSuccessCtas(TemplateView):
    template_name = "plandectas/ctascontable/update_ctas_success.html"

    
class CtaContableUpdate(UpdateView):
    model = CtasContable
    template_name = "plandectas/ctascontable/update-ctas.html"
    fields = [ 
        'nombre_cliente',
        'codigo', 
        'descripcion', 
        'grupo', 
        'subgrupo',
        'rubro',
        'subrubro',
        'monetario',
    ]
    success_url = reverse_lazy('plandectas_app:success_update_ctas')


class CtaContableDetail(DetailView):
    model = CtasContable
    template_name = "plandectas/ctascontable/detail-ctas.html"


class DeleteSuccessCtas(TemplateView):
    template_name = "plandectas/ctascontable/delete_ctas_success.html"


class CtaContableDelete(DeleteView):
    model = CtasContable
    template_name = "plandectas/ctascontable/delete-ctas.html"
    success_url = reverse_lazy('plandectas_app:success_delete_ctas')


#<=====END CRUD CtasContable======> 

#<=====CRUD SumasYSaldos======> 

class SuccessAddSumas(TemplateView):
    template_name = "plandectas/sumas/success-add-sumas.html"


class SumasView(CreateView):
    model = SumasYSaldos
    template_name = "plandectas/sumas/add-sumas.html"
    fields = [ 
        'codigo',
        'mes_inicio', 
        'cierre_anterior', 
        'axi_ejercicio_anterior', 
        'mes1',
        'mes2',
        'mes3',
        'mes4',
        'mes5',
        'mes6',
        'mes7',
        'mes8',
        'mes9',
        'mes10',
        'mes11',
        'mes12',
        'mes13',
        'cierre',
    ]
    success_url = reverse_lazy('plandectas_app:success_add_sumas')

class UpdateSuccessSumas(TemplateView):
    template_name = "plandectas/sumas/update_sumas_success.html"

    
class SumasUpdate(UpdateView):
    model = SumasYSaldos
    template_name = "plandectas/sumas/update-sumas.html"
    fields = [
        'mes_inicio', 
        'cierre_anterior', 
        'axi_ejercicio_anterior', 
        'mes1',
        'mes2',
        'mes3',
        'mes4',
        'mes5',
        'mes6',
        'mes7',
        'mes8',
        'mes9',
        'mes10',
        'mes11',
        'mes12',
        'mes13',
        'cierre',
    ]
    success_url = reverse_lazy('plandectas_app:success_update_sumas')


class SumasDetail(DetailView):
    model = SumasYSaldos
    template_name = "plandectas/sumas/detail-sumas.html"


class DeleteSuccessSumas(TemplateView):
    template_name = "plandectas/sumas/delete_sumas_success.html"


class SumasContableDelete(DeleteView):
    model = SumasYSaldos
    template_name = "plandectas/sumas/delete-sumas.html"
    success_url = reverse_lazy('plandectas_app:success_delete_sumas')



#<=====END CRUD SumasYSaldos======> 

#<=====CRUD EmpresasClientes======> 



class SuccessAddEmpresas(TemplateView):
    template_name = "plandectas/empresasclientes/success-add-empresa.html"


class EmpresasAdd(CreateView):
    model = EmpresasClientes
    template_name = "plandectas/empresasclientes/add-empresa.html"
    fields = [ 
        'nombre',
        'cuit',
    ]
    success_url = reverse_lazy('plandectas_app:success_add_empresa')

class UpdateSuccessEmpresa(TemplateView):
    template_name = "plandectas/empresasclientes/update_empresa_success.html"

    
class EmpresaUpdate(UpdateView):
    model = EmpresasClientes
    template_name = "plandectas/empresasclientes/update-empresa.html"
    fields = [
        'nombre',
        'cuit',
    ]
    success_url = reverse_lazy('plandectas_app:success_update_empresa')


class EmpresaDetail(DetailView):
    model = EmpresasClientes
    template_name = "plandectas/empresasclientes/detail-empresa.html"


class DeleteSuccessEmpresa(TemplateView):
    template_name = "plandectas/empresasclientes/delete_empresa_success.html"


class EmpresaDelete(DeleteView):
    model = EmpresasClientes
    template_name = "plandectas/empresasclientes/delete-empresa.html"
    success_url = reverse_lazy('plandectas_app:success_delete_empresa')
