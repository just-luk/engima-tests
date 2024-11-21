USER_POST_FORMAT = "<h1>{post_title}</h1><h3>Posted by {author_name}</h3><div>{content}</div><div>{tags_html}</div>"

def create_post_html(author_name: str, post_title: str, content: str, post_tags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in post_tags])
    return USER_POST_FORMAT.format(author_name=author_name, post_title=post_title, content=content, tags_html=tags_html)