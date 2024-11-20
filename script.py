html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

def build_html_page(page_content: str) -> str:
    return html_template.format(user_content=page_content)