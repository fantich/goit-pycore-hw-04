from pathlib import Path

def total_salary(path):
    try:
        salaries = []
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  

                try:
                    _, salary = line.split(",")  
                    salaries.append(int(salary))  
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")  
                    continue  

        if salaries:
            total = sum(salaries)
            average = total // len(salaries)  
            return total, average
        else:
            return 0, 0  

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None  

path = Path("Salary.txt")

total, average = total_salary(path)

if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")