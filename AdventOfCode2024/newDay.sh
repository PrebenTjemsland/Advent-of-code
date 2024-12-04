#!/bin/bash
YEAR="$(date +%Y)"
DAY="$(date +'%d')"
echo "Creating todays dict and files for $DAY December $YEAR"
mkdir day$DAY && cd $_
cat <<EOF >Task1.py

with open('testData.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()
        line_num += 1
        if not line:
            break

EOF
cat <<EOF >Task2.py

with open('testData.txt') as f:
    line_num = 0
    while True:
        line = f.readline().strip()
        line_num += 1
        if not line:
            break

EOF

DAY_NO_ZEROS="$(echo $DAY | sed 's/^0*//')"
PUZZLE_URL="https://adventofcode.com/${YEAR}/day/${DAY_NO_ZEROS}/input"
PUZZLE_FILE="Dataset.txt"

EXAMPLE_DATA_URL="https://adventofcode.com/${YEAR}/day/${DAY_NO_ZEROS}"

#Session token from AOC in AOC_TOKEN needed
curl "${PUZZLE_URL}" -H "cookie: ${AOC_TOKEN}" -o "${PUZZLE_FILE}" 2>/dev/null
result="$(curl "${EXAMPLE_DATA_URL}")"

parsedResult=`<<< $result sed -e 's/.*<pre><code>\(.*\)<\/code><\/pre>.*/\1/'`
echo "$parsedResult" > TestData.txt

