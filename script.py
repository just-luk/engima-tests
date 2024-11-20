INVITATION_FORMAT = "<div><h2>{event_title}</h2><p>{event_description}</p><p><strong>Date:</strong> {event_date}</p><p>{additional_notes}</p></div>"

def create_event_invitation(e_title: str, e_description: str, e_date: str, e_notes: str):
    return INVITATION_FORMAT.format(event_title=e_title, event_description=e_description, event_date=e_date, additional_notes=e_notes)