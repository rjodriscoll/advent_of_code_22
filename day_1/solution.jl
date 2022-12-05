data = readchomp("data.txt")

max = 0 
for elfstr = eachsplit(data, "\n\n")
    elfint = parse.(Int, eachsplit(elfstr))
    if sum(elfint) > max 
        max = sum(elfint)
    end
end

println(max)
