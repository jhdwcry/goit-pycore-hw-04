def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            file = file.readlines()
            total_sum = 0
            num_devs = len(file)

            for line in file:
                name, salary = line.strip().split(',')
                total_sum += int(salary)

            average_salary = total_sum / num_devs
            return total_sum, average_salary
    
    except FileNotFoundError:
        print(f'File "{path}" is not found')
        return None, None
    

total, average = total_salary("total_salary/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
