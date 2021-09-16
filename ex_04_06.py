def computepay(h, r):
    return h*r if h < 40 else 40*r + (h-40) * (1.5 * r)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    fhrs = float(hrs)
except:
    print("Please enter numeric input for hours, please restart.")

try:
    frate = float(rate)
except:
    print("Please enter numeric input for hours, please restart.")
    
p = computepay(fhrs, frate)

print("Pay", p)
