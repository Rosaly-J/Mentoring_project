from django.db import models

class Memo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True) # 현재 시간으로 세팅



    def __str__(self):
        return self.title