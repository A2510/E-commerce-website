# Generated by Django 3.1.1 on 2021-06-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210620_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emali', models.EmailField(max_length=254)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
