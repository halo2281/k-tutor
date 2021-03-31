# Generated by Django 3.1.7 on 2021-03-31 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_learned_kw'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievedManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=200)),
                ('orm', models.TextField()),
                ('image', models.TextField()),
                ('condition', models.IntegerField(default=0)),
                ('achieved', models.ManyToManyField(related_name='achieved_user', through='account.AchievedManage', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='achievedmanage',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.achievement'),
        ),
        migrations.AddField(
            model_name='achievedmanage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
