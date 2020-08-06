from django.db import models

# Create your models here.


class Place(models.Model):
    city = models.CharField(max_length=64, verbose_name='城市')
    address = models.CharField(max_length=128, verbose_name='详细地址')

    class Meta:
        verbose_name_plural = verbose_name = '地址'

    def __str__(self):
        return f'{self.city} {self.address}'


class Restaurant(models.Model):
    name = models.CharField(max_length=128, verbose_name='店名')
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='地址',
    )
    serves_hot_dogs = models.BooleanField(default=False, verbose_name='售卖热狗')
    serves_pizza = models.BooleanField(default=False, verbose_name='售卖Pizza')

    class Meta:
        verbose_name_plural = verbose_name = '饭店'

    def __str__(self):
        return f'饭店（{self.name}）'


class Waiter(models.Model):
    name = models.CharField(max_length=128, verbose_name='姓名')
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        verbose_name='所属饭店'
    )

    class Meta:
        verbose_name_plural = verbose_name = '服务员'

    def __str__(self):
        return f'服务员（{self.name}）'
