class Patient:
    def __init__(
        self,
        name,
        age,
        concern, 
        diagnostics,
        weight,
        height, 
        BMI, 
        patient_file, 
        medications
        ):

        self.name = name 
        self.age = age
        self.concern = concern
        self.diagnostics = diagnostics
        self.weight = weight
        self.height = height 
        self.bmi = BMI
        self.file = patient_file
        self.medications = medications

    
