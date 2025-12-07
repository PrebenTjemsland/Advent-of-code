invalidIdSum = 0


def is_repeating_pattern(currentId):
    s = str(currentId)
    length = len(s)

    # We only need to check patterns up to half the length of the string.
    # (A pattern longer than half cannot repeat to fill the whole string).
    for i in range(1, (length // 2) + 1):

        # Optimization: A pattern can only fit perfectly if the total length
        # is divisible by the pattern length.
        if length % i == 0:
            pattern = s[:i]  # Take the first i characters

            # Logic: If we replace the pattern with nothing, is the result empty?
            if s.replace(pattern, "") == "":
                return True

            # Alternative (slightly faster) logic:
            # repeats_needed = length // i
            # if pattern * repeats_needed == s:
            #     return True

    return False


with open('Dataset.txt') as f:
    line = f.readline().strip()
    ranges = line.split(',')

    for r in ranges:  # Renamed 'range' to 'r' to avoid conflict
        rangeStart, rangeStop = r.split('-')
        currentId = int(rangeStart)

        while currentId <= int(rangeStop):

            if is_repeating_pattern(currentId):
                # print(f"Found Invalid: {currentId}") # Uncomment to see what matches
                invalidIdSum += currentId

            currentId = currentId + 1

print("Sum: ", invalidIdSum)