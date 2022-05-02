class Doctor:
    def __init__(self, name, speciality, qualifications, experience, patients):
        self.name = name
        self.speciality = speciality
        self.patients = patients
        self.experience = experience
        self.qualifications = qualifications
    
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
if __name__ == "__main__":
    Samarth = Doctor('Samarth Pyati', 'Neurologist',['MBBS', 'B.Sc'], 15, [])
    


