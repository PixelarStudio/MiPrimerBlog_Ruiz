from django.db import models

ESTADOS_POST = [
    ("borrador", "Borrador"),
    ("publicado", "Publicado"),
]

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.email})"

class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=140)
    contenido = models.TextField()
    estado = models.CharField(max_length=10, choices=ESTADOS_POST, default="publicado")
    publicado_at = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="posts")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")

    def __str__(self) -> str:
        return self.titulo

