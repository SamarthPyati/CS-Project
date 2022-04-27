class Doctor:
    def __init__(self, name, speciality, qualifications, experience, patients):
        self.name = name
        self.speciality = speciality
        self.patients = patients
        self.experience = experience
        self.qualifications = qualifications
    
    def list_patient(self):
        for i in enumerate(self.patients):
            print(i)

    def doctor_info(self):
        d_name = self.name
        d_speciality = self.speciality
        d_quals = self.qualifications
        d_experience = self.experience
        info = f''' 
        \rName: Dr.{d_name}
        \rSpeciality: {d_speciality}
        \rExperience: {d_experience} years
        \rQualification: {d_quals}
        '''
        return info
        

# Main 
if __name__ == '__main__':

    Samarth = Doctor('Samarth', 'Cardiologist', 'MBBS', 15, ['z','g','h'])
    natassha = Doctor('Natassha', 'Orthopeadist', 'MBBS', 9, ['x','y','z'])
    print(natassha.doctor_info())
    print(Samarth.doctor_info())

    