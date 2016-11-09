from datetime import datetime
now = datetime.now()
if now.hour >= 12:
    print ('%s/%s/%s '%(now.month, now.day, now.year) +
           '%s:%s:%s' %(now.hour%12,now.minute,now.second))
    
else:
    print ('%s/%s/%s '%(now.month, now.day, now.year) +
           '%s:%s:%s' %(now.hour,now.minute,now.second))
    


