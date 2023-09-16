s = "20,46,75,10"
marks = s.split(',')
results = []
for i in marks:
    if int(i) >= 35:
        results.append("Pass")
    else:
        results.append("Fail")
print(results)