from django.db import models
from django.shortcuts import reverse


class TodoList(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def done_link(self):
        return reverse('todolist:done', self.id)
        