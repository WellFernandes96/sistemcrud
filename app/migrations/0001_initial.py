# Generated by Django 4.1.5 on 2023-01-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('preco', models.IntegerField()),
            ],
        ),
    ]
