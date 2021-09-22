import calendar
y = int(input("Enter the year"))
m=1

print("\n***********CALENDER*************")
Cal = calendar.TextCalendar(calendar.SUNDAY)

#an instance of text calender class is created and calender. SUNDAY means
#that you want to start displaying calender from Sunday.


i=1
while i<=12:
    Cal.prmonth(y,i)
    i+= 1
#prmonth() is a function that prints the calender
#for given month and year


    
      
      
