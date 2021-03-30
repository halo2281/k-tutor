from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    consecutive_access = models.IntegerField(default=1)
    learned_lc = models.ManyToManyField('klass.Lc', related_name='learned_user')
    learned_kw = models.ManyToManyField('klass.kw', related_name='learned_user')


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    test_at = models.DateField(auto_now_add=True)


class AccessDate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_at = models.DateField(auto_now_add=True)


class Recent_learned_lc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lc = models.ForeignKey('klass.Lc', on_delete=models.CASCADE)
    learned_at = models.DateField(auto_now_add=True)


class Achievement(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    image = models.TextField()
    condition = models.IntegerField(default=0)

class UserUnlockedAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)