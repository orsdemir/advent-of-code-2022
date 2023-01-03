def solve(positions):
    steps_t=[(0,0)]
    for row_h, col_h in positions:
        row_t, col_t= steps_t[-1]
        dist_row, dist_col = row_t-row_h, col_t-col_h
               
        if abs(dist_row)>1 or abs(dist_col)>1:
            dir_row = 1 if row_h >= row_t else -1
            dir_col= 1 if col_h >= col_t else -1
            delta_row, delta_col = (dir_row*max(0,abs(row_t-row_h)-1), dir_col*max(0,abs(col_t-col_h)-1)) if dist_row ==0 or dist_col==0 else (dir_row, dir_col)
            steps_t += [(row_t+delta_row, col_t+delta_col)]

    return steps_t

with open("input_day9.txt") as f:
    raw_data=f.read().splitlines()

data=iter([e.split(' ')[0],int(e.split(' ')[1])] for e in raw_data)

pos_head=[(0,0)]
pos_tail=[(0,0)]
walk={'R':(0,1),'L':(0,-1),'U':(1,0),'D':(-1,0)}
steps=[(0,0)]
for dir, dist in data:
    row, col, drow, dcol = *steps[-1], *walk[dir]
    steps += [(row+drow*i,col+dcol*i) for i in range(1,dist+1)]

positions_t=solve(steps)
len(set(positions_t))

# part 2

for i in range(0,9):
    steps=solve(steps)
len(set(steps))