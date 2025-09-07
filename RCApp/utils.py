from datetime import date, datetime
import pytz

def add_time_stamp():
    
    # Define the date
    date_today = date.today()
    date_str = date_today.isoformat()

    # Get the current time in the specified timezone
    timezone = pytz.timezone('Asia/Karachi')
    current_time_str = datetime.now(timezone).strftime("%H:%M:%S")

    # Concatenating Date and Time for TimeStamp
    dt_stamp_msg = f" EVENT --- [{date_str} | {current_time_str}] --> "

    return dt_stamp_msg