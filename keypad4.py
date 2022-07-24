import re
phone_letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def number_to_text(val):
    groups = [match.group() for match in re.finditer(r'(\d)\1*', val)]  #puts the match objects in a list
    four_letters = [7, 9]
    three_letters = [2, 3, 4 , 5, 6, 8]
    result = ""
    for group in groups:
        keynumber = int(group[0])
        count = len(group)
        if count == 5 and keynumber in four_letters:
            result += str(keynumber)
        elif count == 4 and keynumber in three_letters:
            result += str(keynumber)
        else:
            result += phone_letters[keynumber][count - 1]
    return result

keynum = input("enter a number: ")
print(number_to_text(keynum))