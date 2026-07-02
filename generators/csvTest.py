def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result





def csv_gen_reader(file_name):
    for row in open(file_name):
        yield row
csv_gen = csv_gen_reader('test.csv')



# csv_gen = csv_reader("test.csv")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")



letters = ["a", "b", "c", "y"]
it = iter(letters)
while True:
    try:
       letter = next(it)
    except StopIteration:
       break
    print(letter)