from csv import writer

newEntry=['Andrew Earlwood','2012-02-14',80000.0,14]

with open ('hrdata_modified.csv', 'a') as employee_file:
    employee_writer = writer(employee_file)
    employee_writer.writenow(newEntry)

    employee_file.close()