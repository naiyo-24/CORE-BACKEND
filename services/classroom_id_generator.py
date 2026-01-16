from datetime import datetime

def generate_classroom_id(created_at: datetime) -> str:
    """
    Generate a classroom ID in the format CLASS-XXX where XXX are the last three digits of the timestamp.
    created_at: datetime object
    """
    timestamp = int(created_at.timestamp())
    last_three = str(timestamp)[-3:]
    return f"CLASS-{last_three}"
