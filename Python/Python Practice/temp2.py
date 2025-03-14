
value = []
items=['0100','0011','1010','1001','1111','0101']
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

#print(','.join(value))

items=['0100','0011','1010','1001','1111','0101']

intp = int('0010',2)

print(intp)
print(format(intp,'08b'))
