from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_post, name='create'),
    path('<int:pk>/', views.Article.as_view(), name='article'),
    path('<int:pk>/edit', views.edit_post, name='edit'),
]
