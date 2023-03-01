import datetime
import random


def generate_random_date(start_date, end_date):
    """
        Generate a random date between two given dates.

        Args:
            start_date (datetime.date): The start date of the date range.
            end_date (datetime.date): The end date of the date range.

        Returns:
            A randomly generated date between start_date and end_date (inclusive).
        """
    days_delta = (end_date - start_date).days
    added_days = random.randrange(start=0, stop=days_delta)
    return start_date + datetime.timedelta(days=added_days)


def main():
    date_start_str = str(input("Enter start date in this format: YYYY-MM-DD\n"))
    date_end_str = str(input("Enter end date in this format: YYYY-MM-DD\n"))

    date_start = datetime.datetime.strptime(date_start_str, "%Y-%m-%d")
    date_end = datetime.datetime.strptime(date_end_str, "%Y-%m-%d")

    new_date = generate_random_date(date_start, date_end)

    if new_date.weekday() == 0:  # new date falls on a Monday
        print("אין לי ויניגרט!")


if __name__ == "__main__":
    main()
