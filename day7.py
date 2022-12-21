class Node:
    def __init__(self,name,parent):
        self.children=[] #directories
        self.parent=parent
        self.leaves=[] #files
        self.size=0
        self.name=name
    
    def add_leaf(self,filesize):
        self.leaves.append(int(filesize))
    def add_children(self,name):
        self.children.append(Node(name,self))


def read_file(filename):
    with open(filename) as f:
        return f.read()

def parse(input_text):
    terminal=input_text.strip().split('\n')
    for command in terminal:
        match command.split(" "):
            case "$","cd", "/":
                head=Node("/",None)
                current=head
            case "$","ls":
                continue
            case "dir", directory_name:
                current.add_children(directory_name)
            case "$","cd","..":
                current=current.parent
            case "$","cd", directory:
                for child in current.children:
                    if directory == child.name:
                        current=child
                        break            
            case filesize, filename:
                current.add_leaf(filesize)


    return head


def find_dir_size(head):
    current_size=(sum(head.leaves)) if len(head.leaves)>0 else 0
    for node in head.children:
        current_size=current_size+find_dir_size(node)
    head.size=current_size
    return current_size

def find_small_folders(head,size_limit,total):
    total+=head.size if head.size<size_limit else 0
    for node in head.children:
        total=total+find_small_folders(node,size_limit,0)
    return total

def find_del_folder(head,shortfall,current_size):
    current_size = min(head.size,current_size) if head.size>shortfall else current_size
    for node in head.children:
        current_size=find_del_folder(node,shortfall,current_size)
    return current_size

if __name__=="__main__":
    filename="input_day7.txt"
    input_text=read_file(filename)
    head=parse(input_text)
    find_dir_size(head)
    part1=find_small_folders(head,100000,0)
    required_size=70000000-head.size
    part2=find_del_folder(head,30000000-required_size,head.size)
    print(f'part 1 solution: {part1} and part 2 solution: {part2}')