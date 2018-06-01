from patterns import Pattern

class PatternManagement:
    @staticmethod
    def get_pattern_addition_two():
        pattern_addition = Pattern()
        pattern_addition.text = '{domain1} {property} {nr1} {range1} and {nr2} {range2}.'
        pattern_addition.number_domains = 1
        pattern_addition.number_ranges = 2
        pattern_addition.number_properties = 1
        return pattern_addition

    @staticmethod
    def get_pattern_addition_one():
        pattern_addition = Pattern()
        pattern_addition.text = ' {nr1} of them are added. '
        pattern_addition.number_domains = 0
        pattern_addition.number_ranges = 0
        pattern_addition.number_properties = 0
        return pattern_addition

    @staticmethod
    def get_pattern_subtraction_two():
        pattern_subtraction = Pattern()
        pattern_subtraction.text = ' there are {domain1} that {property} {nr1} {range1}, {nr2} of them disappear.'
        pattern_subtraction.number_domains = 1
        pattern_subtraction.number_ranges = 1
        pattern_subtraction.number_properties = 1
        return pattern_subtraction

    @staticmethod
    def get_pattern_subtraction_one():
        pattern_subtraction = Pattern()
        pattern_subtraction.text = ' and from that amount he removes {nr1} from the total'
        pattern_subtraction.number_domains = 0
        pattern_subtraction.number_ranges = 0
        pattern_subtraction.number_properties = 0
        return pattern_subtraction

    @staticmethod
    def get_pattern_multiplication_two():
        pattern_multiplication = Pattern()
        pattern_multiplication.text = ' There is {domain1} that {property} {nr1} {range1}. If we add {nr2} times the same quantity to {domain1}'
        pattern_multiplication.number_domains = 1
        pattern_multiplication.number_ranges = 1
        pattern_multiplication.number_properties = 1
        return pattern_multiplication

    @staticmethod
    def get_pattern_multiplication_one():
        pattern_multiplication = Pattern()
        pattern_multiplication.text = ' and now, it multiplies all by {nr1}'
        pattern_multiplication.number_domains = 1
        pattern_multiplication.number_ranges = 1
        pattern_multiplication.number_properties = 1
        return pattern_multiplication

    @staticmethod
    def get_pattern_division_two():
        pattern_division = Pattern()
        pattern_division.text = ' there is {domain1} that {property} {nr1} {range1}. If  {domain1} is divided into {nr2}.'
        pattern_division.number_domains = 1
        pattern_division.number_ranges = 1
        pattern_division.number_properties = 1
        return pattern_division

    @staticmethod
    def get_pattern_division_one():
        pattern_division = Pattern()
        pattern_division.text = ' and at the end, he decides to share all to {nr1} friends'
        pattern_division.number_domains = 0
        pattern_division.number_ranges = 0
        pattern_division.number_properties = 0
        return pattern_division

    @staticmethod
    def get_obj_pattern_addition():
        pattern_addition_obj = Pattern()
        pattern_addition_obj.text = ' What is the total now?'
        return  pattern_addition_obj

    @staticmethod
    def get_obj_pattern_subtraction():
        pattern_subtraction_obj = Pattern()
        pattern_subtraction_obj.text = ' How many things are left?'
        return pattern_subtraction_obj











