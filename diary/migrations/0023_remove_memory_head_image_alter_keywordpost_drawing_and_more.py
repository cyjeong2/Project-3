# Generated by Django 4.1.2 on 2022-11-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0022_memory_head_image_alter_keywordpost_drawing_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="memory", name="head_image",),
        migrations.AlterField(
            model_name="keywordpost",
            name="Drawing",
            field=models.CharField(
                choices=[
                    ("스케치", "Sketched"),
                    ("유화", "Oil and Canvas"),
                    ("인상주의", "Impressionism"),
                    ("요즘 스타일", "Vaper Wave"),
                    ("디지털 아트", "Digital Art"),
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
                    ("쾌활", "Cheerful"),
                    ("기쁨", "Happy"),
                    ("화남", "Angry"),
                    ("보통", "Neutral"),
                    ("우울", "Depressed"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="keywordpost",
            name="Weather",
            field=models.CharField(
                choices=[("흐림", "흐림"), ("맑음", "맑음"), ("비", "비"), ("눈", "눈")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="memory",
            name="Drawing",
            field=models.CharField(
                choices=[
                    ("스케치", "Sketched"),
                    ("유화", "Oil and Canvas"),
                    ("인상주의", "Impressionism"),
                    ("요즘 스타일", "Vaper Wave"),
                    ("디지털 아트", "Digital Art"),
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
                    ("쾌활", "Cheerful"),
                    ("기쁨", "Happy"),
                    ("화남", "Angry"),
                    ("보통", "Neutral"),
                    ("우울", "Depressed"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="memory",
            name="Weather",
            field=models.CharField(
                choices=[("흐림", "흐림"), ("맑음", "맑음"), ("비", "비"), ("눈", "눈")],
                max_length=20,
                null=True,
            ),
        ),
    ]
