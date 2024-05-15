
lines = []
with open('./data/Balanced_AHR.csv', 'r') as f:
    # Read lines
    lines = f.readlines()
    for i in range(len(lines)):
        # If the line starts with ",
        if lines[i].startswith('",'):
            # Remove \n from the previous line
            lines[i-1] = lines[i-1].rstrip('\n')

# Write the lines back to the file
with open('./data/Balanced_AHR.csv', 'w') as f:
    f.writelines(lines)
