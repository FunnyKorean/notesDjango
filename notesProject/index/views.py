from django.shortcuts import render, redirect
from . import forms, models
from django.views.generic import DetailView, UpdateView, DeleteView
import datetime


class NoteDetailView(DetailView):
    model = models.Note
    template_name = 'detail_view.html'
    context_object_name = 'note'


class NoteUpdateView(UpdateView):
    model = models.Note
    template_name = 'new_note.html'
    fields = ['title', 'text', 'date', 'due_date']


class NoteDeleteView(DeleteView):
    model = models.Note
    template_name = 'note_delete.html'
    success_url = '/'


def home_page(request):
    return render(request, 'index.html')


def see_completed(request):
    print(request.user.id)
    context = models.Note.objects.filter(user_id=request.user.id, status='complete')
    return render(request, 'see_completed_notes.html', {'notes': context})


def see_active(request):
    print(request.user.id)
    context = models.Note.objects.filter(user_id=request.user.id, status='active')
    return render(request, 'see_active_notes.html', {'notes': context})


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.RegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def complete(request, pk):
    note = models.Note.objects.get(id=pk)
    note.status = 'complete'
    note.save()
    return redirect('/')


def new_note(request):
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            models.Note.objects.create(
                title=request.POST.get('title'),
                text=request.POST.get('text'),
                date=datetime.datetime.now(),
                due_date=request.POST.get('due_date'),
                user_id=request.user.id,
                status='active'
            ).save()
            return redirect('/')
    else:
        form = forms.NoteForm()
    context = {'form': form}
    return render(request, 'new_note.html', context)

