with open("input_day6.txt") as f:
    stream_file=f.read()
#stream_file="mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def start_of_packet(stream):
    ls=[]
    for n,i in enumerate(stream):
        if len(ls)<4:
            ls=ls+list(i)
            ls
        else:
            ls=ls[1:4]+list(i)
        if len(set(ls))==4:
            print(n+1)
            break
    return n+1, i

start_of_packet(stream_file)

def start_of_message(stream):
    ls=[]
    for n,i in enumerate(stream):
        if len(ls)<14:
            ls=ls+list(i)
            ls
        else:
            ls=ls[1:14]+list(i)
        if len(set(ls))==14:
            print(n+1)
            break
    return n+1, i
start_of_message(stream_file)