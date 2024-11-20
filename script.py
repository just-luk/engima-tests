USER_POST_FORMAT = "<h1>{title_key}</h1><h3>Posted by {username_key}</h3><div>{body_key}</div><div>{tags_html}</div>"

def render_user_content(username_key: str, title_key: str, body_key: str, tag_elements: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in tag_elements])
    return USER_POST_FORMAT.format(username_key=username_key, title_key=title_key, body_key=body_key, tags_html=tags_html)