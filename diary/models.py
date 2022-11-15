from django.db import models


class Memory(models.Model):
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    weather_choices = {('맑음', '맑음'),
                       ('흐림', '흐림'),
                       ('비', '비'),
                       ('눈', '눈')}

    # drawing_choices = {('Digital Art', '디지털 아트'),
    #                    ('Oil and Canvas', '유화'),
    #                    ('Sketched', '스케치'),
    #                    ('Impressionism', '인상주의'),
    #                    ('Vaper Wave','MZ세대 스타일'),
    #                    }
    drawing_choices = {('디지털 아트', 'Digital Art'),
                       ('유화', 'Oil and Canvas'),
                       ('스케치', 'Sketched'),
                       ('인상주의', 'Impressionism'),
                       ('MZ세대 스타일','Vaper Wave'),
                       }

    # emotion_choices = {('Cheerful', '쾌활'),
    #                    ('Happy', '기쁨'),
    #                    ('Neutral', '보통'),
    #                    ('Depressed', '우울'),
    #                    ('Angry', '화남')
    #                    }
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
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    weather_choices = {('맑음', '맑음'),
                       ('흐림', '흐림'),
                       ('비', '비'),
                       ('눈', '눈')}

    # drawing_choices = {('Digital Art', '디지털 아트'),
    #                    ('Oil and Canvas', '유화'),
    #                    ('Sketched', '스케치'),
    #                    ('Impressionism', '인상주의'),
    #                    ('Vaper Wave', 'MZ세대 스타일'),
    #                    }
    drawing_choices = {('디지털 아트', 'Digital Art'),
                       ('유화', 'Oil and Canvas'),
                       ('스케치', 'Sketched'),
                       ('인상주의', 'Impressionism'),
                       ('MZ세대 스타일','Vaper Wave'),
                       }

    # emotion_choices = {('Cheerful', '쾌활'),
    #                    ('Happy', '기쁨'),
    #                    ('Neutral', '보통'),
    #                    ('Depressed', '우울'),
    #                    ('Angry', '화남'),
    #                    }
    emotion_choices = {('쾌활', 'Cheerful'),
                       ('기쁨', 'Happy'),
                       ('보통', 'Neutral'),
                       ('우울', 'Depressed'),
                       ('화남', 'Angry')
                       }

    Weather = models.CharField(max_length=20, choices=weather_choices, null=True)
    Drawing = models.CharField(max_length=20, choices=drawing_choices, null=True)
    Emotion = models.CharField(max_length=20, choices=emotion_choices, null=True)
    # title = models.CharField(max_length=30)

    content1 = models.TextField(max_length=15)
    content2 = models.TextField(max_length=15)
    content3 = models.TextField(max_length=15)

    create_dat = models.DateTimeField(auto_now_add=True)
    update_dat = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f"/diary/{self.pk}/"

    def __str__(self):
        return f"[{self.pk}] {self.content1} "
