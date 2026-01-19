import time

def generate_admission_enquiry_id(created_at=None):
    """
    Generate an enquiry ID in the pattern: ENQ-<last three digits of timestamp>
    If created_at is a datetime, use its timestamp; otherwise use current time.
    """
    if created_at is None:
        ts = int(time.time())
    else:
        try:
            ts = int(created_at.timestamp())
        except Exception:
            ts = int(time.time())
    return f"ENQ-{str(ts)[-3:]}"
