from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

from proyectoFinal.forms import NoteForm
from proyectoFinal.models import Note


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # lógica de inicio de sesión
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/login.html', {'form': form})


    form = AuthenticationForm(request, data=request.POST)
    return render(request, 'auth/login.html', {'form': form})


def new_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/note_edit.html', {'form': form})

def edite_note(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {'form': form})

def list_notes(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note(request, id):
    _note = Note.objects.get(id=id)
    return render(request, 'notes/note.html', {'note': _note})

def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('home')


