import datetime

class ObservatoryRecord:
    def __init__(self, temp, date):
        # method, initialize / constructor
        # this function is responsible to create an instance / object of a class
        self.temp = temp
        self.date = date

    def display_info(self):
        print(self.date, "/", self.temp)


# instance / object
record = ObservatoryRecord(19, datetime.date(2024, 12, 1))
recrod2 = ObservatoryRecord(21, datetime.date(2024, 12, 2))

# print(record.date, record.temp)
# print(recrod2.date, recrod2.temp)
record.display_info()
recrod2.display_info()
