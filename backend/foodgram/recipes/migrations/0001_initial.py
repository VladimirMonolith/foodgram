# Generated by Django 3.2.15 on 2022-10-08 08:13

from django.db import migrations, models

import colorfield.fields
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Hазвание')),
                ('measurement_unit', models.CharField(max_length=10, verbose_name='единица измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='IngredientAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Количество ингредиента не может быть нулевым')], verbose_name='количество')),
            ],
            options={
                'verbose_name': 'Соответствие ингредиента и рецепта',
                'verbose_name_plural': 'Таблица соответствия ингредиентов и рецептов',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='изображение')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Hазвание')),
                ('text', models.TextField(verbose_name='описание')),
                ('cooking_time', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Время приготовления не может быть меньше 1')], verbose_name='время приготовления (в минутах)')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата публикации')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Hазвание')),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=7, samples=None, unique=True, verbose_name='цвет')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(message='Слаг тега содержит недопустимый символ', regex='^[-a-zA-Z0-9_]+$')], verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to='recipes.recipe', verbose_name='рецепт')),
            ],
            options={
                'verbose_name': 'Рецепт пользователя для списка покупок',
                'verbose_name_plural': 'Рецепты пользователей для списка покупок',
                'ordering': ('user',),
            },
        ),
    ]