from schedule import Schedule
from discipline import Discipline
from workwithxml import schedule_to_xml, xml_to_schedule, validate_xml_with_xsd
import os

class Menu:
    @staticmethod
    def example_scenario():
        newSchedule = Schedule()
        newSchedule.addDiscipline(Discipline(1, "Математика", "Іванов", 5, "50"))
        newSchedule.addDiscipline(Discipline(2, "Фізика", "Петров", 4, "56"))
        newSchedule.addDiscipline(Discipline(3, "Хімія", "Сидорова", 3, "12"))
        newSchedule.addDiscipline(Discipline(4, "Біологія", "Ковальчук", 3, "34"))
        newSchedule.addDiscipline(Discipline(5, "Історія", "Шевченко", 2, "45"))
        newSchedule.addDisciplineToDay("Понеділок", newSchedule.getDisciplineById(1))
        newSchedule.addDisciplineToDay("Понеділок", newSchedule.getDisciplineById(4))
        newSchedule.addDisciplineToDay("Вівторок", newSchedule.getDisciplineById(2))
        newSchedule.addDisciplineToDay("Вівторок", newSchedule.getDisciplineById(5))
        newSchedule.addDisciplineToDay("Середа", newSchedule.getDisciplineById(3))
        newSchedule.addDisciplineToDay("Середа", newSchedule.getDisciplineById(1))
        newSchedule.addDisciplineToDay("Середа", newSchedule.getDisciplineById(2))
        newSchedule.addDisciplineToDay("Четвер", newSchedule.getDisciplineById(2))  
        newSchedule.addDisciplineToDay("Четвер", newSchedule.getDisciplineById(4))  
        newSchedule.addDisciplineToDay("П'ятниця", newSchedule.getDisciplineById(3))
        newSchedule.addDisciplineToDay("П'ятниця", newSchedule.getDisciplineById(5))
        newSchedule.printSchedule()
        schedule_from_xml = xml_to_schedule("./xml/schedule.xml")
        schedule_from_xml.printSchedule()
        schedule_to_xml(newSchedule,"./xml/schedule1.xml" )
        validate_xml_with_xsd('./xml/schedule.xml','./xsd/schedule.xsd')

    @staticmethod
    def __main__():
        while True:
            print("\nМеню:")
            print("1. Створити новий розклад")
            print("2. Завантажити наявний розклад")
            print("3. Вийти з програми")
            action = input("Оберіть опцію (1/2/3): ")

            if action == '1':
                Menu.create_new_schedule()
            elif action == '2':
                Menu.load_schedule()
            elif action == '3':
                print("Програма завершена.")
                break
            else:
                print("Введено неправильний символ. Будь ласка, виберіть опцію зі списку.")

    @staticmethod
    def create_new_schedule():
        newSchedule = Schedule()
        Menu.use_schedule(newSchedule)

    @staticmethod
    def load_schedule():
        files = os.listdir("./xml")
        files_with_index = [(index, file) for index, file in enumerate(files, start=1)]
        print("Вибери який розклад завантажити:")
        for index, file in files_with_index:
            print(f"{index}) {file}")
        try:
            selected_index = int(input())
            selected_file = files[selected_index - 1]
            schedule_from_xml = xml_to_schedule(f"./xml/{selected_file}")
            print("\nВибрано розклад:",selected_file)
            Menu.use_schedule(schedule_from_xml)
        except (ValueError, IndexError):
            print("Неправильний ввід. Будь ласка, виберіть номер зі списку.")
    
    @staticmethod
    def use_schedule(newSchedule):
        while True:
            print("Меню:")
            print("1. Додати дисципліну")
            print("2. Додати дисципліну до дня")
            print("3. Вивести розклад")
            print("4. Зберегти розклад")
            print("5. Повернутись в головне меню(стирає поточний розклад)")
            action = input("Оберіть дію (1/2/3/4/5): ")
            if action == '1':
                try:
                    discipline_id = int(input("Введіть ID дисципліни: "))
                    discipline_name = input("Введіть назву дисципліни: ")
                    teacher_name = input("Введіть ім'я викладача: ")
                    credits = int(input("Введіть кількість кредитів: "))
                    hours = input("Введіть кількість годин: ")
                    newSchedule.addDiscipline(Discipline(discipline_id, discipline_name, teacher_name, credits, hours))
                    print("Додано нову дисципліну")
                except ValueError:
                    print("Помилка: Введені неправильні дані. Будь ласка, введіть числове значення для ID та кількості кредитів.")
                except Exception as e:
                    print(f"Помилка: {e}")
            elif action == '2':
                print("Додавання дисципліни до дня:")
                schedule_days = newSchedule.getDays()
                print("Доступні дні:")
                for idx, day in enumerate(schedule_days, 1):
                    print(f"{idx}. {day}")
                try:
                    day_idx = int(input("Оберіть номер дня (1-7): "))
                    if 1 <= day_idx <= 7:
                        selected_day = schedule_days[day_idx - 1]
                        print(f"Вибрано день: {selected_day}")
                        newSchedule.printAllDisciplines()
                        discipline_id = int(input("Оберіть ID дисципліни: "))
                        selected_discipline = newSchedule.getDisciplineById(discipline_id)
                        newSchedule.addDisciplineToDay(selected_day, selected_discipline)
                        print(f"Додано дисципліну '{selected_discipline.name}' до дня '{selected_day}'.")
                    else:
                        print("Невірно вибраний номер дня.")
                except ValueError:
                    print("Помилка: Введіть ціле число.")
            elif action == '3':
                newSchedule.printSchedule()
            elif action == '4':
                filename = input("Введіть назву розкладу для збереження: ")
                newSchedule.schedule_to_xml('./xml/' + filename + '.xml')
                break
            elif action == '5':
                print("Сесія завершена.")
                break
            else:
                print("Введено не підходящий символ")



#Menu.__main__()
#Menu.example_scenario()