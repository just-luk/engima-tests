INVITATION_FORMAT = "<div><h2>{event_title}</h2><p>{event_description}</p><p><strong>Date:</strong> {event_date}</p><p>{additional_notes}</p></div>"

def generate_event_html(title: str, description: str, date: str, extra_notes: str):
    return INVITATION_FORMAT.format(event_title=title, event_description=description, event_date=date, additional_notes=extra_notes)