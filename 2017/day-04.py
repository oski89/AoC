# Obtain input and store in list #
file = open('input/04.txt')
data = file.read()
phrases = [row.split(" ") for row in data.split("\n")]

#
# Part 1 #
#

# Set a fail counter #
failed_1 = 0

# Loop through rows and words and add seen words to a list #
# If a word in a row is matching a word in "seen", then increment failed and go to next row #
for row in phrases:
    seen_1 = set()
    for word in row:
        if word not in seen_1:
            seen_1.add(word)
        else:
            failed_1 += 1
            break

print("Answer to part 1: ", len(phrases) - failed_1)

#
# Part 2 #
#

# Set a fail counter #
failed_2 = 0

# Loop through rows and words and add seen words (and all anagrams of it) to a list #
# If a word in a row is matching a word in "seen", then increment failed and go to next row #
for row in phrases:
    seen_2 = set()
    for word in row:
        if ''.join(sorted(word)) not in seen_2:
            seen_2.add(''.join(sorted(word)))
        else:
            failed_2 += 1
            break

print("Answer to part 2: ", len(phrases) - failed_2)
