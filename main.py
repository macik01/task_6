import string
#Task 6.1
letter = input(str("ведіть дві букви через дефіс "))
st_letter , and_leter = letter.split( '-' )
print(st_letter, and_leter)
vs_letter = string.ascii_letters
print(vs_letter)
st_index = vs_letter.index(st_letter)
and_index = vs_letter.index(and_leter)
result = vs_letter[st_index:and_index + 1]
print(result)