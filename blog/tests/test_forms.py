from django.test import SimpleTestCase

from blog.forms import *


class TestForms(SimpleTestCase):
    def test_comment_form_has_valid_data(self):
        form = CommentForm(
            data={
                "name": "johnny",
                "email": "johnny@test.email",
                "body": "comment content",
            }
        )

        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
