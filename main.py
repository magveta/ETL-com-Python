import pandas

data = pandas.read_csv("homes.csv")

sell = data['Sell'].tolist()
average_sell = sum(sell)/len(sell)
low_sell = min(sell)
high_sell = max(sell)

with open('load.txt', 'w') as load:
    load.write(f"O preço médio das casas é {average_sell} mil dólares.\n")
    load.write(f"O menor preço das casas é {low_sell} mil dólares.\n")
    load.write(f"O maior preço das casas é {high_sell} mil dólares.\n")