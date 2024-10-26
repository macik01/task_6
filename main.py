import string
#Task 6.1
'''letter = input(str("ведіть дві букви через дефіс "))
st_letter , and_leter = letter.split( '-' )
print(st_letter, and_leter)
vs_letter = string.ascii_letters
print(vs_letter)
st_index = vs_letter.index(st_letter)
and_index = vs_letter.index(and_leter)
result = vs_letter[st_index:and_index + 1]
print(result)'''
#task 6.2
seconds = int(input("Введіть кількість секунд - "))
if seconds < 0 or seconds >= 8640000:
    print("Помилка меньше 0 або більше 8640000")
else:
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds = seconds % 60
    day_word = "день" if days == 1 else "дні" if 2 <= days <= 4 else "днів"
    formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(formatted_time)
