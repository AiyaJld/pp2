from datetime import datetime, time

def diff(dt2, dt1):
  dif = dt2 - dt1
  return dif.days * 24 * 3600 + dif.seconds

d1 = datetime.strptime('2019-06-23 15:34:45', '%Y-%m-%d %H:%M:%S')
d2 = datetime.now()

print("\n%d seconds" %(diff(d2, d1)))