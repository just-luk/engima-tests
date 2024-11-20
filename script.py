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

def assemble_patient_report(patient_identifier, report_template):
    if patient_identifier not in patients:
        raise ValueError("Patient not found")
    patient = patients[patient_identifier]
    return report_template.format(patient=patient)