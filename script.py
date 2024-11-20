FORUM_POST_FORMAT = "<h2>{title}</h2><p>{body}</p>{points}"

def create_forum_entry(title: str, body: str, points: list[str]):
    formatted_points = "<ul>" + "".join([f"<li>{point}</li>" for point in points]) + "</ul>"
    return FORUM_POST_FORMAT.format(title=title, body=body, points=formatted_points)