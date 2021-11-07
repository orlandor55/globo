from django.contrib import admin
from django.urls import path

from . import views


app_name = 'plandectas_app'


urlpatterns = [
    #CtasContable
    path('add-ctas/', views.CtaContable.as_view(), name='add_ctas'),
    path('success-add-ctas/', views.SuccessAddCtas.as_view(), name='success_add_ctas'),
    path('update-ctas/<pk>', views.CtaContableUpdate.as_view(), name='update_ctas'),
    path('success-update-ctas/', views.UpdateSuccessCtas.as_view(), name='success_update_ctas'),
    path('detail-ctas/<pk>', views.CtaContableDetail.as_view(), name='detail_ctas'),
    path('delete-ctas/<pk>', views.CtaContableDelete.as_view(), name='delete_ctas'),
    path('success-delete-ctas/', views.DeleteSuccessCtas.as_view(), name='success_delete_ctas'),

    #SumasySaldos
    path('add-sumas/', views.SumasView.as_view(), name='add_sumas'),
    path('success-add-sumas/', views.SuccessAddSumas.as_view(), name='success_add_sumas'),
    path('update-sumas/<pk>', views.SumasUpdate.as_view(), name='update_sumas'),
    path('success-update-sumas/', views.UpdateSuccessSumas.as_view(), name='success_update_sumas'),
    path('detail-sumas/<pk>', views.SumasDetail.as_view(), name='detail_sumas'),
    path('delete-sumas/<pk>', views.SumasContableDelete.as_view(), name='delete_sumas'),
    path('success-delete-sumas/', views.DeleteSuccessSumas.as_view(), name='success_delete_sumas'),

    #EmpresasClientes
    path('add-empresa/', views.EmpresasAdd.as_view(), name='add_empresa'),
    path('success-add-empresa/', views.SuccessAddEmpresas.as_view(), name='success_add_empresa'),
    path('update-empresa/<pk>', views.EmpresaUpdate.as_view(), name='update_empresa'),
    path('success-update-empresa/', views.UpdateSuccessEmpresa.as_view(), name='success_update_empresa'),
    path('detail-empresa/<pk>', views.EmpresaDetail.as_view(), name='detail_empresa'),
    path('delete-empresa/<pk>', views.EmpresaDelete.as_view(), name='delete_empresa'),
    path('success-delete-empresa/', views.DeleteSuccessEmpresa.as_view(), name='success_delete_empresa'),


]
 