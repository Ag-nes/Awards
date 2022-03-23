from unittest.suite import TestSuite
from django.test import TestCase
from .models import Profile,Projects,Image,Self
from django.contrib.auth.models import User


class ProfileTest(TestCase):
    def setUp(self):
        self.tess = User(username = 'Aggie',email = 'faithagnes2@gmail.com')
        self.tess = Profile(user = Self.tess,user = 1,bio = 'tests',photo = 'test.jpg',date_created='Mar,23.2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.tess,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.tess.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)


class ProjectsTestCase(TestCase):
    def setUp(self):
        self.new_post = Projects(title = 'testT',shot = 'test.jpg',description = 'testD',user = TestSuite,url = 'https://test.com',date_created='Mar,23.2022')


    def test_save_project(self):
        self.new_post.save_project()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        pictures = Projects.objects.all()
        self.assertEqual(len(pictures),1)
