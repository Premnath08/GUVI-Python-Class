l = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    }
]
#Print all the value in the list
print(l)
#print the hex value of green
print(l[1]["value"])
#print the hex codes of all colors
c=len(l)
for i in range(0,c):
 print(l[i]["value"])