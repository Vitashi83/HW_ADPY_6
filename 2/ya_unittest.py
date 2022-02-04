import unittest
from ya_api import YaUploader

yd = YaUploader('YD token')

class TestSomething(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def test_response(self):
        self.assertEqual(str(yd.create_folder('552934290')), '<Response [409]>')

    def test_folder_appearence(self):
        self.assertIn('552934290', yd.checking_avaliability())

    def tearDown(self):
        print('method tearDown')

if __name__ == '__main__':
    unittest.main()