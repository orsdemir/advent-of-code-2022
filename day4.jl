using Revise

function read_from_txt(filename)
    file=open(filename)
    lines=readlines(file)
    close(file)
    return lines
end

lines=read_from_txt("input_day4.txt")

function split_str(lines)
    return split.(lines,",")
end


splitted=split_str(lines)

function check_bounds(splitted)
    split2=split.(splitted,"-")
    range1=parse.(Float64,split2[1])
    range2=parse.(Float64,split2[2])
    
    max1=reduce((x,y)->max(x,y),range1)
    max2=reduce((x,y)->max(x,y),range2)
    
    min1=reduce((x,y)->min(x,y),range1)
    min2=reduce((x,y)->min(x,y),range2)

    if (max1 >=max2 && min1<=min2 ) || (max1 <=max2 && min1>=min2 )
        return 1
    else
        return 0
    end
    
end


function check_bounds_2(splitted)
    split2=split.(splitted,"-")
    range1=parse.(Float64,split2[1])
    range2=parse.(Float64,split2[2])
    
    #max1=reduce((x,y)->max(x,y),range1)
    #max2=reduce((x,y)->max(x,y),range2)
    max1=maximum(range1)
    max2=maximum(range2)

    min1=minimum(range1)
    min2=minimum(range2)

    if (max1 < min2 || max2<min1 ) 
        return 0
    else
        return 1
    end
    
end


vec=check_bounds.(splitted)

vec2=check_bounds_2.(splitted)

println(sum(vec.==1))

println(sum(vec2.==1))
