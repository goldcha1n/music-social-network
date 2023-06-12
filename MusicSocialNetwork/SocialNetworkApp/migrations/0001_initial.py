# Generated by Django 4.2 on 2023-06-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.CharField(max_length=255)),
                ('comment_date', models.DateField(auto_now_add=True)),
                ('is_self', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Like_Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MusicPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=255)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('audio_post', models.FileField(upload_to='music_posts/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=255)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('photo_post', models.ImageField(default='photo_post/Rap.png', upload_to='photo_post/')),
            ],
        ),
    ]
