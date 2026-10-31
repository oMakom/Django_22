from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="заголовок записи поста", help_text="введите заголовок записи поста"
    )  # заголовок
    content = models.TextField(verbose_name="содержимое поста")  # содержимое
    preview_image = models.ImageField(
        upload_to="myblog/preview",
        blank=True,
        null=True,
        verbose_name="превью поста",
        help_text="Загрузите превью поста",
    )  # превью (изображение)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # дата создания
    is_published = models.BooleanField(default=False, verbose_name="признак публикации")  # признак публикации
    views_count = models.PositiveIntegerField(default=0, verbose_name="количество просмотров")  # количество просмотров

    def __str__(self):
        return f"Пост: {self.title}({self.content[:15]}). Количество просмотров: {self.views_count}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-is_published", "-created_at"]
