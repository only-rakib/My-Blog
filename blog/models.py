from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


class UvaSolve(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    url_txt = models.URLField(max_length=100)
    description = models.TextField()
    critical_input = models.TextField()
    critical_output = models.TextField()
    code_txt = models.TextField()

    def get_absolute_url(self):
        return reverse(viewname="acm_codes", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = UvaSolve.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    # This method autometic assign title value to the slug by the pre_save class
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, UvaSolve)
