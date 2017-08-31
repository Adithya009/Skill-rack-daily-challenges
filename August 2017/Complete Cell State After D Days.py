def cellCompete(cells,days):
    a=[0 for x in range(0,8,1)]
    for i in range(days):
        if cells[1]==0:
            a[0]=0
        else:
            a[0]=1
        if cells[6]==0:
            a[7]=0
        else:
            a[7]=1
        for j in range(1,7,1):
            if cells[j-1]!=cells[j+1]:
                a[j]=1 
            else:
                a[j]=0 
        cells=list(a)
    return cells
        
