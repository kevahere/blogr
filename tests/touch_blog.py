from app.models import Blog,User
from app import db
import unittest

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_Kev = User(username ='Kev',password ='pineapple', email='kevahere@gmail.com')
        self.new_blog = Blog(id=1,
                               title="Milk vendor",
                               blog_body="Sell milk indoors",
                               body="Sell milk all day everyday",
                               user_id=1,
                               category_id=1,
                               )

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,"Milk vendor")
        self.assertEquals(self.new_blog.blog_body,"Sell milk indoors")
        self.assertEquals(self.new_blog.body,"Sell milk all day everyday")
        self.assertEquals(self.new_blog.user_id,1)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blog = Blog.get_blog(1)
        self.assertTrue(got_blog is not None)