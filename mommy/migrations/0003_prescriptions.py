# Generated by Django 3.1.3 on 2021-03-29 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mommy', '0002_post_reciever'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reciever', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reciever_pres', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
