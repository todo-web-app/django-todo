from django.test import TestCase
from django.urls import reverse

from .models import TodoList


class TodoViewTestCase(TestCase):

    def setUp(self):
        self.todo_1 = TodoList.objects.create(title='Wash dishes')
        self.todo_2 = TodoList.objects.create(title='Grocery')

    def test_index(self):
        url = reverse('todolist:index')

        response = self.client.get(url)

        self.assertContains(response, self.todo_1.title)
        self.assertContains(response, self.todo_2.title)

    def test_add(self):
        url = reverse('todolist:add')
        data = {'title': 'Walking'}

        response = self.client.post(url, data, follow=True)

        self.assertTrue(response.redirect_chain)
        self.assertContains(response, data['title'])

    def test_delete(self):
        url = reverse('todolist:delete', kwargs={'todo_id': self.todo_1.id})

        response = self.client.get(url, follow=True)
        
        self.assertNotContains(response, self.todo_1.title)

    def test_done(self):
        url = reverse('todolist:done', kwargs={'todo_id': self.todo_1.id})

        response = self.client.get(url, follow=True)
        
        self.assertContains(response, '<del>')
