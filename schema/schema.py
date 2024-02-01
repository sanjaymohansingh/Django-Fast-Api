def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "company_id": todo["company_id"],
        "url": todo["url"],
        "events": todo["events"],
        "is_active": todo["is_active"],
        "created_at": todo["created_at"],
        "updated_at": todo["updated_at"],
    }

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]