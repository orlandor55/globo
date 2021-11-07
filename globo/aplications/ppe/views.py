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
    ActivosFijos, 
)
# Create your views here.

#<=====CRUD ActivosFijos======> 

class SuccessAddActivoFijo(TemplateView):
    template_name = "ppe/success-add-activo.html"


class ActivoFijo(CreateView):
    model = ActivosFijos
    template_name = "ppe/add-activo.html"
    fields = [
        'empresa',
        'descripcion', 
        'codigo_cta', 
        'mes_adquisicion', 
        'ano_adquisicion',
        'valor_origen',
        'vida_util',
        'cta_contable_amort_acum',
        'amort_acum',
        'cta_contable_amort_ejercicio',
        'amort_ejercicio',
    ]
    success_url = reverse_lazy('ppe_app:success_add_activo')

class UpdateSuccessActivo(TemplateView):
    template_name = "ppe/update_activo_success.html"

    
class ActivoContableUpdate(UpdateView):
    model = ActivosFijos
    template_name = "ppe/update-activo.html"
    fields = [
        'empresa',
        'descripcion', 
        'codigo_cta', 
        'mes_adquisicion', 
        'ano_adquisicion',
        'valor_origen',
        'vida_util',
        'cta_contable_amort_acum',
        'amort_acum',
        'cta_contable_amort_ejercicio',
        'amort_ejercicio',
    ]
    success_url = reverse_lazy('ppe_app:success_update_activo')


class ActivoDetail(DetailView):
    model = ActivosFijos
    template_name = "ppe/detail-activo.html"


class DeleteSuccessActivo(TemplateView):
    template_name = "ppe/delete_activo_success.html"


class ActivoDelete(DeleteView):
    model = ActivosFijos
    template_name = "ppe/delete-activo.html"
    success_url = reverse_lazy('ppe_app:success_delete_activo')


#<=====END CRUD ActivosFijos======> 