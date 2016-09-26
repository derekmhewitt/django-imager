from django.test import TestCase

from imager_images.models import Photo
# Create your tests here.


class PhotoTestCase(TestCase):
    def setUp(self):
        pass

    def test_babys_first_test(self):
        assert 1 == 1

    def tearDown(self):
        pass

"""
OK, so I had a conversation with Cris about testing.  First of all, I'm going to go after our models with a buzzsaw and cut out just about everything that isn't explicitely required as part of the assignment.  Additional things to do:
- create factory.py in each tests directory, our factories live there
- remember the difference between PhotoFactory.create() and .build() <-- this lets us test that properties instantiate properly when we save things manually inside our tests.
- Test created-on and last-modified dates by comparison - modify an extra property on the instance of the model and assert those dates are different, and that modified is after created.
- create a different test_modelname file for each model and another diff test file for every other major division."""
