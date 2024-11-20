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

def modify_project_settings(user_id: str, user_role: str, project_id: str, new_settings: dict):
    # Check if the project exists
    if project_id not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[project_id]["settings"].update(new_settings)
    return f"Project settings for {project_id} have been updated successfully"