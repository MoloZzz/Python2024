## Lab2 Робота з базою даних
Програма не вимагає створення інтерфейсу
користувача. Тестування працездатності програми
здійснюється на основі сценаріїв, які демонструють
можливості програми.
Відомості про об'єкти зберігаються в таблицях бази
даних. Читання і редагування даних здійснюється за
допомогою запитів SQL.
Характеристики об'єктів, що автоматизуються
визначаються студентом самостійно. Обов'язковою
характеристикою об'єкта є його унікальний ідентифікатор.
Унікальність ідентифікаторів при виконанні операцій
додавання і редагування об'єктів повинна забезпечуватися
засобами СУБД або засобами програми, що розробляється

Програма повинна підтримувати виконання наступних
операцій з даними:
+ додавання нового об'єкта
+ зміна параметрів існуючого об'єкту
+ видалення об'єкта
+ пошук об'єктів по заданим критеріям і
виведення інформації про об'єкти

Запуск міграцій(консоль): 
alembic upgrade head

Створення міграції 
alembic revision -m "Назва міграції"

Алембік в моїй локальній пам'яті 
C:\Users\megao\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\alembic