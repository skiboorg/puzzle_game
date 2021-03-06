# Generated by Django 3.0.6 on 2020-06-22 19:14

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Правила')),
                ('rules_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Правила')),
                ('rules_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Правила')),
                ('rules_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Правила')),
                ('about', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='О нас')),
                ('about_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='О нас')),
                ('about_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='О нас')),
                ('about_zh_cn', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='О нас')),
            ],
        ),
    ]
