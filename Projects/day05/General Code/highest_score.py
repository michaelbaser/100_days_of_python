# Sum
# Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total). e.g.

# student_scores = [180, 124, 165, 173, 189, 169, 146]
# total_score = sum(student_scores) 
# But how does sum() work behind the scenes? The code is written by the people who developed Python and it might look something like this:

# student_scores = [180, 124, 165]

# sum = 0
# for score in student_scores:
#     sum += score
    
# print(sum)


student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_exam_score = sum(student_scores)
print(f'Total exam score, "sum(student_scores)" method = {total_exam_score:,}')

sum_var = 0

# Accumulates in this variable to keep adding throughout the list
for score in student_scores:
    sum_var += score
    
print(f'Total exam score, "sum_var" manual for loop method = {sum_var:,}')


    
#------------------
# PAUSE 1 - Max
#------------------

# There are also a built-in Python methods called max() and min(), which allow you to pass in a List of numbers, and it will give you the highest number or the lowest number.

# Your job is to figure out how the Python programmers might have built this functionality using loops and conditionals.

# COMPLETE THIS CHALLENGE WITHOUT USING max()
# You are given a list of exam scores, and you have to print out the highest score from the List. You will need to use what you have learnt about Lists, For Loops and Conditionals to print out the highest score in the list of student_scores. For example, if the scores were:

# 8 65 89 86 55 91 64 89
# Your code should print

# 91

# Can use print to help with reviewing data!
for score in student_scores:
    print(f'This is printing our loop: {score}')
# 8
# 65
# 89
# 86
# 55
# 91
# 64
# 89

print(f'Max result, using "max(exam_scores)" method = {max(student_scores)}')



# variable to hold intermediate values until we reach the max
max_var = 0

# In this example, we initialize the max value to the first element. 
# Then we iterate through the list, and if we find a larger value than the current max, we assign that value to max. 
# At the end, we should have the largest value, which we print.
# https://stackoverflow.com/questions/24235268/max-value-of-list-without-max-method

for score in student_scores:
    if score > max_var:
        max_var = score
        
print(f'Max result, using "max_var" manual for loop method = {max_var}')



