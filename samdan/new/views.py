from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def new_home(request):
    new = Articles.objects.order_by('-date')
    return render(request, 'new/new_home.html', {'new' : new})

class NewDetailView(DetailView):
    model = Articles
    template_name = 'new/details_view.html'
    context_object_name = 'article'

class NewUpdateView(UpdateView):
    model = Articles
    template_name = 'new/create.html'

    form_class = ArticlesForm

class NewDeleteView(DeleteView):
    model = Articles
    success_url = '/new/'
    template_name = 'new/new-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'new/create.html', data)