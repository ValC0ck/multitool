import time_converter

print("Конвертер единиц")
print("Выберите\n"
      "1. Время")

if input() == "1":
    timeConverter = time_converter.TimeConverter()
    print("Введите данные\n"
          "1.сек\n"
          "2.мин\n"
          "3.час\n")
    choice = input()
    if choice == "сек":
        

