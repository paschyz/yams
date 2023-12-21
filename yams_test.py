import unittest
from yams import Yams

class TestYams(unittest.TestCase):
    figurePoints = {
        "brelan": 28,
        "carre": 35,
        "full": 30,
        "grande_suite": 40,
        "yams": 50,
    }

    
    def test_calculate_points_for_brelan(self):
        yams=Yams()
        result = yams.calculate_points([6,6,6,1,2])
        self.assertEqual(result,self.figurePoints["brelan"])
        
    def test_calculate_points_for_carre(self):
        yams=Yams()
        result = yams.calculate_points([6,6,6,6,2])
        self.assertEqual(result,self.figurePoints["carre"])
                
    def test_calculate_points_for_full(self):
        yams=Yams()
        result = yams.calculate_points([6,6,6,2,2])
        self.assertEqual(result,self.figurePoints["full"])
                        
    def test_calculate_points_for_grande_suite(self):
        yams=Yams()
        result = yams.calculate_points([1,2,3,4,5])
        self.assertEqual(result,self.figurePoints["grande_suite"])
                        
    def test_calculate_points_for_yams(self):
        yams=Yams()
        result = yams.calculate_points([6,6,6,6,6])
        self.assertEqual(result,self.figurePoints["yams"])
                        
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
        
    def test_calculate_points_for_multiple_yams(self):
        yams = Yams()
        result = yams.calculate_points([6, 6, 6, 6, 6])
        self.assertEqual(result, self.figurePoints["yams"])

        # Second throw also yams
        result = yams.calculate_points([1, 1, 1, 1, 1])
        self.assertEqual(result, self.figurePoints["carre"])
        
if __name__ == '__main__':
    unittest.main()