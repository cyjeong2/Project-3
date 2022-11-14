from django.db import models


class Memory(models.Model):
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    Emotion = models.CharField(max_length=20, choices=weather_choices, null=True)
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
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
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
    Emotion = models.CharField(max_length=20, choices=weather_choices, null=True)
    # title = models.CharField(max_length=30)

    content1 = models.TextField(max_length=7)
    content2 = models.TextField(max_length=7)
    content3 = models.TextField(max_length=7)

    create_dat = models.DateTimeField(auto_now_add=True)
    update_dat = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f"/diary/{self.pk}/"

    def __str__(self):
        return f"[{self.pk}] {self.content} "
