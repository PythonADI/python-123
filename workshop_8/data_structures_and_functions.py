import datetime


def create_record(temp, date):
    return {
        "temp": temp,
        "date": date
    }


def increase(record):
    return create_record(record["temp"] + 1, record["date"])

temps = [
    create_record(18, datetime.date(2024, 12, 1)),
    create_record(19, datetime.date(2024, 12, 2)),
    create_record(21, datetime.date(2024, 12, 3)),
    create_record(21, datetime.date(2024, 12, 4)),
]

for record in temps:
    # print(record["date"].day - 1)
    # print(record["date"] - datetime.timedelta(weeks=4))
    # print(record["date"].isoformat())
    print(record)

print(increase(temps[0]))

