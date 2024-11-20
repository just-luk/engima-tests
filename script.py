PROJECTS_DB = {
    "PROJ001": {
        "project_id": "PROJ001",
        "creator_id": "USER1",
        "members": ["USER1", "USER2", "USER3"],
        "settings": {"visibility": "private", "deadline": "2023-12-31"}
    },
    "PROJ002": {
        "project_id": "PROJ002",
        "creator_id": "USER4",
        "members": ["USER4", "USER5"],
        "settings": {"visibility": "public", "deadline": "2023-10-15"}
    }
}

def edit_project_settings(member_id: str, role: str, project_key: str, updated_configuration: dict):
    # Check if the project exists
    if project_key not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[project_key]["settings"].update(updated_configuration)
    return f"Project settings for {project_key} have been updated successfully"