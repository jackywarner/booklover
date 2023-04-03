import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        test_object1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object1.add_book("Book1", 4)
        self.assertTrue(test_object1.has_read("Book1"))

    def test_2_add_book(self):
        test_object2 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object2.add_book("Book1", 4)
        test_object2.add_book("Book1", 2)
        self.assertEqual(test_object2.num_books_read(), 1)
        
    def test_3_add_book(self):
        test_object3 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object3.add_book("Book1", 4)
        # test_object3.add_book("Book1", 2)
        self.assertTrue(test_object3.has_read("Book1"))
    
    def test_4_add_book(self):
        test_object4 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object4.add_book("Book1", 4)
        # test_object3.add_book("Book1", 2)
        self.assertFalse(test_object4.has_read("Book2"))
    
    def test_5_add_book(self):
        test_object5 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object5.add_book("Book1", 4)
        test_object5.add_book("Book2", 4)
        test_object5.add_book("Book3", 4)
        test_object5.add_book("Book4", 4)
        # test_object3.add_book("Book1", 2)
        self.assertEqual(test_object5.num_books_read(),4)

    def test_6_add_book(self):
        test_object6 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object6.add_book("Book1", 4)
        test_object6.add_book("Book2", 3)
        test_object6.add_book("Book90", 5)
        test_object6.add_book("Book3", 2)
        test_object6.add_book("Book4", 1)
        # test_object3.add_book("Book1", 2)
        fav_books_df = test_object6.fav_books()
        self.assertEqual(len(fav_books_df), 2)  
        self.assertTrue((fav_books_df['book_rating'] > 3).all())

if __name__ == '__main__':
    unittest.main(verbosity=3)
