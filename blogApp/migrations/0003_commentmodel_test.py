# Generated by Django 4.1.5 on 2023-01-17 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_rename_comments_blogmodel_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog', to='blogApp.blogmodel'),
        ),
    ]
