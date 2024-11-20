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

def compose_patient_report(patient_uid, report_schema):
    if patient_uid not in patients:
        raise ValueError("Patient not found")
    patient = patients[patient_uid]
    return report_schema.format(patient=patient)