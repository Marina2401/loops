def clean_string(s):
    i = 0
    while i < len(s):
        if s[i] == '#':
            if i == 0:
                s = s[1:]
            else:
                s = s[:i-1] + s[i+1:]
                i -= 1
        else:
            i += 1
    return s

print(clean_string('#ab#c#d'))