total_pnl = 0
count = 0
max_pnl = 0
min_pnl = 0
profitable_days = []
unprofitable_days = []
count_profit_trades = 0
count_loss_trade = 0
worst_loss = 0
best_win = 0

trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]


# Determine number of total trading days

for trade in trading_pnl:
    count += 1
    # total profit and losses. This is the sumation
    total_pnl += trade

    # Profitable days list
    if trade >= 0:
        profitable_days.append(trade)
    
    elif trade < 0:
        unprofitable_days.append(trade)



# Daily average

average = total_pnl/count
# Daily average profit and loss


# Best win
for profittrade in profitable_days:
    count_profit_trades += 1

    if profittrade > best_win:
        best_win = profittrade

# worst Loss

for losstrade in unprofitable_days:
    count_loss_trade +=1

    if losstrade < worst_loss:
        worst_loss = losstrade

perc_win_rate = round(count_profit_trades / count * 100,2)
perc_loss_rate = round(count_loss_trade /count *100, 2)

print(" -------------Summary Statistics ---------------")
print (f"Number of total of trading days: {count}")
print (f"Number of profitable trading days: {count_profit_trades}")
print (f"Number of Unprofitable trading days: {count_loss_trade}")
print(f"Percentage of winning trades: {perc_win_rate} %")
print(f"Percentage of winning trades: {perc_loss_rate} %")
print("----------------------")
print(f"Profitable trades: {profitable_days}")
print(f"Unprofitable trades: {unprofitable_days}")
print("----------------------")
print(f"Total profit and Losses: {total_pnl}")
print(f"Daily Average: {average}")
print(f"Worst Loss : {worst_loss}")
print(f"Best Win: {best_win}")


def Addtwodigits(num):
    # convert num into string
    string_num = str(num)
    list1 = string_num.split()
    map_object = map(int,list1)
    listofint = list(map_object)
    totals = 0

    #sumation loop
    for digit in listofint:
        totals += digit

    return totals

    
print(Addtwodigits(29))

num = 29
x = [int(a) for a in str(num)]
print (x)