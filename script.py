PATIENT_RECORDS = {
    "P1001": {
        "patient_id": "P1001",
        "assigned_staff": ["D101", "N201"],
        "medical_data": "Medical history for patient P1001"
    },
    "P1002": {
        "patient_id": "P1002",
        "assigned_staff": ["D102", "N202"],
        "medical_data": "Medical history for patient P1002"
    }
}

def fetch_patient_info(staff_identifier: str, staff_role: str, patient_ref: str):
    # Check if the patient record exists
    if patient_ref not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[patient_ref]["medical_data"]