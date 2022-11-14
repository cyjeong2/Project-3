# Generated by Django 4.1.2 on 2022-11-14 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0014_alter_keywordpost_drawing_alter_keywordpost_emotion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keywordpost",
            name="Drawing",
            field=models.CharField(
                choices=[
                    ("Digital Art", "디지털 아트"),
                    ("Sketched", "스케치"),
                    ("Oil and Canvas", "유화"),
                    ("Impressionism", "인상주의"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="keywordpost",
            name="Emotion",
            field=models.CharField(
                choices=[
                    ("Angry", "화남"),
                    ("Cheerful", "쾌활"),
                    ("Happy", "기쁨"),
                    ("Neutral", "보통"),
                    ("Depressed", "우울"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="keywordpost",
            name="Weather",
            field=models.CharField(
                choices=[
                    ("Rainy", "비"),
                    ("Sunny", "맑음"),
                    ("Cloudy", "흐림"),
                    ("Snowy", "눈"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="memory",
            name="Drawing",
            field=models.CharField(
                choices=[
                    ("Digital Art", "디지털 아트"),
                    ("Sketched", "스케치"),
                    ("Oil and Canvas", "유화"),
                    ("Impressionism", "인상주의"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="memory",
            name="Emotion",
            field=models.CharField(
                choices=[
                    ("Angry", "화남"),
                    ("Cheerful", "쾌활"),
                    ("Happy", "기쁨"),
                    ("Neutral", "보통"),
                    ("Depressed", "우울"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="memory",
            name="Weather",
            field=models.CharField(
                choices=[
                    ("Rainy", "비"),
                    ("Sunny", "맑음"),
                    ("Cloudy", "흐림"),
                    ("Snowy", "눈"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
