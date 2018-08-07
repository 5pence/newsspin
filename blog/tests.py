from django.test import TestCase
from blog.models import Post


class TestBlog(TestCase):
    def test_create_post(self):
