print "Ernest Pobee\n"
first_name = raw_input("Enter your first name:")
first_name = str(first_name)
last_name = raw_input("Enter your last name:")
last_name = str(last_name)
print "Please Enter digit for month you were born\n"
print "January - 11\nFebruary -12\nMarch - 1\nApril - 2\nMay - 3\nJune - 4\nJuly - 5\nAugust - 6"
print "September - 7\nOctober - 8\nNovember - 9\nDecember - 10"
A = raw_input()
A  = int(A)
B = raw_input("Please Enter day of the month(1.2.3,...31):")
B = int(B)
C= raw_input("Please Enter the year of the century, eg, 89 for 1989:")
C = int(C)
D = raw_input("Please enter the century, eg 19 for 1989:")
D =int(D)

# if the user selects either 11 or 12 the year is decreased by 1

if (A) > 10:
     C = C-1
################################
W = (13*A - 1) / 5
X  =  C/4
Y  =  D/4
Z  = W + X + Y + B + C - 2*D


R = Z % 7
# if R is a negative number, add 7 to R to get a positive integer between 0 and 6
if (R) < 0:
     R = R + 7
#Assign the name of the day to a variable based on value of R
if (R) == 0:
     day_name = "Sunday";
elif  (R) == 1:
     day_name = "Monday"
elif (R) == 2:
     day_name = "Tuesday"
elif (R) == 3:
     day_name = "Wednesday"
elif (R) == 4:
     day_name = "Thursday"
elif (R) == 5:
     day_name = "Friday"
elif (R) == 6:
     day_name = "Saturday"

#              OUTPUT MESSAGE

print first_name," ",last_name, " was born on a ",day_name
