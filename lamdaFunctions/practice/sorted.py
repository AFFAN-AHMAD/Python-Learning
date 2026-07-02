lists= [(1,'b'), (2,'a'), (3,'c')]

sortedData = sorted(lists, key=lambda x: x[1])
print(sortedData)