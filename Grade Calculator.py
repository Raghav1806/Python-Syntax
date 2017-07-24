grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += float(grade)
    return total
    
def grades_average(grades):
    sum_of_grades = float(grades_sum(grades))
    average = float(sum_of_grades/(len(grades)))
    return average

def grades_variance(scores):
    average = float(grades_average(scores))
    variance = 0
    for score in scores:
        variance += float((average - score) ** 2)
    variance = float(variance/len(scores))
    return variance

print grades_variance(grades)   

def grades_std_deviation(variance):
    return variance ** 0.5

print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
variance = grades_variance(grades)
print variance
print grades_std_deviation(variance)
