# Generated by Django 2.2.12 on 2021-05-04 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_age', models.IntegerField()),
                ('user_rol', models.PositiveSmallIntegerField(choices=[(1, 'Academico'), (2, 'Usuario RS'), (3, 'Grupo vulnerable')], default=1)),
                ('user_gender', models.PositiveSmallIntegerField(choices=[(1, 'Hombre'), (2, 'Mujer'), (3, 'Otro')], default=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
