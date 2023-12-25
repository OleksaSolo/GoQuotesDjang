from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=120, unique=True)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return f"{self.fullname}"


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]
    def __str__(self) -> str:
        return f"{self.name}"


class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

