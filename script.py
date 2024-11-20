USER_POST_FORMAT = "<h1>{post_title}</h1><h3>Posted by {username}</h3><div>{post_body}</div><div>{tags_html}</div>"

def render_user_post(username: str, post_title: str, post_body: str, tags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in tags])
    return USER_POST_FORMAT.format(username=username, post_title=post_title, post_body=post_body, tags_html=tags_html)