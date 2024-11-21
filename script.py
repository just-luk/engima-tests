USER_POST_FORMAT = "<h1>{title}</h1><h3>Posted by {author_name}</h3><div>{body_content}</div><div>{tags_html}</div>"

def render_forum_post(author_name: str, title: str, body_content: str, tag_list: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in tag_list])
    return USER_POST_FORMAT.format(author_name=author_name, title=title, body_content=body_content, tags_html=tags_html)