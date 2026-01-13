import time

def generate_student_id(created_at=None):
	"""
	Generate a student ID in the pattern: STUDENT + last three digits of timestamp (created_at or now)
	"""
	if created_at is None:
		ts = int(time.time())
	else:
		ts = int(created_at.timestamp())
	return f"STUDENT{str(ts)[-3:]}"
