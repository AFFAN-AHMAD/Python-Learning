listing = ['asfd','asdfjka','asfasfa','da','rwqfdsaf']
filteredList = filter(lambda x:len(x)>4, listing )
print(list(filteredList))