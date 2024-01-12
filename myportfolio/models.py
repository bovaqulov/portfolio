import telnetlib

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=100, verbose_name='loyha nomi')
    price = models.CharField(max_length=100, verbose_name='loyha narxi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    description = models.TextField(verbose_name='loyha haqida')
    link = models.URLField(blank=True, null=True, verbose_name="loyha urli")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.all()[0].images.url
            except:
                return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5igFUHiY5DMEZEKlymdVHp4r3MA9Pj7mEI6uKW_iT6A&s'
        return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5igFUHiY5DMEZEKlymdVHp4r3MA9Pj7mEI6uKW_iT6A&s'

    class Meta:
        verbose_name = "loyha"
        verbose_name_plural = "loyhalar"


class Gallery(models.Model):
    images = models.ImageField(upload_to='images/', verbose_name='loyha rasmi')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='images')


    class Meta:
        verbose_name = 'loyha rasmi'
        verbose_name_plural = 'loyha rasmlari'



class UsersALL(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

