#3.2 With error checking

try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Rate:")
    r = float(rate)
except:
    print "Error, please enter numeric input"
    quit()

pay = float()
if h <=40:
    pay = h * r
else:
    pay = 40 * r  + ((h-40) * r * 1.5)
    
#print hours, rate and pay
print h
print r
print pay
