from django.db import models

class Post(models.Model):
    # 미니미 4종류 중에 하나 고르기
    MINIMI_CHOICES = [
        (1, '미니미1'),
        (2, '미니미2'),
        (3, '미니미3'),
        (4, '미니미4'),
    ]

    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    content = models.TextField()
    minimi = models.IntegerField(choices=MINIMI_CHOICES, default=1)
    is_secret = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-idx'] # 최신 글이 위로

    def __str__(self):
        return self.name
