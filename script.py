class Patient:
    def __init__(self, id, name, age, gender, diagnosis, treatment_plan):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.treatment_plan = treatment_plan

patients_data = {
    "P001": Patient("P001", "John Doe", 45, "Male", "Hypertension", "Medication and lifestyle changes")
}

def generate_patient_summary(patient_id, report_template):
    if patient_id not in patients_data:
        raise ValueError("Patient not found")
    patient = patients_data[patient_id]
    return report_template.format(patient=patient)