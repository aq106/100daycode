import traceback
from dateutil import parser
from datetime import datetime
from datetime import timedelta
from calendar import monthrange


def get_next_day(next_day_freq):
    """Gets next day date from string frequency
    """
    if next_day_freq not in ["weekday","everyday"]:
        print("Unsupported daily frequency! Only 'weekday' and 'everyday' supported")
        return None
    today = datetime.utcnow().date()
    next_day = today + timedelta(days=1)
    next_day_name = next_day.strftime("%A")
    if next_day_freq=="weekday" and next_day_name in ["Saturday", "Sunday"]:
        next_day = today + timedelta( (0-today.weekday()) % 7 )#next monday
    return next_day


def get_next_day_of_week(day, today, next_day_check=True):
    """Returns date for next day of week"""
    if day.lower() == "monday" or day.lower() == "mon":
        next_day = today + timedelta( (0-today.weekday()) % 7 )
        if next_day_check and today == next_day:
            next_day = today + timedelta( (6-today.weekday()) % 7 + 1)
        return str(next_day)
    elif day.lower() == "tuesday" or day.lower() == "tue":
        next_day = today + timedelta( (1-today.weekday()) % 7 )
        if next_day_check and today == next_day:
            next_day = today + timedelta( (0-today.weekday()) % 7 + 1)
        return str(next_day)
    elif day.lower() == "wednesday" or day.lower() == "wed":
        next_day = today + timedelta( (2-today.weekday()) % 7 )
        if next_day_check and today == next_day:
            next_day = today + timedelta( (1-today.weekday()) % 7 + 1)
        return str(next_day)
    elif day.lower() == "thursday" or day.lower() == "thu":
        next_day = today + timedelta( (3-today.weekday()) % 7 )
        if next_day_check and today == next_day:
            next_day = today + timedelta( (2-today.weekday()) % 7 + 1)
        return str(next_day)
    elif day.lower() == "friday" or day.lower() == "fri":
        next_day = today + timedelta( (4-today.weekday()) % 7 )
        if next_day_check and today == next_day:
            next_day = today + timedelta( (3-today.weekday()) % 7 + 1)
        return str(next_day)
    elif day.lower() == "saturday" or day.lower() == "sat":
        next_day = today + timedelta( (5-today.weekday()) % 7 )
        if next_day_check and today == next_day:
            next_day = today + timedelta( (4-today.weekday()) % 7 + 1)
        return str(next_day)
    elif day.lower() == "sunday" or day.lower() == "sun":
        next_day = today + timedelta( (6-today.weekday()) % 7 )
        if next_day_check and today == next_day:
            next_day = today + timedelta( (5-today.weekday()) % 7 + 1)
        return str(next_day)
    else:
        print("[DQ_LOGS] Invalid Day Defined in Onboarding Table!")
        return None


def get_first_day_of_next_month(day, given_date):
    """Get first day of month"""
    current_month = int(str(given_date).split('-')[1])
    next_month = 1 if current_month == 12 else current_month + 1
    next_day = get_next_day_of_week(day, given_date)
    month_next_day = int(next_day.split('-')[1])
    while(next_month!=month_next_day):
        next_day = get_next_day_of_week(day, parser.parse(next_day).date())
        month_next_day = int(next_day.split('-')[1])
    return next_day


