people = input('How many people do you want to invite?: ')
if int(people) > 10:
    print('Too many people! ')
elif int(people) <= 10:
    for i in range(0, (int(people))):
        person = input('What is the name of the person you would like to invite?: ')
        print(person + ' has been invited')
else:
    print('I do not understand! ')