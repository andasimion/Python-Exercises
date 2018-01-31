import unittest
from book_keeping import Product, Batch, Warehouse
import datetime

class TestBookKeeping(unittest.TestCase):
    
    def test_bbd_as_date(self):
        batch_321234 = Batch(1, 'Tertensif', '321234', '23.04.2017', '30.04.2020', 100)
        self.assertEqual(batch_321234.bbd_as_date(), datetime.datetime.strptime('30.04.2020', '%d.%m.%Y').date())

    def test_add_product_when_two_products_are_added(self):
        

if __name__ == '__main__':
    unittest.main()	
