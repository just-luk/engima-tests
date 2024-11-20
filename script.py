INVITATION_FORMAT = "<div><h2>{headline}</h2><p>{summary}</p><p><strong>Date:</strong> {scheduled_date}</p><p>{additional_info}</p></div>"

def prepare_event_details(headline: str, summary: str, scheduled_date: str, additional_info: str):
    return INVITATION_FORMAT.format(headline=headline, summary=summary, scheduled_date=scheduled_date, additional_info=additional_info)