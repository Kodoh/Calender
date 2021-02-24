import time
EventList = []

class Calender:
    def __init__(self,month,day):
        self.month = month
        self.day = day   

class Event(Calender):
    def __init__(self,EventName,StartDate,EndDate,StartTime,EndTime,month,day,EventList = EventList):     
        Calender.__init__(self,month,day)
        self.EventName = EventName
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.StartTime = StartTime
        self.EndTime = EndTime

    def EventClash(self):
        for i in EventList:
            if i.month == self.month:
                clashList = []
                if (i.EndDate >= self.StartDate >= i.StartDate) or (self.EndDate >= i.StartDate >= self.StartDate):                    
                    if i.StartDate == self.StartDate:
                        if (i.EndTime >= self.StartTime >= i.StartTime) or (self.EndTime >= i.StartTime >= self.StartTime):
                            if i != self:
                                clashList.append(i)
                    else:
                        clashList.append(i)
        if len(clashList) != 0:
            print("Your event is clashing with: ")
            for r in clashList:
                print(r.EventName)
        else:
            print("This event is not clashing with any others")
                
    def EventInMonth(self,month):
        MonthList = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
        if month in MonthList:
            for i in EventList:
                if i.month == month:
                    printList = []
                    printList.append(i)
            print(f"Events in {month} - ")
            for x in printList:
                print(x.EventName)
        else:
            print("Invalid Month")

    def EventInTimePeriod(self,TPstart,TPend):
        eventInPeriodList = []
        for i in EventList:
            if (TPend >= i.StartTime >= TPstart) or (i.EndTime >= TPend >= i.StartTime):
                eventInPeriodList.append(i)
        print("Events in given time period -")
        if len(eventInPeriodList) == 0:
            print("No events in given time period")
        else:
            for x in eventInPeriodList:
                print(x.EventName)

Event1 = Event("Birthday", 15, 16, 900, 1000,"January", "Tuesday")          #example of instance called
Event2 = Event("Birthday2", 13, 16, 800, 1700,"January", "Monday")
EventList.append(Event1)
EventList.append(Event2)


"""
t = Event1.EventClash()
if t == None:
    pass
else:                                   #more examples of instances
    print(t)
Event1.EventInMonth("Febuary")
Event1.EventInTimePeriod(900,1600)
"""

