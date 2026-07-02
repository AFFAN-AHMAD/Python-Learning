employee_file = open('./employee.txt', 'r+')
print(employee_file.read())
employee_file.write('\nVijay - Operations')
employee_file.close()