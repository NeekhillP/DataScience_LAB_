# 2. File Processing with Exception Handling
#  Reads numbers from a text file (one number per line)
#  Ignores invalid entries using exception handling
#  Calculates and displays the sum and average of valid numbers


total = 0
count = 0

try:
    with open("q2.txt", "r") as file:
        for line in file:
            try:
                number = float(line.strip())
                total += number
                count += 1
            except ValueError:
                # Ignore invalid lines
                continue

    if count > 0:
        print("Sum:", total)
        print("Average:", total / count)
    else:
        print("No valid numbers found.")

except FileNotFoundError:
    print("File not found.")
