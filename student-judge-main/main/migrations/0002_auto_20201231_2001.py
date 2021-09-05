# Generated by Django 3.1.4 on 2020-12-31 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='about',
            name='Active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Class',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('J.S.C', 'J.S.C'), ('S.S.C', 'S.S.C'), ('H.S.C 1st', 'H.S.C 1st'), ('H.S.C 2nd', 'H.S.C 2nd')], default='-----', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='chapter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='Class',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('J.S.C', 'J.S.C'), ('S.S.C', 'S.S.C'), ('H.S.C 1st', 'H.S.C 1st'), ('H.S.C 2nd', 'H.S.C 2nd')], default='-----', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='chapter',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
