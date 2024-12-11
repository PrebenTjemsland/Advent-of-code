import math


with open('testData.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()
        line_num += 1
        if not line:
            break
        goal_part, values_part = line.split(':')
        goal = int(goal_part.strip())
        values = list(map(int, values_part.split()))
        values.sort()
        if sum(values) > goal:
            continue
        if math.prod(values) < goal:
            continue
        if sum(values) > goal or math.prod(values) < goal:
            print("Skipping calculation due to initial checks")
        else:
            temp_sum = 0
            for idx in range(len(values) + 1):
                # Compute the partial sums and products
                sum_sum = sum(values[idx:])
                prod_sum = math.prod(values[:idx])
                temp_sum = sum_sum + prod_sum

                # Print the state for debugging to understand inclusion/exclusion
                print(f"idx: {idx}, sum_sum: {sum_sum}, prod_sum: {prod_sum}, temp_sum: {temp_sum}")

                if temp_sum >= goal:
                    break

            print("Final temp_sum:", temp_sum)