def get_day_of_month(day):
    """Get first day of month"""
    try:
        day_name = day.split(",")[0]
        day_name = day_name.strip()
        if day_name.lower() != "lastday":
            day_number = int(day.split(",")[1])
    except:
        print("Invalid Day or Number! :", day)
        return None
    current_utc_date_string = str(datetime.utcnow().date())
    if day_name.lower() == "nthday":
        if day_number > 31 or day_number < 1:
            print("Invalid nth day number! :", day_number)
            return None
        current_day_number = int(current_utc_date_string.split('-')[2])
        current_month = int(current_utc_date_string.split('-')[1])
        current_year = int(current_utc_date_string.split('-')[0])
        if day_number >= current_day_number:
            last_day_current_month = monthrange(current_year, current_month)[1]
            day_number = last_day_current_month if day_number > last_day_current_month else day_number
            next_day = "{}-{}-{}".format(str(current_year),str(current_month),str(day_number))
        else:
            next_month = 1 if current_month == 12 else current_month + 1
            next_year = current_year + 1 if next_month == 1 else current_year
            last_day_next_month = monthrange(next_year, next_month)[1]
            day_number = last_day_next_month if day_number > last_day_next_month else day_number
            next_day = "{}-{}-{}".format(str(next_year),str(next_month),str(day_number))
        return next_day
    elif day_name.lower() == "lastday":
        current_month = int(current_utc_date_string.split('-')[1])
        current_year = int(current_utc_date_string.split('-')[0])
        last_day = monthrange(current_year, current_month)[1]
        next_day = "{}-{}-{}".format(str(current_year),str(current_month),str(last_day))
        return next_day
    elif day_name.lower() in ["mon","monday","tue","tuesday","wed","wednesday","thu","thursday","fri","friday","sat","saturday","sun","sunday",]:
        if day_number < 1 or day_number > 4:
            print("Invalid specific week number :", day_number)
            return None
        current_month = int(current_utc_date_string.split('-')[1])
        current_year = int(current_utc_date_string.split('-')[0])
        if current_month == 1:
            previous_month_date = "{}-{}-{}".format(str(current_year-1),'12','28')
        else:
            previous_month_date = "{}-{}-{}".format(str(current_year),str(current_month-1),'28')
        next_day = get_first_day_of_next_month(day_name, parser.parse(previous_month_date).date())
        if day_number > 1:
            for i in range(day_number-1):
                next_day = get_next_day_of_week(day_name, parser.parse(next_day).date())
        current_day_number = int(current_utc_date_string.split('-')[2])
        next_day_number = int(next_day.split('-')[2])
        if next_day_number < current_day_number:
            next_day = get_first_day_of_next_month(day_name, datetime.utcnow().date())
            if day_number > 1:
                for i in range(day_number-1):
                    next_day = get_next_day_of_week(day_name, parser.parse(next_day).date())
        return next_day
    else:
        print("Invalid/Unsupported day name! :", day_name)
        return None


def get_next_quarter_day():
    current_date = datetime.utcnow()
    current_quarter = round((current_date.month - 1) / 3 + 1)
    # first_date = datetime(current_date.year, 3 * current_quarter - 2, 1)
    # last_date = datetime(current_date.year, 3 * current_quarter + 1, 1) + timedelta(days=-1)
    # print(current_quarter)
    # print("First Day of Quarter:", first_date)
    # print("Last Day of Quarter:", last_date)
    next_quarter = current_quarter +1 if current_quarter!=4 else 1
    first_date = datetime(current_date.year, 3 * next_quarter - 2, 1)
    last_date = datetime(current_date.year, 3 * next_quarter + 1, 1) + timedelta(days=-1)
    # print(next_quarter)
    print("First Day of Next Quarter:", first_date)
    print("Last Day of Next Quarter:", last_date)
    return last_date



