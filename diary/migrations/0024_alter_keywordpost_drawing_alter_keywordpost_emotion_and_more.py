# Generated by Django 4.1.2 on 2022-11-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0023_remove_memory_head_image_alter_keywordpost_drawing_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keywordpost",
            name="Drawing",
            field=models.CharField(
                choices=[
                    ("Oil and Canvas", "Oil and Canvas"),
                    ("Impressionism", "Impressionism"),
                    ("Sketched", "Sketched"),
                    ("Digital Art", "Digital Art"),
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
                    ("Depressed", "Depressed"),
                    ("Neutral", "Neutral"),
                    ("Happy", "Happy"),
                    ("Cheerful", "Cheerful"),
                    ("Angry", "Angry"),
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
                    ("Snowy", "Snowy"),
                    ("Sunny", "Sunny"),
                    ("Rainy", "Rainy"),
                    ("Cloudy", "Cloudy"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="keywordpost",
            name="content1",
            field=models.TextField(max_length=7),
        ),
        migrations.AlterField(
            model_name="keywordpost",
            name="content2",
            field=models.TextField(max_length=7),
        ),
        migrations.AlterField(
            model_name="keywordpost",
            name="content3",
            field=models.TextField(max_length=7),
        ),
        migrations.AlterField(
            model_name="memory",
            name="Drawing",
            field=models.CharField(
                choices=[
                    ("디지털 아트", "Digital Art"),
                    ("유화", "Oil and Canvas"),
                    ("MZ세대 스타일", "Vaper Wave"),
                    ("스케치", "Sketched"),
                    ("인상주의", "Impressionism"),
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
                    ("화남", "Angry"),
                    ("보통", "Neutral"),
                    ("우울", "Depressed"),
                    ("기쁨", "Happy"),
                    ("쾌활", "Cheerful"),
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
                    ("흐림", "Cloudy"),
                    ("맑음", "Sunny"),
                    ("비", "Rainy"),
                    ("눈", "Snowy"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]