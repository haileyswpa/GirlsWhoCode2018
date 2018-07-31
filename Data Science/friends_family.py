framily = {
"Hannah":19,
"Mom":47,
"Dad":51,
"Kendra":16,
"Erin":16,
"Sydney":15,
"Jenny":17
}

avg = 0

for key,value in sorted (framily.items()):
    avg += value
    print(avg)

avg = float(avg / len(framily))
print (avg)
