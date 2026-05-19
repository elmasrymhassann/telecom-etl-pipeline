from datetime import datetime


def print_header(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)



def current_time():
    return datetime.now()