def validate_frequency_and_get_next_datetime(frequency):
    """Return weekly and monthly frequency"""
    try:
        freq = frequency.lower().strip()
        if freq.startswith("daily;"):
            freqd = freq.replace("daily;", "").strip()
            if ";" in freqd:
                next_day_freq = freqd.split(";")[0].strip()
                time_of_day = freqd.split(";")[1].strip()
                print(f"Day Freq: {next_day_freq}, Time: {time_of_day}")
                next_day_to_receive = get_next_day(next_day_freq)
                if next_day_to_receive is None:
                    print("Please Correct Unsupported Frequency!", frequency)
                    next_datetime_to_receive = None
                else:
                    next_day_to_receive = datetime(year=next_day_to_receive.year, month=next_day_to_receive.month,day=next_day_to_receive.day)
                    print(f"Next Day: {next_day_to_receive}")
                    next_datetime_to_receive = next_day_to_receive + timedelta(minutes=int(time_of_day.split(":")[1].strip()), hours=int(time_of_day.split(":")[0].strip()))
                    print(f"Next Day DateTime: {next_datetime_to_receive}")
                return next_datetime_to_receive
            else:
                next_day_freq = freqd
                print(f"Day Freq: {next_day_freq}")
                next_day_to_receive = get_next_day(next_day_freq)
                if next_day_to_receive is None:
                    print("Please Correct Unsupported Frequency!", frequency)
                    next_datetime_to_receive = None
                else:
                    next_day_to_receive = datetime(year=next_day_to_receive.year, month=next_day_to_receive.month,day=next_day_to_receive.day)
                    print(f"Next Day: {next_day_to_receive}")
                    next_datetime_to_receive = next_day_to_receive + timedelta(minutes=59, hours=23)
                    print(f"Next Day DateTime: {next_datetime_to_receive}")
                return next_datetime_to_receive
        if freq.startswith("weekly;"):
            freqw = freq.replace("weekly;", "").strip()
            if ";" in freqw:
                day_of_week = freqw.split(";")[0].strip()
                time_of_day = freqw.split(";")[1].strip()
                print(f"Week Freq: {day_of_week}, Time: {time_of_day}")
                next_day_to_receive = get_next_day_of_week(day_of_week, datetime.utcnow().date())
                if next_day_to_receive is None:
                    print("Please Correct Unsupported Frequency!", frequency)
                    next_datetime_to_receive = None
                else:
                    next_day_to_receive = parser.parse(next_day_to_receive)
                    print(f"Next Week Day: {next_day_to_receive}")
                    next_datetime_to_receive = next_day_to_receive + timedelta(minutes=int(time_of_day.split(":")[1].strip()), hours=int(time_of_day.split(":")[0].strip()))
                    print(f"Next Week DateTime: {next_datetime_to_receive}")
                return next_datetime_to_receive
            else:
                day_of_week = freqw
                print(f"Week Freq: {day_of_week} No Time")
                next_day_to_receive = get_next_day_of_week(day_of_week, datetime.utcnow().date())
                if next_day_to_receive is None:
                    print("Please Correct Unsupported Frequency!", frequency)
                    next_datetime_to_receive = None
                else:
                    next_day_to_receive = parser.parse(next_day_to_receive)
                    print(f"Next Week Day: {next_day_to_receive}")
                    next_datetime_to_receive = next_day_to_receive + timedelta(minutes=59, hours=23)
                    print(f"Next Week DateTime: {next_datetime_to_receive}")
                return next_datetime_to_receive
        elif freq.startswith("monthly;"):
            freqm = freq.replace("monthly;", "").strip()
            if ";" in freqm:
                day_of_month = freqm.split(";")[0].strip()
                time_of_day = freqm.split(";")[1].strip()
                print(f"Month Freq: {day_of_month}, Time: {time_of_day}")
                next_day_to_receive = get_day_of_month(day_of_month)
                if next_day_to_receive is None:
                    print("Please Correct Unsupported Frequency!", frequency)
                    next_datetime_to_receive = None
                else:
                    next_day_to_receive = parser.parse(next_day_to_receive)
                    print(f"Next Month Day: {next_day_to_receive}")
                    next_datetime_to_receive = next_day_to_receive + timedelta(minutes=int(time_of_day.split(":")[1].strip()), hours=int(time_of_day.split(":")[0].strip()))
                    print(f"Next Month DateTime: {next_datetime_to_receive}")
                return next_datetime_to_receive
            else:
                day_of_month = freqm
                print(f"Month Freq: {day_of_month}, No Time")
                next_day_to_receive = get_day_of_month(day_of_month)
                if next_day_to_receive is None:
                    print("Please Correct Unsupported Frequency!", frequency)
                    next_datetime_to_receive = None
                else:
                    next_day_to_receive = parser.parse(next_day_to_receive)
                    print(f"Next Month Day: {next_day_to_receive}")
                    next_datetime_to_receive = next_day_to_receive + timedelta(minutes=59, hours=23)
                    print(f"Next Month DateTime: {next_datetime_to_receive}")
                return next_datetime_to_receive
        elif freq.startswith("quarterly"):
            # freqq = freq
            # print(f"Quarter Freq: {freqq}")
            # next_datetime_to_receive = datetime.utcnow() + timedelta(hours=2200)
            # print(f"Next Quarter DateTime: {next_datetime_to_receive}")
            # return next_datetime_to_receive
            #freqq = freq.replace("quarterly", "").strip()
            freqq = freq.strip()
            print(f"Quarter Freq: {freqq}")
            if ";" in freqq:
                time_of_day = freqq.split(";")[1].strip()
                next_day_to_receive = get_next_quarter_day()
                next_day_to_receive = datetime(year=next_day_to_receive.year, month=next_day_to_receive.month,day=next_day_to_receive.day)
                next_datetime_to_receive = next_day_to_receive + timedelta(minutes=int(time_of_day.split(":")[1].strip()), hours=int(time_of_day.split(":")[0].strip()))
                print(f"Next Quarter DateTime: {next_datetime_to_receive}")
                return next_datetime_to_receive
            else:
                next_day_to_receive = get_next_quarter_day()
                next_day_to_receive = datetime(year=next_day_to_receive.year, month=next_day_to_receive.month,day=next_day_to_receive.day)
                next_datetime_to_receive = next_day_to_receive + timedelta(minutes=59, hours=23)
                print(f"Next Quarter DateTime: {next_datetime_to_receive}")
                return next_datetime_to_receive
        else:
            print("Unsupported frequency! Not starting with either 'daily;', 'weekly;', 'monthly;', 'quarterly;'")
            return None
    except Exception as e:
        print("Unsupported frequency! ", frequency)
        print(e)
        traceback.print_exc()
        return None



