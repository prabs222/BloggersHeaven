from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField


# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        db_table = "Categories"

    def __str__(self) -> str:
        return self.category


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = FroalaField()
    cover_image = models.ImageField(upload_to="cover_images")
    category = models.ForeignKey(
        Categories, on_delete=models.DO_NOTHING, db_column="category"
    )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Blogs"

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
