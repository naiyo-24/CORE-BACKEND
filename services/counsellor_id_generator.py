from datetime import datetime

def generate_counsellor_id(created_at: datetime):
	"""
	Generate a counsellor ID in the format COUNS-XXX where XXX are the last three digits of the timestamp.
	"""
	timestamp = int(created_at.timestamp())
	last_three = str(timestamp)[-3:]
	return f"COUNS-{last_three}"
