from django.urls import path
#from . import views
from .views import AddPostView, DeletePostView, HomeView, ArticleDetailView, UpdatePostView



urlpatterns = [
   #path('',views.home,name='home'),
   path('', HomeView.as_view(),name='home'),
   path('article/<int:pk>',ArticleDetailView.as_view(), name='article_details'),
   path('add_post/',AddPostView.as_view(), name='add_post'),
   path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
   path('article/<int:pk>/delete',DeletePostView.as_view(), name='delete_post'),
]