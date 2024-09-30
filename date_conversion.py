from datetime import datetime


def convert_date(year, date_time_string):
    date_time_string = f"{year} {date_time_string}"
    date_format1 = "%Y %b %d  %I%p"
    date_format2 = "%Y %b %d  %I:%M%p"
    try:
        return datetime.strptime(date_time_string, date_format2)
    except ValueError:
        return datetime.strptime(date_time_string, date_format1)


if __name__ == "__main__":
    year = 2024
    date_time_string = "Aug 19  11:59pm"
    date_time_strin2 = "Aug 19  11pm"
    print((convert_date(year, date_time_strin2)))
