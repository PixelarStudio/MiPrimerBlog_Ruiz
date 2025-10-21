from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, SearchForm

def index(request):
    posts = Post.objects.select_related("autor", "categoria").filter(estado="publicado").order_by("-publicado_at")
    return render(request, "blog/index.html", {"posts": posts})

def post_detalle(request, pk: int):
    p = get_object_or_404(Post.objects.select_related("autor", "categoria"), pk=pk)
    return render(request, "blog/post_detalle.html", {"post": p})

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "blog/autor_form.html", {"form": form})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "blog/categoria_form.html", {"form": form})

def crear_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "blog/post_form.html", {"form": form})

def buscar_posts(request):
    form = SearchForm(request.GET or None)
    resultados, query = [], ""
    if form.is_valid():
        query = form.cleaned_data["q"]
        resultados = (
            Post.objects
            .filter(Q(titulo__icontains=query))
            .select_related("autor", "categoria")
            .order_by("-publicado_at")
        )
    return render(request, "blog/search.html", {"form": form, "resultados": resultados, "query": query})
