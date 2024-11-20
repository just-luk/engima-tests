FORUM_POST_FORMAT = "<h2>{header}</h2><p>{message}</p>{options}"

def build_forum_entry(post_title: str, post_body: str, bullet_points: list[str]):
    formatted_points = "<ul>" + "".join([f"<li>{point}</li>" for point in bullet_points]) + "</ul>"
    return FORUM_POST_FORMAT.format(header=post_title, message=post_body, options=formatted_points)