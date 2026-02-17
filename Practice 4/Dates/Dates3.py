from datetime import datetime

now = datetime.now()
print("Original datetime:", now)

no_microseconds = now.replace(microsecond=0)
print("Datetime without microseconds:", no_microseconds)
