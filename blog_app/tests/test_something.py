from django.test import TestCase, Client
from blog_app.models import Post
from django.contrib.auth.models import User
from django.urls import reverse


class BlogTestCase(TestCase):
    def setUp(self):
        self.api_client = Client()
        self.admin_user = User.objects.create_user("admin", "admin@email.com", "AdminPass")
        Post.objects.create(title="post_title", author=self.admin_user, slug="post-title")

    def test_post_was_created(self):
        # first step define the data for your test
        post_title = "test_post"
        Post.objects.create(title=post_title, slug="test-post", author=self.admin_user)

        # run the function that you want to test
        test_post = Post.objects.get(title=post_title)

        # verify the result
        self.assertEqual(test_post.title, post_title, "Test is not working")

    def test_view_post_detial_works(self):
        # prepare test data
        slug = "post-title-1"
        url = reverse("post_detail", kwargs={"slug": slug})
        Post.objects.create(title="some title", author=self.admin_user, slug=slug, content="hellooooooooo")
        
        # run test
        response = self.api_client.get(url)
        
        # check result
        self.assertContains(response, "hello")

    def test_view_post_detial_not_exist(self):
        # prepare test data
        slug = "post-title-1"
        _404_slug = "some-post"
        url = reverse("post_detail", kwargs={"slug": _404_slug})
        
        # run test
        response = self.api_client.get(url)
        
        # check result
        self.assertEqual(response.status_code, 404)
    
    def test_view_post_list_works(self):
        # prepare test data
        url = reverse("home")
        # run test
        response = self.api_client.get(url)
        
        # check result
        self.assertEqual(response.status_code, 200)
