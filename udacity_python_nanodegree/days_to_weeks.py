# Write your code for readable_timedelta here.

def readable_timedelta(days):
    """Print the number of weeks and days in a number of days."""
    weeks = days//7
    remainder = days%7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

# Uncomment this function call to test it:
print(readable_timedelta(10))
