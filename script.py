INVITATION_FORMAT = "<div><h2>{event_title}</h2><p>{event_description}</p><p><strong>Date:</strong> {event_date}</p><p>{additional_notes}</p></div>"

def render_event_invitation(event_title: str, event_description: str, event_date: str, additional_notes: str):
    return INVITATION_FORMAT.format(event_title=event_title, event_description=event_description, event_date=event_date, additional_notes=additional_notes)