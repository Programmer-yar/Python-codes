def greater(v,x,y,z):
    if v>x:
        max1=v
    else:
        max1=x
    #comaprison between first 2 numbers ends here
    if y>z:
        max2=y
    else:
        max2=z
    #comaprison between second 2 numbers ends here
    if max1>max2:
        return max1
    else:
        return max2
""" now max number out of two groups is comapred here
and result is returned""" #this is a docstring

print(greater(2,5,4,6))
