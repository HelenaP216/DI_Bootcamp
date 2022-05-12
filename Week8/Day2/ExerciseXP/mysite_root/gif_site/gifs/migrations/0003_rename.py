from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0002_auto_20211125_0415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
    ]