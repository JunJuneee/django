from django.db import models


class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    update = models.DateTimeField(auto_now=True)  # 매번 실행
    created = models.DateTimeField(auto_now_add=True)  # 처음만 실행

    def __str__(self):
        return self.body[0:50]
