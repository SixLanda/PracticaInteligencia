# Generated by Django 3.2.4 on 2023-12-08 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_formulario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('creation_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('pendiente', 'Pendiente'), ('completada', 'Completada')], max_length=10)),
                ('type', models.CharField(choices=[('general', 'General'), ('recordatorio', 'Recordatorio')], max_length=12)),
            ],
        ),
    ]
