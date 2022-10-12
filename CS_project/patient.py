class Patient:
    def __init__(
        self,
        id, 
        name,
        age,
        gender, 
        concern, 
        diagnostics,
        weight,
        height,  
        medications
        ):

        self.id = id
        self.name = name 
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height 
        self.bmi = weight/(height^2)
        self.concern = concern
        self.diagnostics = diagnostics
        self.medications = medications

