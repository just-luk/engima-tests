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

def build_patient_summary(identifier, report_template):
    if identifier not in patients:
        raise ValueError("Patient not found")
    patient = patients[identifier]
    return report_template.format(patient=patient)