from datetime import datetime

def generate_course_id() -> str:
    """
    Generate course ID in the format: COURSE{last4digits_timestamp}
    Example: COURSE1234
    """
    timestamp = int(datetime.utcnow().timestamp())
    # Get last 4 digits of timestamp
    four_digit_timestamp = str(timestamp)[-4:]
    course_id = f"COURSE{four_digit_timestamp}"
    return course_id
