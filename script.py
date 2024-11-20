FORUM_POST_FORMAT = "<h2>{header}</h2><p>{message}</p>{options}"

def build_post_html(topic_title: str, body_text: str, list_items: list[str]):
    formatted_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
    return FORUM_POST_FORMAT.format(header=topic_title, message=body_text, options=formatted_list)