from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "email", "bio"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "estado", "autor", "categoria"]

class SearchForm(forms.Form):
    q = forms.CharField(label="Buscar posts por título", max_length=140, required=True)
