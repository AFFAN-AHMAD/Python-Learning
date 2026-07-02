file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
# g = next(lines)
# print(g)
list_line = (s.rstrip().split(",") for s in lines)
g = next(list_line)
print(g)