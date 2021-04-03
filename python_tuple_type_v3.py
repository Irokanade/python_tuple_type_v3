input = str(input("enter a list: "))
input = input.strip('][')
a = input.split(',')
print(a)


for i in range(len(a)):
    print(a[i])
    try:
        x = complex(a[i])
        if x.imag != 0:
            a[i] = x
        elif x.imag == 0:
            try:
                x = float(a[i])
                if x.is_integer():
                    x = int(a[i])
                    a[i] = x
                else:
                    a[i] = x
                    
            except:
                continue
    except:
        x = str(a[i])
        x = x.strip(" '")
        a[i] = x

print(a)