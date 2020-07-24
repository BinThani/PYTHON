def split_and_join(line): # Splits a string into a list, then to a string but space is replaced with "-"
    line = line.split()
    line = "-".join(line)
    return line

txt = input(" ")
print(split_and_join(txt))
