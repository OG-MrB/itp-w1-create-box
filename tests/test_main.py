import unittest

from create_box import create_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

fourth_box_expected = """
'invalid'
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_large_box(self):
        self.assertEqual(create_box(3, 24, 'x'), third_box_expected)

    # def test_zero_width(self):
    #     self.assertEqual(create_box(2, 0, '0'), fourth_box_expected)
        
    # def test_zero_height(self):
    #     self.assertEqual(create_box(0, 3, '!'), fourth_box_expected)
        
    
    # Add your own test using third_box_expected
