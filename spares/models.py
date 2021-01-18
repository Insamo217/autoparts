from django.db import models


class Category(models.Model):
    category_name = models.CharField('Категория', max_length=150, db_index=True,
                                     unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Spares(models.Model):
    spares_name = models.CharField('Название запчасти', max_length=150, db_index=True)
    number = models.CharField('Оригинальный номер', max_length=150, unique=True)
    manufacturer = models.CharField('Производитель', max_length=150, db_index=True)
    stock = models.IntegerField('Остаток', db_index=True)
    price = models.FloatField('Цена', blank=True, db_index=True)
    category_name = models.ForeignKey\
        (Category, to_field='category_name', verbose_name='Категория', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.spares_name

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти'


class Brand(models.Model):
    name = models.CharField('Бренд', max_length=150, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
