monthly_gold_rate=[{"month":"January",
                    "gold_rate":3000},
                   {"month":"February",
                    "gold_rate":1000},
                   {"month":"March",
                    "gold_rate":5600},
                   {"month":"April",
                    "gold_rate":2000}]

max=monthly_gold_rate[0]["gold_rate"]
max_month= ""
min=monthly_gold_rate[0]["gold_rate"]
min_month=""
for gold in monthly_gold_rate:
    if gold["gold_rate"]>max:
        max=gold["gold_rate"]
        max_month=gold["month"]
    if gold["gold_rate"]<min:
        min=gold["gold_rate"]
        min_month=gold["month"]

print(f"Maximun gold rate:{max},\tMonth='{max_month}'.")
print(f"Minimum gold rate:{min},\tMonth='{min_month}'.")










