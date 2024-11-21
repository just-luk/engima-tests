INVITATION_FORMAT = "<div><h2>{event_title}</h2><p>{event_description}</p><p><strong>Date:</strong> {event_date}</p><p>{additional_notes}</p></div>"

def build_event_invitation(title_of_event: str, details_of_event: str, when_event_is: str, extra_event_info: str):
    return INVITATION_FORMAT.format(event_title=title_of_event, event_description=details_of_event, event_date=when_event_is, additional_notes=extra_event_info)