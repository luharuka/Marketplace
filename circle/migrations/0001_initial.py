# Generated by Django 3.2.5 on 2021-07-04 11:15

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=64, validators=[django.core.validators.MinLengthValidator(1)])),
                ('description', models.TextField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('price', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(blank=True, max_length=64)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Not Preferred to say')], default='X', max_length=1)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('ph_no', models.BigIntegerField(unique=True)),
                ('allowsMessage', models.BooleanField(default=True)),
                ('bookmarked', models.ManyToManyField(blank=True, related_name='bookmarked', to='circle.Article')),
                ('bought', models.ManyToManyField(blank=True, related_name='purchased', to='circle.Article')),
                ('cart', models.ManyToManyField(blank=True, related_name='cart', to='circle.Article')),
                ('following', models.ManyToManyField(blank=True, related_name='_circle_person_following_+', to='circle.Person')),
                ('rented', models.ManyToManyField(blank=True, related_name='rented', to='circle.Article')),
                ('sold', models.ManyToManyField(blank=True, related_name='sold', to='circle.Article')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)])),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive', to='circle.person')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send', to='circle.person')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='circle.Tag'),
        ),
    ]
