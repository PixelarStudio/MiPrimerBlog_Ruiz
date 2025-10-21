from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>/", views.post_detalle, name="post_detalle"),
    path("autor/new/", views.crear_autor, name="autor_new"),
    path("categoria/new/", views.crear_categoria, name="categoria_new"),
    path("post/new/", views.crear_post, name="post_new"),
    path("buscar/", views.buscar_posts, name="buscar"),
]
