def jaygasht(letters: list, last_string):
    for i in range(len(letters)):
        remaining_letters = letters.copy()
        remaining_letters.pop(i)
        jaygasht(remaining_letters , last_string + str(letters[i]))
    if len(letters) == 0:
        print(last_string)

jaygasht([1,2,3,4],'')
