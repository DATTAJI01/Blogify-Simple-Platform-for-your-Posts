from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView, CreateView, UpdateView
from .models import Post
from .forms import *
# Create your views here.
# def home(request):
#     return render(request, 'theblog/home.html',{})
class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'

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