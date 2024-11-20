INVITATION_FORMAT = "<div><h2>{event_name}</h2><p>{description_of_event}</p><p><strong>Date:</strong> {date_of_event}</p><p>{notes_for_event}</p></div>"

def create_invitation_for_event(event_name: str, description_of_event: str, date_of_event: str, notes_for_event: str):
    return INVITATION_FORMAT.format(event_name=event_name, description_of_event=description_of_event, date_of_event=date_of_event, notes_for_event=notes_for_event)