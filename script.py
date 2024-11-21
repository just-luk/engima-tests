class Patient:
    def __init__(self, id, name, age, gender, diagnosis, treatment_plan):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.treatment_plan = treatment_plan

patient_records = {
    "P001": Patient("P001", "John Doe", 45, "Male", "Hypertension", "Medication and lifestyle changes")
}

def build_patient_report(patient_identifier, template_string):
    if patient_identifier not in patient_records:
        raise ValueError("Patient not found")
    patient = patient_records[patient_identifier]
    return template_string.format(patient=patient)