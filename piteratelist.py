# Initialize the metric variables
count = 0
total = 0
average = 0
minimum = 0
maximum = 0

# List daily tips
cash_tips = [22, 10, 30, 45, 54, 60, 56]

# Showcase every tip in the list
for tip in cash_tips:
    print(tip)

# Iterate over each list element and determine metrics

for tip in cash_tips:
    # Cumulate the total of tips and count how many tips
    total += tip
    count += 1

    # logic to determine min tip value
    if minimum == 0:
        minimum = tip
    elif tip < minimum:
        minimum = tip
    
    # logic for the maximum tip received

    if tip > maximum:
        maximum = tip
    
# Calculate the average tip received
average = round(total/count, 2)


# Print the statistics
print("summary statistics")
print(f"Number of tips: {count}")
print(f"total Tips: {total}")
print(f" Daily average : {average}")
print(f"least amount of tip: {minimum}")
print(f"Maximum tip received: {maximum}")