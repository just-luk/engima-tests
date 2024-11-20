FORUM_POST_FORMAT = "<h2>{title}</h2><p>{body}</p>{topics}"

def create_forum_post(title: str, body: str, topics: list[str]):
    formatted_topics = "<ul>" + "".join([f"<li>{topic}</li>" for topic in topics]) + "</ul>"
    return FORUM_POST_FORMAT.format(title=title, body=body, topics=formatted_topics)