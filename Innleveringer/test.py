
with open('Personer.dta') as person_fil:
    persons = [line for line in person_fil]


print(persons[-6:-1])