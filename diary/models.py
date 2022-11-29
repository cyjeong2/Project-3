from django.db import models

from urllib.parse import urlparse

# from django.core.files import File

# from utils.file import download, get_buffer_ext # 위에서 만든 file.py 경로


class Memory(models.Model):

    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    weather_choices = {('맑음','Sunny' ),
                       ( '흐림','Cloudy'),
                       ('비', 'Rainy'),
                       ('눈', 'Snowy')}

    drawing_choices = {('디지털 아트', 'Digital Art'),
                       ('유화', 'Oil and Canvas'),
                       ('스케치', 'Sketched'),
                       ('인상주의', 'Impressionism'),
                       ('MZ세대 스타일','Vaper Wave'),
                       }
                       
    emotion_choices = {('쾌활', 'Cheerful'),
                       ('기쁨', 'Happy'),
                       ('보통', 'Neutral'),
                       ('우울', 'Depressed'),
                       ('화남', 'Angry')
                       }

    Weather = models.CharField(max_length=20, choices=weather_choices, null=True)
    Drawing = models.CharField(max_length=20, choices=drawing_choices, null=True)
    Emotion = models.CharField(max_length=20, choices=emotion_choices, null=True)
    def __str__(self):
        return f'[{self.pk}]{self.content}'

    # def __str__(self):
    #     return f'[{self.user_name}]{self.created_at}'

    def get_absolute_url(self):
        return f"/diary/{self.pk}/"

    class Meta:
        # 쿼리셋에서 order_by를 지정하지 않았을 때, 사용되는 기본 정렬
        ordering = ['-id']


class KeywordPost(models.Model):
    weather_choices = {('Sunny', 'Sunny'),
                       ('Cloudy', 'Cloudy'),
                       ('Rainy', 'Rainy'),
                       ('Snowy', 'Snowy')}

    drawing_choices = {('Digital Art', 'Digital Art'),
                       ('Oil and Canvas', 'Oil and Canvas'),
                       ('Sketched', 'Sketched'),
                       ('Impressionism', 'Impressionism'),
                       # ('','')
                       }
    emotion_choices = {('Cheerful', 'Cheerful'),
                       ('Happy', 'Happy'),
                       ('Neutral', 'Neutral'),
                       ('Depressed', 'Depressed'),
                       ('Angry', 'Angry')
                       }

    Weather = models.CharField(max_length=20, choices=weather_choices, null=True)
    Drawing = models.CharField(max_length=20, choices=drawing_choices, null=True)
    Emotion = models.CharField(max_length=20, choices=emotion_choices, null=True)
    # title = models.CharField(max_length=30)

    content1 = models.TextField(max_length=7)
    content2 = models.TextField(max_length=7)
    content3 = models.TextField(max_length=7)

    create_dat = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f"/diary/{self.pk}/"

    def __str__(self):
        return f"[{self.pk}] {self.content} "


class ImageFields(models.Model):
    mainImage = models.ImageField()
    keywords = models.TextField()
    url1 = models.TextField()
    url2 = models.TextField()
    url3 = models.TextField()
    url4 = models.TextField()


class FinImg(models.Model):
    finImg = models.ImageField(null=True, blank=True)
