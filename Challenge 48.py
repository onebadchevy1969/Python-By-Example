y_n = input('Would you like to invite someone to the party?: ')
party_people = 0
while y_n.lower() == 'y':
    answer = input('Who would you like to invite to the party?: ')
    print('Ok, I have invited ' + answer + ' to the party. ')
    party_people = party_people + 1
    y_n = input('Would you like to invite someone to the party?: ')

print('There are ' + str(party_people) + ' going to the party! ')
