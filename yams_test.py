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
        
if __name__ == '__main__':
    unittest.main()