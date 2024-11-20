FORUM_POST_FORMAT = "<h2>{header}</h2><p>{message}</p>{options}"

def generate_forum_post(header: str, message: str, options: list[str]):
    formatted_options = "<ul>" + "".join([f"<li>{option}</li>" for option in options]) + "</ul>"
    return FORUM_POST_FORMAT.format(header=header, message=message, options=formatted_options)