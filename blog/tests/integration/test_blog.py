from unittest import TestCase

from blog import Blog


class TestBlog(TestCase):

    def test_create_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(1, len(b.posts))
        self.assertEqual('Test Post', b.posts[0].title)
        self.assertEqual('Test Content', b.posts[0].content)

    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': []
        }
        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        b.create_post('Test Post1', 'Test Content1')
        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Test Post',
                    'content': 'Test Content'

                },
                {
                    'title': 'Test Post1',
                    'content': 'Test Content1'

                }
            ]
        }
        self.assertDictEqual(expected, b.json())



