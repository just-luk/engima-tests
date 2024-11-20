USER_POST_FORMAT = "<h1>{title}</h1><h3>Posted by {author}</h3><div>{body}</div><div>{tags_html}</div>"

def generate_post_html(author: str, title: str, body: str, post_tags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in post_tags])
    return USER_POST_FORMAT.format(author=author, title=title, body=body, tags_html=tags_html)