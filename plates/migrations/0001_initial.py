# Generated by Django 3.2.18 on 2023-05-02 05:59


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import plates.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='식당 이름')),
                ('description', models.TextField(verbose_name='설명')),
                ('address', models.CharField(max_length=200, verbose_name='주소')),
                ('restaurant_type', models.CharField(max_length=50, verbose_name='식당 종류')),
                ('loc', models.CharField(max_length=50, verbose_name='위치')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=plates.models.Post.post_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종수정일')),
                ('parking', models.BooleanField(default=False, verbose_name='주차가능')),
                ('price_range', models.IntegerField(default=0, verbose_name='가격대')),
                ('phone_number', models.CharField(blank=True, max_length=20, verbose_name='전화번호')),
                ('closed_days', models.CharField(blank=True, max_length=50, verbose_name='휴무일')),
                ('rating', models.IntegerField(blank=True, default=0, verbose_name='평점')),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('rating', models.IntegerField(verbose_name='평점')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='업로드 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('taste_evaluation', models.CharField(choices=[('맛있다', '맛있다'), ('괜찮다', '괜찮다'), ('별로', '별로')], max_length=10)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=plates.models.Review.post_image_path)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plates.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAndAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(verbose_name='업로드 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plates.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(verbose_name='업로드 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plates.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
