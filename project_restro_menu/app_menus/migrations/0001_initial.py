# Generated by Django 4.2.1 on 2023-06-14 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=100)),
                ('category_code', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'restro_categories',
                'ordering': ['-category_title'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_title', models.CharField(max_length=100)),
                ('menu_price', models.FloatField(default=0.0)),
                ('menu_ingredient', models.CharField(max_length=100)),
                ('menu_img', models.FileField(blank=True, null=True, upload_to='images/menus/')),
                ('menu_created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('menu_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_menus.category')),
            ],
            options={
                'db_table': 'restro_menus',
                'ordering': ['-menu_title'],
            },
        ),
    ]
