from django.db import models


class TodoList(models.Model):
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description
