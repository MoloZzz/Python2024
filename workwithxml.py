import xml.etree.ElementTree as ET
from schedule import Schedule
from discipline import Discipline

def xml_to_schedule(file_path):
    schedule = Schedule()
    tree = ET.parse(file_path)
    root = tree.getroot()

    for day_element in root.findall("Day"):
        day_name = day_element.get("name")
        for discipline_element in day_element.findall("Discipline"):
            discipline_id = int(discipline_element.get("id"))
            name = discipline_element.find("Name").text
            teacher = discipline_element.find("Teacher").text
            credits = int(discipline_element.find("Credits").text)
            hours = discipline_element.find("Hours").text
            discipline = Discipline(discipline_id, name, teacher, credits, hours)
            schedule.addDisciplineToDay(day_name, discipline)

    return schedule

def schedule_to_xml(schedule,filename):
    root = ET.Element("Schedule")

    # Отримуємо список днів тижня
    days = schedule.getDays()

    for day in days:
        # Отримуємо дисципліни для поточного дня
        disciplines = schedule.getDisciplinesForDay(day)
        
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
