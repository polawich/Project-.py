in_time = input("in:(xx.xx) ")
out_time = input("out:(xx.xx) ")

def price(in_time, out_time):
    in_hr = int(in_time[0:2])
    in_mn = int(in_time[3:5])
    out_hr = int(out_time[0:2])
    out_mn = int(out_time[3:5])
    total = (out_hr * 60 + out_mn) - (in_hr * 60 + in_mn)
    return total
    if (total) % 60 == 0:
        hr = total // 60
    else:
        hr = total // 60 + 1
    return hr

Time, hr = price(in_time, out_time)
print("total min is",Time)

if Time <= 15:
    print("total price : 0")
if 15 < Time <= 240:
    mon = hr * 10
    print("total parking price", mon )
if 180 < Time <= 360:
    mon = hr * 10
    print("total parking price", mon ) 
else :
    print("total parking hours : 200 ")