import json

class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                students = json.load(file)
        except FileNotFoundError:
            students = []
        return students

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file)

    def add_student(self):
        name = input("Введите имя студента: ")
        surname = input("Введите фамилию студента: ")
        average_grade = float(input("Введите средний бал успеваемости: "))

        student = {
            "Имя": name,
            "Фамилия": surname,
            "Средний балл": average_grade
        }
        self.students.append(student)
        self.save_data()
        print("Студент добавлен успешно.")

    def delete_student(self):
        surname = input("Введите фамилию студента, которого нужно удалить: ")
        students_to_delete = [student for student in self.students if student["Фамилия"] == surname]
        if students_to_delete:
            for student in students_to_delete:
                self.students.remove(student)
            self.save_data()
            print(f"Студент(ов) с фамилией {surname} удален(ы).")
        else:
            print(f"Студент с фамилией {surname} не найден.")

    def view_student_info(self):
        surname = input("Введите фамилию студента, информацию о котором вы хотите просмотреть: ")
        student_to_view = [student for student in self.students if student["Фамилия"] == surname]
        if student_to_view:
            for student in student_to_view:
                print(f"Имя: {student['Имя']}, Фамилия: {student['Фамилия']}, Средний балл: {student['Средний балл']}")
        else:
            print(f"Студент с фамилией {surname} не найден.")

    def show_all_students(self):
        if self.students:
            for student in self.students:
                print(f"Имя: {student['Имя']}, Фамилия: {student['Фамилия']}, Средний балл: {student['Средний балл']}")
        else:
            print("Список студентов пуст.")

    def search_student(self):
        parameter = input("Введите параметр поиска (фамилия, имя и так далее): ")
        value = input(f"Введите значение параметра {parameter}: ")
        found_students = [student for student in self.students if student.get(parameter) == value]
        if found_students:
            for student in found_students:
                print(f"Имя: {student['Имя']}, Фамилия: {student['Фамилия']}, Средний балл: {student['Средний балл']}")
        else:
            print(f"Студент(ы) с {parameter} {value} не найден(ы).")

    def sort_students(self):
        key = input("Введите ключ сортировки (Фамилия, Средний балл и так далее): ")
        sorted_students = sorted(self.students, key=lambda x: x[key])
        for student in sorted_students:
            print(f"Имя: {student['Имя']}, Фамилия: {student['Фамилия']}, Средний балл: {student['Средний балл']}")

    def excellent_students(self):
        excellent = [student for student in self.students if student['Средний балл'] >= 10]
        if excellent:
            for student in excellent:
                print(f"Имя: {student['Имя']}, Фамилия: {student['Фамилия']}, Средний балл: {student['Средний балл']}")
        else:
            print("Отличников не найдено.")

def main():
    manager = StudentManager("students.json")

    while True:
        print("\nМеню:")
        print("1. Добавить студента")
        print("2. Удалить студента")
        print("3. Просмотреть информацию о студенте")
        print("4. Показать всех студентов")
        print("5. Поиск информации о студенте")
        print("6. Вывести студентов в определенном порядке")
        print("7. Вывести 'отличников'")
        print("8. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.delete_student()
        elif choice == "3":
            manager.view_student_info()
        elif choice == "4":
            manager.show_all_students()
        elif choice == "5":
            manager.search_student()
        elif choice == "6":
            manager.sort_students()
        elif choice == "7":
            manager.excellent_students()
        elif choice == "8":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
