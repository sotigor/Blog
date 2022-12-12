from unittest import TestCase
from post import Post

class TestPost(TestCase):

    def test_check_quant_attr(self):
        p = Post('Test', 'Test Content')
        self.assertEqual(2, len(p.__dict__))

    def test_create_post(self):
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        self.assertDictEqual(expected, p.json())