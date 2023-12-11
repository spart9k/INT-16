import resourses

print("В данном проекте выполнено 2 домашних задания.\n"
      "1 задание: Реализована функция title.\n"
      "2 задание: Изменение вида JSON файла.\n"
      "Введите цифру, какое задание вас интересует: ")
number = int(input())
print(number)
print(f"Вы выбрали проверку {number}-го задания.")

if number > 2:
    print("Такого задания не существует :)")
elif number == 1:
    a = resourses.Title2()
else:
    b = resourses.myjson()