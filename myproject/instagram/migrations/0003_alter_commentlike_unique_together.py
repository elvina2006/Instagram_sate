# Generated by Django 5.1.4 on 2024-12-23 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_post_description_en_post_description_ru_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='commentlike',
            unique_together={('user', 'comment')},
        ),
    ]
