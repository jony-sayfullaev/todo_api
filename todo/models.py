from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Todo(models.Model):
    NEW = "new"
    FINISHED = "finished"

    STATUS = [
        ("NEW", "new"),
        ("FINISHED", "finished")
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    status = models.CharField(choices=STATUS, max_length=10, default=NEW)

    def mark_as_finished(self):
        self.status = self.FINISHED
        self.save()

    def mark_as_unfinished(self):
        self.status = self.NEW
        self.save()
