from datetime import datetime as dt
from datetime import timedelta as delta


def display_current_datetime():
    current_date = dt.now()
    return(current_date.strftime('%Y-%m-%d %H:%M:%S'))


def calculate_future_date(days):
    current_date = dt.now()
    future_date = current_date + delta(days=days)
    return(future_date.strftime('%Y-%m-%d'))


if __name__ == '__main__':
    print(f'Current date and time: {display_current_datetime()}')
    days = int(input('Enter the number of days to add to the current date: '))
    print(f'Future date: {calculate_future_date(days)}')
    
    
    
