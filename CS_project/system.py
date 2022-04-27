# Patients:
# -> [Name ,age ,concern, diagnostics, weight, height, BMI, patient_file, medications]
# Doctors:
# -> [Name, Speciality, patients, experience, qualifications]

# System:
# Enter data And retrieve data

# Patient will only enter enter and can also retrieve
# Doctors can only retrieve or enter medication 

import time

time_now = time.strftime("%d/%m/%Y - %H:%M:%S", time.localtime())

class files():
    
    def __init__(self, name):
        self.name = name

    def read_file(self):
        with open(f'{self.name}', 'r+') as file:
            for lines in file:
                data = lines
                print(data, end = '')
        return data
    
    def write_file(self, input):
        with open(f'{self.name}', 'a+') as file:
            nfile = file.writelines(input)
            print(f'----------- {time_now} -----------')
            print(nfile)

f1 = files('someshit.txt')
f1.write_file('\nTAKE THIS SERIOUSLY')
f1.read_file()

        
