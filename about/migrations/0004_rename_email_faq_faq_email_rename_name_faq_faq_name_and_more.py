# Generated by Django 4.2.6 on 2023-11-30 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_faq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='email',
            new_name='faq_email',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='name',
            new_name='faq_name',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='question',
            new_name='faq_question',
        ),
    ]
