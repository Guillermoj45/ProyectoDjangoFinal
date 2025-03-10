from django.urls import path

from proyectoFinal import views

urlpatterns = [
    path('', views.list_notes, name='home'),
    path('login', views.login, name='login'),
    path('new_note', views.new_note, name='new_note'),
    path('edit_note/<int:id>', views.edite_note, name='edit_note'),
    path('note/<int:id>', views.note, name='note'),
    path('delete_note/<int:id>', views.delete_note, name='delete_note'),
]

