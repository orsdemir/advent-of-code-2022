with open("input_day10.txt") as f:
    raw_data=f.read().splitlines()

data=iter(int(e.split(' ')[1]) if len(e.split(' '))==2 else 0 for e in raw_data)
#crt= range(0,len(list(data)))

# first part
cycle=1
x_val=1
values=[]

for ins in data:
    
    values+= [(cycle,x_val),(cycle+1,x_val)] if ins != 0 else [(cycle,x_val)]
    x_val += ins
    cycle+= 2 if ins != 0 else 1

tot=0
stri=[]
for cyc, val in values:
    if (cyc+20) % 40 ==0:
        tot+= cyc *val
    pos=cyc-1
    stri+= "#" if abs(pos % 40 - val) <= 1 else "."
print(tot)
letters="\n".join("".join(stri)[i:40+i] for i in range(0,len(stri),40))


with open('output_day10.txt', 'w') as f:
    f.write(letters)