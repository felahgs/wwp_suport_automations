import time, sys, os, re, datetime

class dateChecker():
    def daterange(self, date1, date2):
        for n in range(int ((date2 - date1).days)+1):
            yield date1 + datetime.timedelta(n)

    def get_days_beetween(self, date1, date2):
        days = []
        for dt in self.daterange(date1, date2):
            # print(dt.strftime("%d/%m/%y"))
            days.append(dt.strftime("%d/%m/%Y"))
        return days

    def convert_to_date(self, date):
        dd = int(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%d'))
        mm = int(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m'))
        yyyy = int(datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%Y'))
        return datetime.date(yyyy,mm,dd)
