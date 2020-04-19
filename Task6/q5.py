class Time:
    def __init__(self,hr,min):
        self.hr=hr
        self.min=min
    def addTime(time1,time2):
        time3=Time(0,0)
        time3.hr=time1.hr+time2.hr
        time3.min=time1.min+time2.min
        if time3.min >=60:
            time3.min =time3.min-60
            time3.hr=time3.hr+1
        return time3
    def DisplayTime(self):
        print("Time is :",self.hr,"hour",self.min ,"min")
    def DisplayMinute(self):
        z=((self.hr))*60+(self.min)
        print ("Total Minutes :",z,"minutes" )
x=Time(2,50)
y=Time(1,20)
res=Time.addTime(x,y)
res.DisplayTime()
res.DisplayMinute()

