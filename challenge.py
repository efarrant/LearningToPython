sequence = [4,2,3,1,3,4,1]
print(sequence)
# sequence.sort()
for number in sequence:
    sequence.remove(number)
    if number not in sequence:
        sequence.append(number)
        # sequence.sort()
print(sequence)


sequence = [4,2,3,1,3,4,1]
print(sequence)
sequence = list(set(sequence))
print(sequence)

sequence = [4,2,3,1,3,4,1]
unique_sequence = []
for number in sequence:
    if number not in unique_sequence:
        unique_sequence.append(number)
print(unique_sequence)

sequence = [4,2,3,1,3,4,1]
for number in sequence:
    if sequence.count(number) > 1:
        sequence.remove(number)
print(sequence)