FORUM_POST_FORMAT = "<h2>{headline}</h2><p>{content}</p>{items}"

def build_forum_post(headline: str, content: str, items: list[str]):
    formatted_items = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    return FORUM_POST_FORMAT.format(headline=headline, content=content, items=formatted_items)