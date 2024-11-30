def calculate_love_score(name1,name2):
    c="true"
    d="love"
    t=0
    l=0
    for i in name1:
        if i in c:
            t+=1
        if i in d:
            l+=1
    for i in name2:
        if i in c:
            t+=1
        if i in d:
            l+=1
    print(str(t)+str(l))
calculate_love_score("Angela Yu","Jack Bauer")