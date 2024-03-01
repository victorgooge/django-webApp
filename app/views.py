from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
# Create your views here.

# Main Home Page
class HomePage(TemplateView):
    template_name = 'app/_index.html'


############################## DASHBOARD #####################################
# User Dashboard
@login_required(login_url='login')
def dashboard(request):
    posts = Post.objects.filter(owner=request.user).order_by('-timestamp')
    context = {
        'posts':posts,
    }
    return render(request, 'app/dashboard.html', context)

# Post Creation
class PostCreatView(CreateView):
    model = Post
    success_url = reverse_lazy('dashboard-home')
    fields = ['image', 'caption']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# Post Deletion
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard-home')
############################################################################
