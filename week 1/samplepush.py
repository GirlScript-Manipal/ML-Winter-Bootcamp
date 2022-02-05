hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r=float(rate)
if h > 40 :
    r1=float( (r * 1.5) * (h-40))
pay = float(((h-5)*r) + r1)
print (pay)
