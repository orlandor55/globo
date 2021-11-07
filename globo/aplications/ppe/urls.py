from django.contrib import admin
from django.urls import path

from . import views


app_name = 'ppe_app'


urlpatterns = [
    #ActivosFijos
    path('add-activo/', views.ActivoFijo.as_view(), name='add_activo'),
    path('success-add-activo/', views.SuccessAddActivoFijo.as_view(), name='success_add_activo'),
    path('update-activo/<pk>', views.ActivoContableUpdate.as_view(), name='update_activo'),
    path('success-update-activo/', views.UpdateSuccessActivo.as_view(), name='success_update_activo'),
    path('detail-activo/<pk>', views.ActivoDetail.as_view(), name='detail_activo'),
    path('delete-activo/<pk>', views.ActivoDelete.as_view(), name='delete_activo'),
    path('success-delete-activo/', views.DeleteSuccessActivo.as_view(), name='success_delete_activo'),
    
] 