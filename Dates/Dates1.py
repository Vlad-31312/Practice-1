from datetime import datetime, timedelta

now = datetime.now()
print("Current date and time:", now)

five_days_ago = now - timedelta(days=5)
print("Date 5 days ago:", five_days_ago)
