BLOG_FORMAT = "<h1>{subject}</h1><p>{description}</p>"

def publish_blog_article(subject: str, description: str):
    return BLOG_FORMAT.format(subject=subject, description=description)