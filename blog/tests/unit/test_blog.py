from unittest import TestCase
from blog import Blog
from post import Post

class TestBlog(TestCase):

    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')
        self.assertEqual('Test by Test Author (0 posts)', b.__repr__())
        self.assertEqual('My Day by Rolf (0 posts)', b2.__repr__())

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        self.assertEqual('Test by Test Author (1 post)', b.__repr__())



