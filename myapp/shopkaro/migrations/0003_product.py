# Generated by Django 4.0.4 on 2022-05-17 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopkaro', '0002_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_description', models.TextField(max_length=5000)),
                ('price', models.IntegerField()),
                ('product_image1', models.ImageField(blank=True, null=True, upload_to='productimages')),
                ('product_image2', models.ImageField(blank=True, null=True, upload_to='productimages')),
                ('product_image3', models.ImageField(blank=True, null=True, upload_to='productimages')),
                ('discount', models.IntegerField(null=True)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopkaro.category')),
                ('subcat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopkaro.subcategory')),
            ],
        ),
    ]
