class Patient:
    def __init__(self, id, name, age, gender, diagnosis, treatment_plan):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.treatment_plan = treatment_plan

patients = {
    "P001": Patient("P001", "John Doe", 45, "Male", "Hypertension", "Medication and lifestyle changes")
}

def create_patient_report(pat_id, layout):
    if pat_id not in patients:
        raise ValueError("Patient not found")
    patient = patients[pat_id]
    return layout.format(patient=patient)