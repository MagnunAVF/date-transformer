import unittest

from faker import Faker

from src.date_transformer import DateTransformer


class TestDateTransformer(unittest.TestCase):
    def setUp(self):
        self.date_transformer = DateTransformer()
        self.fake = Faker()

    def test_change_date(self):
        result = self.date_transformer.change_date(
                                                "01/03/2010 23:00", '+', 4000)

        self.assertEqual(result, "01/03/2010 23:00")
