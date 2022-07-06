with open("note.txt", "r") as fp:
    lines = fp.readlines()
    first = lines[0].split('/n')[0]
    end = lines[-1].split('/n')[0]

    print(first)
    print(end)

sep = '    '
first = first.split(sep, 1)[0]
end = end.split(sep, 1)[0]

print(first)
print(end)
