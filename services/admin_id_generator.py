from datetime import datetime

def generate_admin_id() -> str:
    """
    Generate admin ID in the format: ADMIN-4DIGIT_TIMESTAMP
    Example: ADMIN-1234567890
    """
    timestamp = int(datetime.utcnow().timestamp())
    # Get last 4 digits of timestamp
    four_digit_timestamp = str(timestamp)[-4:]
    admin_id = f"ADMIN-{four_digit_timestamp}{timestamp}"
    return admin_id
