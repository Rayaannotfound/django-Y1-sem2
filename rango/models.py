from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

slug = models.SlugField(unique=True)


class Category(models.Model):
    CAT_NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=CAT_NAME_MAX_LENGTH, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    PAGE_TITLE_MAX_LENGTH = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=PAGE_TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username