# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u"%s" % (self.name)


class Cartoon(models.Model):
    IMAGE_WIDTH = (
        ('1', '1'),
        ('2', '2'),
        ('4', '4'),
    )

    IMAGE_HEIGHT = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    description = models.TextField(blank=True)
    ordering = models.IntegerField()
    category = models.ForeignKey(Category, related_name="category", blank=True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="cartoons")
    width = models.CharField(max_length=20, choices=IMAGE_WIDTH)
    height = models.CharField(max_length=20, choices=IMAGE_HEIGHT)

    class Meta:
        verbose_name_plural = "Cartoons"

    def __unicode__(self):
        return u"%s %s" % (self.image,  self.category)
