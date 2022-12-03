with open('input.txt') as f:
    data=f.readlines()
a=0
count=0
for i in data:
    if (i=="A X\n"):       #rock rock 3+1
        a = a + 4
    if (i=="A Y\n"):       #rock paper 6+2 
        a = a + 8
    if (i=="A Z\n"):       #rock scissor 0+3
        a = a + 3
    if (i=="B X\n"):       #paper rock 0+1
        a = a + 1
    if (i=="B Y\n"):       #paper paper 3+2 
        a = a + 5
    if (i=="B Z\n"):       #paper scissor 6+3
        a = a + 9
    if (i=="C X\n"):       #scissor rock 6+1
        a  = a + 7
    if (i=="C Y\n"):       #scissor paper 0+2
        a = a + 2
    if (i=="C Z\n"):       #scissor scissor 3+3
        a = a + 6          
    count += 1
    print(str(count)+" "+str(a))    
print(a)