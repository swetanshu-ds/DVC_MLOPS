with open("artifact1.txt","r") as f:
    text = f.read()
    
    
with open("artifact1.txt","w") as f:
    text = f.write(text + "i have added one line")
print(text)

print("It is a end of stage 03.")