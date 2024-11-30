import colorgram
color=colorgram.extract("image.jpg",7)
# print(color)
'''loc=[]
for i in color:
    loc.append(i.rgb)
print(loc)'''
loc=[]
for i in color:
    R=i.rgb.r
    G=i.rgb.g
    B=i.rgb.b
    tup=(R,G,B)
    loc.append(tup)
print(loc)