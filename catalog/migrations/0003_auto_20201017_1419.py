# Generated by Django 3.1.1 on 2020-10-17 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201004_2134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_view_all_borrowed_books', 'can_edit_all_borrowed_books'),)},
        ),
    ]