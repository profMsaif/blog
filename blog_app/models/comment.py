from datetime import datetime

from django.db import models



class Comment(models.Model):
    post = models.ForeignKey(
        "Post", related_name="comments", on_delete=models.CASCADE, null=False
    )
    name = models.CharField(max_length=128)
    body = models.CharField(max_length=255)
    email = models.EmailField(null=False)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}:{self.body}"
