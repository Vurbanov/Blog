from django.test import TestCase
from blog.models import Post, Comments

class CorrectTemplateTests(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title='Test', author='Tester', category='Test', body_text='Just Testing')

    def test_uses_contacts_template(self):
        response = self.client.get('/blog/contacts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/contacts.html')

    def test_uses_index_template(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_uses_posts_template(self):
        response = self.client.get('/blog/' + str(self.post.id) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts.html')
        self.assertContains(response, self.post.author)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.category)
        self.assertContains(response, self.post.body_text)
        

    def test_uses_publications_template(self):
        response = self.client.get('/blog/publications/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/publications.html')
