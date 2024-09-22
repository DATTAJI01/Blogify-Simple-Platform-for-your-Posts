from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views import generic 
from .models import Post
from .forms import *
# Create your views here.
# def home(request):
#     return render(request, 'theblog/home.html',{})
class HomeView(generic.ListView):
    model = Post
    template_name = 'theblog/home.html'
    ordering = ['-publication_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = Postform
    template_name = 'theblog/add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = Editform
    template_name = 'theblog/update_post.html'
    #fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')
    