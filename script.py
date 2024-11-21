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

def alter_project_preferences(member_id: str, member_role: str, proj_id: str, fresh_settings: dict):
    # Check if the project exists
    if proj_id not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[proj_id]["settings"].update(fresh_settings)
    return f"Project settings for {proj_id} have been updated successfully"