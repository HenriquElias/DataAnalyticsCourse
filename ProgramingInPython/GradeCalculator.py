# inputs
fullname = input('Your full name: ')
score1 = float(input('Score 1(out of 100): '))
score2 = float(input('Score 2(out of 100): '))
score3 = float(input('Score 3(out of 100): '))
attendance = float(input('Your attendance(%): '))

# average and GPA
average = (score1+score2+score3)/3
gpa = (4*average)/100

# string only with initials
namelist = fullname.split(' ')
initiallist = [initial[0] for initial in namelist]
initials = '.'.join(initiallist).upper()

#second name
secondname = namelist[1].capitalize()

# check if there's only letters in the string name
checkchar = [i.isalpha() for i in namelist] # Boolean list. If one of the names contains numeric or special characters, return False

if all(checkchar): # Run if name there's only letters, otherwise discontinue the program
    if (score1 < 0 or score1 > 100) or (score2 < 0 or score2 > 100) or (score3 < 0 or score3 > 100): # check if scores are valid numbers
        print('Invalid score!!!') 
    elif (attendance < 0 or attendance > 100): # check if attendance is valid
        print('Invalid attendance!!!')
    else: # if inputs are correct, run!
        print('Your average score is: ',average)
        print('Your initials: ',initials)
        print('Second Name: ',secondname)
        print('Student GPA: ', round(gpa, 2))

        
        if (attendance < 75):
            print('Grade F. Your attendance is too low!')
        elif (average < 40):
            print('Grade F. You need to study more!')
        elif (average >= 40) and (average < 55):
            print('Grade D')
        elif (average >= 55) and (average < 70):
            print('Grade C')
        elif (average >= 70) and (average < 85):
            print('Grade B')
        elif (average >= 85) and (average <= 100):
            print('Grade A. Congratulations!')
        else:
            print('Your score is not valid!')
else:
    print('Your name should consist only of letters!!!')