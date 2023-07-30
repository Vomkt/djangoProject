from django.shortcuts import render
from .models import Task, Note, About
from .forms import ContactForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def about(request):
    self = About.objects.all()
    return render(request, 'about.html', {'self': self})


def blog(request):
    notes = Note.objects.all()
    return render(request, 'blog.html', {'notes': notes})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contacts.html', context)
