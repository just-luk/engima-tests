INVITATION_FORMAT = "<div><h2>{title_of_event}</h2><p>{event_details}</p><p><strong>Date:</strong> {scheduled_date}</p><p>{extra_info}</p></div>"

def create_event_invitation(title_of_event: str, event_details: str, scheduled_date: str, extra_info: str):
    return INVITATION_FORMAT.format(title_of_event=title_of_event, event_details=event_details, scheduled_date=scheduled_date, extra_info=extra_info)