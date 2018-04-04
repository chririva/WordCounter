
# CHRISTIAN RIVA

rows=0;
words=0;
characters=0;
f = open('input_file.txt', 'r')

row=f.readline()
while row != "":
    row = row.replace('\n', '')
    characters=characters+len(row)
    rows=rows+1
    words=words+len(row.split())
    row = f.readline()

f.close()

print("Row: "+str(rows))
print("Words: "+str(words))
print("Characters: "+str(characters))
