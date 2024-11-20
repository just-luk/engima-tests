FORUM_POST_FORMAT = "<h2>{header}</h2><p>{message}</p>{options}"

def create_forum_post(topic: str, text_body: str, points: list[str]):
    formatted_points = "<ul>" + "".join([f"<li>{point}</li>" for point in points]) + "</ul>"
    return FORUM_POST_FORMAT.format(header=topic, message=text_body, options=formatted_points)