import unittest
from yams import Yams

class TestYams(unittest.TestCase):

    def test_calculate_points_for_brelan(self):
        yams=Yams()
        result = yams.calculate_points([6,6,6,1,2])
        self.assertEqual(result,28)
        
    def test_calculate_points_for_carre(self):
        yams=Yams()
        result = yams.calculate_points([6,6,6,6,2])
        self.assertEqual(result,35)
        
    def test_calculate_points_for_full(self):
        yams=Yams()
        result = yams.calculate_points([6,6,6,2,2])
        self.assertEqual(result,30)
        
    def test_calculate_points_for_grande_suite(self):
        yams=Yams()
        result = yams.calculate_points([1,2,3,4,5])
        self.assertEqual(result,40) 
        
    def test_calculate_points_for_yams(self):
        yams=Yams()
        result = yams.calculate_points([6,6,6,6,6])
        self.assertEqual(result,50)
        
    def test_calculate_points_for_chance(self):
        yams=Yams()
        result = yams.calculate_points([1,3,4,5,6])
        sum = 1+3+4+5+6 #=19
        self.assertEqual(result,sum)     
        
        
    def test_is_brelan(self):
        yams=Yams()
        result = yams.is_brelan([6,6,6,1,2])
        self.assertEqual(result,True) 
        
    def test_is_carre(self):
        yams=Yams()
        result = yams.is_carre([6,6,6,6,1])
        self.assertEqual(result,True) 
        
    def test_is_full(self):
        yams=Yams()
        result = yams.is_full([6,6,6,2,2])
        self.assertEqual(result,True) 
        
    def test_is_grande_suite(self):
        yams=Yams()
        result = yams.is_grande_suite([1,2,3,4,5])
        self.assertEqual(result,True) 
        
    def test_is_yams(self):
        yams=Yams()
        result = yams.is_yams([6,6,6,6,6])
        self.assertEqual(result,True) 
        
    def test_is_brelan_false(self):
        yams = Yams()
        result = yams.is_brelan([1, 2, 3, 4, 5])
        self.assertEqual(result, False)  

    def test_is_carre_false(self):
        yams = Yams()
        result = yams.is_carre([1, 2, 3, 4, 5])
        self.assertEqual(result, False) 

    def test_is_full_false(self):
        yams = Yams()
        result = yams.is_full([1, 2, 3, 4, 5])
        self.assertEqual(result, False) 

    def test_is_grande_suite_false(self):
        yams = Yams()
        result = yams.is_grande_suite([1, 2, 3, 4, 6])
        self.assertEqual(result, False)  

    def test_is_yams_false(self):
        yams = Yams()
        result = yams.is_yams([1, 2, 3, 4, 5])
        self.assertEqual(result, False) 
        
if __name__ == '__main__':
    unittest.main()