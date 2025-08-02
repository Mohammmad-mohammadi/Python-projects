import statistics

print("==== Central Tendency Calculator ====")
user_input = input("Enter a list of numbers separated by a space (e.g: 1 5 7 2 ): ")

numbers = [float(num) for num in user_input.split()]

mean = statistics.mean(numbers)
median = statistics.median(numbers)
modes = statistics.multimode(numbers)

print("\nResults")
print(f"Mean = {mean}")
print(f"Median = {median}")

if len(modes) == 1:
    print(f"Mode : {modes[0]}")
elif len(modes) > 1:
    print(f"Modes : {', '.join(str(m) for m in modes)}")
else:
    print("No modes found")	