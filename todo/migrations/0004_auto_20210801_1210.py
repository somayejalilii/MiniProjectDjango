# Generated by Django 3.2.5 on 2021-08-01 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_tasks_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2000)),
                ('priority', models.CharField(choices=[('Top', 'Top'), ('medium', 'Medium'), ('Down', 'Down')], max_length=10, verbose_name='priority')),
                ('time_reached', models.DateTimeField(verbose_name='Times hit task')),
                ('category', models.ManyToManyField(blank=True, related_name='tasks', to='todo.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]