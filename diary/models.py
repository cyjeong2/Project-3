from django.db import models


class Memory(models.Model):
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    # def __str__(self):
    #     return f'[{self.user_name}]{self.created_at}'

    # def get_absolute_url(self):
    #     return f"/diary/{self.pk}/"

    class Meta:
        # 쿼리셋에서 order_by를 지정하지 않았을 때, 사용되는 기본 정렬
        ordering = ['-id']
