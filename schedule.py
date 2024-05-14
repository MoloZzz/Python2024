import xml.etree.ElementTree as ET

class Schedule:
    def __init__(self):
        self.__disciplines = []
        self.__days = {
            "Понеділок": [],
            "Вівторок": [],
            "Середа": [],
            "Четвер": [],
            "П'ятниця": [],
            "Субота": [],
            "Неділя": []
        }

    def getDays(self):
        return list(self.__days.keys())

    def getDisciplinesForDay(self, day):
        if day in self.__days:
            return self.__days[day]
        else:
            print("Day not found in schedule.")
            return []
    
    def addDiscipline(self, discipline):
        self.__disciplines.append(discipline)

    def addDisciplineToDay(self, day, discipline):
        if day in self.__days:
            self.__days[day].append(discipline)
        else:
            print("Day not found in schedule.")

    def countDisciplines(self):
        return len(self.__disciplines)

    def getDisciplineById(self, id):
        for dis in self.__disciplines:
            if dis.id == id:
                return dis

    def getDisciplineByName(self, name):
        for dis in self.__disciplines:
            if dis.name == name:
                return dis
    def deleteDiscipline(self, id):
        for dis in self.__disciplines:
            if dis.id == id:
                self.__disciplines.remove(dis)

    def printSchedule(schedule):
        print("Розклад:")
        for day, disciplines in schedule.__days.items():
            print(f"{day}:")
            for discipline in disciplines:
                print(discipline)
                print("---")
            print()

    def printAllDisciplines(self):
        print("Усі дисципліни:")
        for discipline in self.__disciplines:
            print(discipline)
    
    def schedule_to_xml(self, filename):
        root = ET.Element("Schedule")

        for day, disciplines in self.__days.items():
            day_element = ET.SubElement(root, "Day")
            day_element.set("name", day)

            for discipline in disciplines:
                discipline_element = ET.SubElement(day_element, "Discipline")
                discipline_element.set("id", str(discipline.id))

                name_element = ET.SubElement(discipline_element, "Name")
                name_element.text = discipline.name

                teacher_element = ET.SubElement(discipline_element, "Teacher")
                teacher_element.text = discipline.teacher

                credits_element = ET.SubElement(discipline_element, "Credits")
                credits_element.text = str(discipline.credits)

                hours_element = ET.SubElement(discipline_element, "Hours")
                hours_element.text = discipline.hours

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)