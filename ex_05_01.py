num = 0
tot = 0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue
    print(sval)
    num += 1 
    tot += fval
print('ALL DONE')
print(tot, num, tot/num)
