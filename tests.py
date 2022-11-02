from unittest import TestCase

import main


class Test(TestCase):
    def test_num_keys(self):
        self.assertEqual(len(main.choose_keys(3, 5)), 8)