def check_if_file_arrive_on_expected_day(file_time,expected_day):
    pass

def check_if_file_arrive_in_last_quarter(file_time):
    pass

def check_if_file_arrive_in_hours_period(file_time, hours):
    pass

def initialize_frequency_of_given_file():
    pass
#or
def initialize_frequency_of_new_files():
    #join query?
    pass

def expected_datetime_breached():
    return []

def validate_file_frequency():
    pass


# print(datetime.now())
# print(datetime.utcnow())

#get_next_quarter_day()
#print(validate_frequency_and_get_next_datetime("quarterly"))
#print(validate_frequency_and_get_next_datetime("quarterly;02;30"))

# print(validate_frequency_and_get_next_datetime("daily;everyday"))
# print(validate_frequency_and_get_next_datetime("daily;weekday"))
# print(validate_frequency_and_get_next_datetime("daily;everyday;01:30"))
# print(validate_frequency_and_get_next_datetime("daily;weekday;14:50"))

# print(validate_frequency_and_get_next_datetime("weekly;mon"))
# print(validate_frequency_and_get_next_datetime("weekly;tuesday;12:10"))
# print(validate_frequency_and_get_next_datetime("weekly;thu;11:10"))
# print(validate_frequency_and_get_next_datetime("monthly;nthday,12"))
# print(validate_frequency_and_get_next_datetime("monthly;lastday;15:50"))
# print(validate_frequency_and_get_next_datetime("monthly;tue,2;15:50"))
# print(validate_frequency_and_get_next_datetime("monthly;thu,3;15:50"))
# print(validate_frequency_and_get_next_datetime("monthly;thu,1"))

import json

s = "aoa '' ok"

print(s)

print(json.dumps(s))
