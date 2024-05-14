from schedule import Schedule
from discipline import Discipline
from workwithxml import schedule_to_xml, xml_to_schedule
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

# Приклад використання:
schedule_from_xml = xml_to_schedule("schedule.xml")
schedule_from_xml.printSchedule()

schedule_to_xml(newSchedule,"schedule1.xml" )