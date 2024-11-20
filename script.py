FORUM_POST_FORMAT = "<h2>{heading}</h2><p>{content}</p>{choices}"

def construct_forum_content(heading: str, content: str, choices: list[str]):
    formatted_choices = "<ul>" + "".join([f"<li>{choice}</li>" for choice in choices]) + "</ul>"
    return FORUM_POST_FORMAT.format(heading=heading, content=content, choices=formatted_choices)