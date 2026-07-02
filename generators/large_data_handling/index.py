"""
Let’s think of a strategy:

Read every line of the file.
Split each line into a list of values.
Extract the column names.
Use the column names and lists to create a dictionary.
Filter out the rounds you aren’t interested in.
Calculate the total and average values for the rounds you are interested in.

"""
file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
# g = next(lines)
# print(g)
list_line = (s.rstrip().split(",") for s in lines)
# g = next(list_line)
# print(g)

cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
# g = next(company_dicts)
# print(g)
# # print(g)

funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
g = next(funding)
print(g)

total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")