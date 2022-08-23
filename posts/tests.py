from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
    # Create User
        testuser1 = User.objects.create_user(username='testuser',password='qwerty')
        testuser1.save()
    # Create post
        test_post = Post.objects.create(
            title = 'test title',
            author = testuser1,
            body = 'test body.'
        )
        test_post.save()
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        author = f'{post.author}'
        body = f'{post.body}'
        self.assertEqual(title,'test title')
        self.assertEqual(author, 'testuser')
        self.assertEqual(body, 'test body.')
# Create your tests here.
