FORUM_POST_FORMAT = "<h2>{title}</h2><p>{post_body}</p>{options_list}"

def build_forum_post(title: str, post_body: str, options_list: list[str]):
    formatted_options_list = "<ul>" + "".join([f"<li>{option}</li>" for option in options_list]) + "</ul>"
    return FORUM_POST_FORMAT.format(title=title, post_body=post_body, options_list=formatted_options_list)