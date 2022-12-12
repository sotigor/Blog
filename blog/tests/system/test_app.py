from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class TestApp(TestCase):

    # Testing the menu choice
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'q')

                app.menu()

                mocked_ask_create_blog.assert_called()

    def test_menu_result_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Blog_title', 'Blog_author', 'q')

            app.menu()

            expected = 'Blog_title by Blog_author (0 posts)'
            self.assertIsNotNone(app.blogs['Blog_title'])
            self.assertEqual(expected, str(app.blogs['Blog_title']))


    def test_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:
                mocked_input.side_effect = ('l','q')

                app.menu()

                mocked_print_blogs.assert_called()

    def test_result_print_blogs(self):
        blog = Blog('Blog title', 'Blog content')
        app.blogs['Blog title'] = blog
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('l', 'q')

                app.menu()

                expected = '-Blog title by Blog content (0 posts)'
                mocked_print.assert_called_with(expected)


    def test_calls_ask_read_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_ask_read_blog:
                mocked_input.side_effect = ('r', 'q')

                app.menu()

                mocked_ask_read_blog.assert_called()

    def test_result_ask_read_blog(self):
        blog = Blog('Blog title', 'Blog author')
        app.blogs['Blog title'] = blog
        post = Post('Post title', 'Post content')
        blog.posts.append(post)
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('r', 'Blog title', 'q')

                app.menu()

                mocked_print.assert_called_with('''
--- Post title ---
Post content
    ''')

    def test_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_input.side_effect=('p','q')

                app.menu()

                mocked_ask_create_post.assert_called()


    def test_result_ask_create_post(self):

        app.blogs['Blog title'] = Blog('Blog title', 'Blog author')

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'Blog title', 'Post title', 'Post content', 'q')

            app.menu()

            self.assertEqual('Post title', app.blogs['Blog title'].posts[0].title)
            self.assertEqual('Post content', app.blogs['Blog title'].posts[0].content)

    """
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input1:
            with patch('builtins.input', return_value = 'q') as mocked_input2:

                app.menu()
                mocked_input1.assert_called_with(app.MENU_PROMPT)
    """

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('-Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect=('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                # mocked_input.assert_called()
                mocked_print_posts.assert_called_with(blog)


    def test_print_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        blog.create_post('Title', 'Content')
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])


    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected = '''
--- Post title ---
Post content
    '''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected)

    def test_ask_create_post(self):
        blog = Blog('Title_blog', 'Author_blog')
        app.blogs['Title_blog'] = blog
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Title_blog', 'Title', 'Content')
            app.ask_create_post()
            self.assertEqual('Title', blog.posts[0].title)
            self.assertEqual('Content', blog.posts[0].content)






