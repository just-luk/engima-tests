USER_POST_FORMAT = "<h1>{post_heading}</h1><h3>Posted by {user_name}</h3><div>{post_content}</div><div>{tags_html}</div>"

def build_post_html(user_name: str, post_heading: str, post_content: str, post_tags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in post_tags])
    return USER_POST_FORMAT.format(user_name=user_name, post_heading=post_heading, post_content=post_content, tags_html=tags_html)