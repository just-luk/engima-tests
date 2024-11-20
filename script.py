BLOG_FORMAT = "<h1>{title}</h1><p>{body}</p>"

def render_blog_post(title: str, body: str):
    return BLOG_FORMAT.format(title=title, body=body)