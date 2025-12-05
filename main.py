import time_converter
import story


def main_cycle():
    story_worker = story.Story()
    user_input: float
    result: float

    print("Выберите\n"
          "1. Время\n"
          "0. Прочитать историю операций\n"
          "000. Очистить историю")

    choice = input()
    if choice == "1":
        result: int()
        timeConverter = time_converter.TimeConverter()
        print("Введите данные\n"
              "1.сек\n"
              "2.мин\n"
              "3.час")
        choice = input()
        if choice == "back":
            main_cycle()
        if choice == "1":
            print("Введите секунды")
            user_input = float(input())
            print("Выберите:\n"
                  "1. В мин\n"
                  "2. В час")
            choice = input()
            if choice == "back":
                main_cycle()
            if choice == "1":
                result = timeConverter.convert_time(user_input,"сек", "мин")
                story_worker.save_data(user_input, "сек", result, "мин")
            elif choice == "2":
                result = timeConverter.convert_time(user_input, "сек", "час")
                story_worker.save_data(user_input, "сек", result, "час")
            else:
                print("\nОШИБКА\n")


        elif choice == "2":
            print("Введите минуты")
            user_input = float(input(""))
            print("Выберите:\n"
                  "1. В сек\n"
                  "2. В час")
            choice = input()
            if choice == "back":
                main_cycle()
            if choice == "1":
                result = timeConverter.convert_time(user_input,"мин", "сек")
                story_worker.save_data(user_input, "мин", result, "сек")
            elif choice == "2":
                result = timeConverter.convert_time(user_input, "мин", "час")
                story_worker.save_data(user_input, "мин", result, "час")
            else:
                print("\nОШИБКА\n")
        elif choice == "3":
            print("Введите часы")
            user_input = float(input())
            print("Выберите:\n"
                  "1. В сек\n"
                  "2. В мин")
            choice = input()
            if choice == "back":
                main_cycle()
            if choice == "1":
                result = timeConverter.convert_time(user_input,"час", "сек")
                story_worker.save_data(user_input, "час", result, "сек")
            elif choice == "2":
                result = timeConverter.convert_time(user_input, "час", "мин")
                story_worker.save_data(user_input, "час", result, "мин")
            else:
                print("\nОШИБКА\n")

    elif choice == "0":
        print("История операций:\n")
        story_worker.read_data()
        print("\n")
        main_cycle()
    elif choice == "000":
        story_worker.delete_story()
        print("История очищена\n")
        main_cycle()

    elif choice == "back":
        main_cycle()

    else:
        print("\nОШИБКА\n")
        main_cycle()

    print(f"Результат: {result}")

    main_cycle()


print("Конвертер единиц")
main_cycle()