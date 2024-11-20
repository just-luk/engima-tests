html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

def create_html_output(input_text: str) -> str:
    return html_template.format(user_content=input_text)