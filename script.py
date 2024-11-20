html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

def render_html_page(visitor_message: str) -> str:
    return html_template.format(user_content=visitor_message)