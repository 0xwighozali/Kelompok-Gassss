from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bendungans.index'),
    path('add', views.add, name='bendungans.add'),
    path('save', views.save, name='bendungans.save'),
    path('delete/<int:bendungan_id>', views.delete, name='bendungans.delete'),
    path('edit/<int:bendungan_id>', views.edit, name='bendungans.edit'),
    path('update/<int:bendungan_id>', views.update, name='bendungans.update'),
    path('export_data', views.export_data, name='bendungans.export_data'), 
]