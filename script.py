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

def generate_user_report(patient_id, template):
    if patient_id not in patients:
        raise ValueError("Patient not found")
    patient = patients[patient_id]
    return template.format(patient=patient)