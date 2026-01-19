from sqlalchemy import func
from sqlalchemy.orm import Session
from models.help_center.help_center_models import HelpCenter


def generate_report_id(db: Session) -> str:
    """Generate report id in pattern REPORT-<last two digits of incremented no>.

    Uses the max HelpCenter.id to determine the next number, then takes
    the last two digits (zero-padded).
    """
    max_id = db.query(func.max(HelpCenter.id)).scalar() or 0
    next_num = int(max_id) + 1
    last_two = str(next_num % 100).zfill(2)
    return f"REPORT-{last_two}"
