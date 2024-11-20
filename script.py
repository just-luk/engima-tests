BLOG_FORMAT = "<h1>{post_title}</h1><p>{post_body}</p>"

def format_post_content(post_title: str, post_body: str):
    return BLOG_FORMAT.format(post_title=post_title, post_body=post_body)