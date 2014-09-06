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

    def test_uses_results_template(self):
        response = self.client.get('/blog/search/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/results.html')

class DisplayPostsCorrectly(TestCase):

    def setUp(self):
        self.post_one = Post.objects.create(title='Test_One', author='Tester_One', category='Test_One', body_text='Just Testing One')
        self.post_two = Post.objects.create(title='Test_Two', author='Tester_Two', category='Test_Two', body_text='Just Testing Two')
        self.post_three = Post.objects.create(title='Test_Three', author='Tester_Three', category='Test_Three', body_text='Just Testing Three')

    def test_if_all_posts_are_listed_in_publications(self):
        posts = Post.objects.all()
        response = self.client.post('/blog/publications/', {'posts':posts})
        self.assertContains(response, self.post_one.author)
        self.assertContains(response, self.post_one.title)
        self.assertContains(response, self.post_one.category)
        self.assertContains(response, self.post_two.author)
        self.assertContains(response, self.post_two.title)
        self.assertContains(response, self.post_two.category)
        self.assertContains(response, self.post_three.author)
        self.assertContains(response, self.post_three.title)
        self.assertContains(response, self.post_three.category)

    def test_if_at_home_page_the_last_post_added_is_shown(self):
        response = self.client.get('/blog/')
        self.assertContains(response, self.post_three.author)
        self.assertContains(response, self.post_three.title)
        self.assertContains(response, self.post_three.category)
        self.assertContains(response, self.post_three.body_text)




