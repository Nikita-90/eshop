from django.db import models
from django.db.models.expressions import F

Categories = (
    (0, 'Auto'),
    (1, 'Bikes'),
    (2, 'Chips'),
)


class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price__gt=1000)

    def set_price(self, k):
        super().get_queryset().update(price=F('price') * k)


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField()
    category = models.PositiveIntegerField(choices=Categories)

    objects = MyManager()

    def __repr__(self):
        return 'Product({})'.format(self.name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def get_price(self):
        return "{} grn".format(self.price)


class Feedback(models.Model):
    product = models.ForeignKey(Product)
    feedback = models.TextField('Отзыв')
    nick = models.CharField('Имя', max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Feedback {} {}'.format(self.nick, self.product)
