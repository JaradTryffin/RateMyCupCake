from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Cake(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField()
    image=models.ImageField(default='default.jpg')



    created_by = models.ForeignKey(User,related_name='cakes',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Rate(models.Model):
    REFER_1_STAR = 'refer_1_star'
    REFER_2_STAR = 'refer_2_star'
    REFER_3_STAR = 'refer_3_star'
    REFER_4_STAR = 'refer_4_star'
    REFER_5_STAR = 'refer_5_star'

    CHOICES_RATE=(
        (REFER_1_STAR,'1_star'),
        (REFER_2_STAR,'2_star'),
        (REFER_3_STAR,'3_star'),
        (REFER_4_STAR,'4_star'),
        (REFER_5_STAR,'5_star'),
    )

    cake = models.ForeignKey(Cake, related_name='rates',on_delete=models.CASCADE)
    refer = models.CharField(max_length=20,choices=CHOICES_RATE,default=REFER_1_STAR)
    content = models.TextField()

    created_by = models.ForeignKey(User,related_name='rates',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

