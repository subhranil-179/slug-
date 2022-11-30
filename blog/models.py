from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(
        null=False,
        blank=False,
        max_length=50,
    )

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        slug = slugify(str(self.title)[:50])
        count = self.__class__.objects.filter(
            author=self.author,
            slug__startswith=slug
        ).count()
        self.slug = slug
        if count > 0:
            self.slug = slug + str(count)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)[:50]
