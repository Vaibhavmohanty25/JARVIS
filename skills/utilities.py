from datetime import datetime 
def get_time():
    current_time = datetime.now().strftime("%I:%M:%p")
    return f"The current time is {current_time}"

def get_date():
    current_date = datetime.now().strftime("%A, %d %B %Y")
    return f"Today's date is {current_date}"