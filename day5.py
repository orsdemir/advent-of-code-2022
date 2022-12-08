
import copy

def parse_file(input_file):
    with open(input_file) as f:
        stacks_str,instructions_str=f.read().split("\n\n")
    return stacks_str, instructions_str
    #mapping=list(range(1,34,4))

def convert_to_stacks(stacks_str):
    stacks={}
    for i in range(0,9):
        stacks[i+1]= list(map(lambda x: x[1+4*i],stacks_str.split("\n")))[0:-1]
        stacks[i+1]=list(filter(lambda x: x !=" ",stacks[i+1]))
    return stacks

def get_instructions(instructions_str):
    instructions=[]
    for command in instructions_str.strip().split("\n"):
        _, num, _, start,_,finish =command.split()
        instructions.append(list(map(int,[num,start,finish])))
    return instructions                       

def follow_instructions(stacks,instructions):
    
    stacks1=copy.deepcopy(stacks)
    
    for num, start, end in instructions:
        move_crates=stacks1[start][0:num][::-1]
        stacks1[start]=stacks1[start][num:]
        stacks1[end][0:0]=move_crates
    return stacks1

#{v: temp[0][i] for v,i in enumerate(mapping)}

stacks_str,instructions_str=parse_file("input_day5.txt")

stacks=convert_to_stacks(stacks_str)


instructions = get_instructions(instructions_str)

final_stacks=follow_instructions(stacks,instructions)

"".join([val[0] for (key,val) in final_stacks.items()])