# Generated by Django 2.2.5 on 2021-11-08 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('방이름', models.CharField(max_length=140)),
                ('방소개', models.TextField()),
                ('국가', django_countries.fields.CountryField(max_length=2)),
                ('도시', models.CharField(max_length=80)),
                ('가격', models.IntegerField()),
                ('주소', models.CharField(max_length=140)),
                ('투숙객', models.IntegerField()),
                ('침대', models.IntegerField()),
                ('화장실', models.IntegerField()),
                ('욕조', models.IntegerField()),
                ('체크인_시간', models.TimeField()),
                ('체크아웃_시간', models.TimeField()),
                ('예약', models.BooleanField(default=False)),
                ('주인장', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
