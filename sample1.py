from turtle import*
colors=['red','purple','blue','green','yellow','orange']
for x in range(160):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)
    
             
