from django.db import models

class Product(models.Model):
    photo = models.ImageField(upload_to="photos/%y/", verbose_name="фото")
    name = models.CharField(max_length=30, verbose_name="товар")
    info = models.TextField(verbose_name="информация")
    price = models.IntegerField(blank=True, verbose_name="цена")

    class Meta:
        verbose_name='Товар'
        verbose_name_plural = 'Товары'

class News(models.Model):
    title = models.CharField(max_length=30, verbose_name="заголовок")
    anons = models.TextField(verbose_name="анонс")
    date=models.DateTimeField(verbose_name="дата")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Feed(models.Model):
    fio = models.CharField(max_length=30, verbose_name="заголовок")
    text = models.TextField(verbose_name="анонс")
    date=models.DateTimeField(verbose_name="дата")

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


EDUCATION_TYPES = (
     ('1', 'Штаны Nike'),
     ('2', 'Кофта СЛОН'),
     ('3', 'Футболка-Ямайка')
)
EDUCATION = (
     ('1', 'S'),
     ('2', 'M'),
     ('3', 'L'),
     ('4', 'XL')
)
class History(models.Model):
    tovar = models.CharField(max_length=30, verbose_name="товар",choices=EDUCATION_TYPES)
    razmer = models.CharField(max_length=30, verbose_name="размер",choices=EDUCATION)
    kol = models.CharField(max_length=30, verbose_name="количество товара")
    email = models.CharField(max_length=30, verbose_name="@mail")
    fio = models.CharField(max_length=30, verbose_name="фио")
    date = models.DateField(verbose_name="дата")
    text = models.TextField(verbose_name="адрес")

    class Meta:
        verbose_name = 'История заказов'
        verbose_name_plural = 'История заказов'

