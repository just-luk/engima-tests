USER_POST_FORMAT = "<h1>{title}</h1><h3>Posted by {writer_name}</h3><div>{body}</div><div>{tags_html}</div>"

def generate_post_html(writer_name: str, title: str, body: str, tag_list: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in tag_list])
    return USER_POST_FORMAT.format(writer_name=writer_name, title=title, body=body, tags_html=tags_html)