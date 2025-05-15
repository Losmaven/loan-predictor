# backend/log_crypto.py

import hashlib
import csv
from datetime import datetime

def log_action(action, details):
    timestamp = datetime.utcnow().isoformat()
    details_hash = hashlib.sha256(details.encode()).hexdigest()

    with open('logs/audit_log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, action, details_hash])
