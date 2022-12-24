
import numpy as np

def get_grid(filename):
    with open(filename) as f:
        grid_i=(
            f.read()
            .strip()
            .split("\n"))
        grid_character=list(map(lambda x: list(x),grid_i))
        grid=np.array(grid_character).astype(int)
    return grid

def check_vertical(grid,len_i,i,j):
    if all(grid[i,j]>grid[0:i,j]) or all(grid[i,j]>grid[i+1:len_i,j]):
        visible=1
    else:
        visible=0
    return visible

def check_horizontal(grid,len_j,i,j):
    if all(grid[i,j]>grid[i,0:j]) or all(grid[i,j]>grid[i,j+1:len_j]):
        visible=1
    else:
        visible=0
    return visible


def check_visibility(grid):
    len_i,len_j=grid.shape
    total=0
    #for i in range(1,len_i-1):
    #    for j in range(1,len_j-1):
    for idx, _ in np.ndenumerate(grid):
        if (check_vertical(grid,len_i,idx[0],idx[1])==1) or (check_horizontal(grid,len_j,idx[0],idx[1])==1):
            total+= 1
            #print(f"current total is {total} and (i,j) is {i+1} and {j+1}")
        else:
            continue
    print(total)
    total=total+2*len_j+(len_i-2)*2
    return total

def check_horizontal_part2(grid,len_j,i,j):
    #taller=grid[i,j]>grid[i,:]
    taller_l=0
    for idx in range(j-1,-1,-1):
        if grid[i,idx]<grid[i,j]:
            taller_l+=1
        else:
            taller_l+=1
            break
    taller_r=0
    for idx in range(j+1,len_j,1):
        if grid[i,idx]<grid[i,j]:
            taller_r+=1
        else:
            taller_r+=1
            break
    return taller_l,taller_r


def check_vertical_part2(grid,len_i,i,j):
    taller_u=0
    for idx in range(i-1,-1,-1):
        if grid[idx,j]<grid[i,j]:
            taller_u+=1
        else:
            taller_u+=1
            break
    taller_d=0
    for idx in range(i+1,len_i,1):
        if grid[idx,j]<grid[i,j]:
            taller_d+=1
        else:
            taller_d+=1
            break
    return taller_u,taller_d

def count_trees(grid):
    len_i,len_j=grid.shape
    score=0
    #for i in range(1,len_i-1):
    #    for j in range(1,len_j-1):
    for idx, _ in np.ndenumerate(grid):
        taller_l,taller_r=check_horizontal_part2(grid,len_j,idx[0],idx[1])
        taller_u,taller_d=check_vertical_part2(grid,len_i,idx[0],idx[1])
        score2= taller_l*taller_r*taller_u*taller_d
        score=  score2 if score2>score else score
    return score


#if __name__=="__main___":
filename="input_day8.txt"
#filename="input_day8_test.txt"
grid=get_grid(filename)
tot_visible_trees=check_visibility(grid)
print(tot_visible_trees)
#taller_l,taller_r=check_horizontal_part2(grid,5,3,2)
#taller_u,taller_d=check_vertical_part2(grid,5,3,2)
#print(f'horizontal: {taller_l}, {taller_r} and vertical:{taller_u},{taller_d}')
score=count_trees(grid)
print(f'max visibility score is {score}')