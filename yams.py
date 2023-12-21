class Yams:
    def __init__ (self):
        self.figures = {
        "brelan":[28,True],
        "carre":[35,True],
        "full":[30,True],
        "grande_suite":[40,True],
        "yams":[50,True],
    }
    
    def calculate_points(self, dice_results):
        if self.is_yams(dice_results) and self.figures["yams"][1]:
            self.figures["yams"][1] = False
            return self.figures["yams"][0]
        elif self.is_carre(dice_results) and self.figures["carre"][1]:
            self.figures["carre"][1] = False
            return self.figures["carre"][0]
        elif self.is_full(dice_results) and self.figures["full"][1]:
            self.figures["full"][1] = False
            return self.figures["full"][0]
        elif self.is_brelan(dice_results) and self.figures["brelan"][1]:
            self.figures["brelan"][1] = False
            return self.figures["brelan"][0]
        elif self.is_grande_suite(dice_results) and self.figures["grande_suite"][1]:
            self.figures["grande_suite"][1] = False
            return self.figures["grande_suite"][0]
        else:
            return sum(dice_results)

        
        

    
    def is_brelan(self, dice_results):
        return len(set(dice_results)) <= 3
    
    def is_carre(self, dice_results):
        for value in set(dice_results):
            if dice_results.count(value) >= 4:
                return True
        return False

    def is_full(self, dice_results):
        duplicates_count = [dice_results.count(value) for value in set(dice_results)]
        return sorted(duplicates_count) == [2, 3]

    def is_grande_suite(self, dice_results):
        sorted_dice_results = sorted(dice_results)

        return sorted_dice_results == [1, 2, 3, 4, 5] or sorted_dice_results == [2, 3, 4, 5, 6]


    def is_yams(self, dice_results):
        return len(set(dice_results)) == 1