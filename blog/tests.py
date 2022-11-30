from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from blog.models import Blog

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='',
            password='pass',
        )
        self.blog = Blog.objects.create(
            title='testtitle',
            body='testbody',
            author=self.user,
        )
    
    def test_blog(self):
        self.assertEqual(f'{self.blog.title}', 'testtitle')
        self.assertEqual(f'{self.blog.body}', 'testbody')
        self.assertEqual(f'{self.blog.author}', 'testuser')

    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(), '/post/testtitle/')

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testtitle')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog:detail',
                                           kwargs={'slug': self.blog.slug})
                                   )
        no_response = self.client.get(reverse('blog:detail',
                                              kwargs={'slug': "lmaolmaolmalo"})
                                      )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'testtitle')
        self.assertContains(response, 'testbody')
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_blog_crate_view(self):
        response = self.client.post(reverse('blog:new'), {
            'title': 'hello?',
            'body': 'hi, hru?',
            'author': self.user,
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'hello?')
        self.assertContains(response, 'hi, hru?')
