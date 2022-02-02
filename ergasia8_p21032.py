#TODO look it again
import random
def game(r,c):
    global wpl
    global bpl
    board=[[" 0 "]*r for i in range(c)]
    rook_row=random.randint(1,r-1)
    rook_col=random.randint(1,c-1)
    while True:
        end=False
        bishop_row=random.randint(1,r-1)
        if(bishop_row!=rook_row): #den ginetai na einai stis idies theseis
            end=True
        bishop_col=random.randint(1,c-1)
        if(bishop_col!=rook_col):
            end=True
        if end:
            break
    board[rook_row-1][rook_col-1]=" R " 
    board[bishop_row-1][bishop_col-1]=" B "
    # print("*--------------*")
    # for i in board: 
    #     print(i)
    # print(bishop_row-1,bishop_col-1,"bishop")
    # print(rook_row-1,rook_col-1,"rook")
    # print("*--------------*")
    if bishop_row==rook_row or bishop_col==rook_col:
        wpl+=1
    else:
        j=bishop_col
        for step in range(bishop_row,-1,-1):      #sinthikes tou Bishop
            if step==rook_row and j==rook_col:
                bpl+=1
            j+=1
            if j==c:
                break
        j=bishop_col
        if j>0:
            for step in range(bishop_row,r):
                if step==rook_row and j==rook_col:
                    bpl+=1
                j+=-1
                if j==-1:
                    break
        j=bishop_col
        for step in range(bishop_row,r):
            if step==rook_row and j==rook_col:
                bpl+=1
            j+=1
            if j==c:
                break
        j=bishop_col
        for step in range(bishop_row,-1,-1):
            if step==rook_row and j==rook_col:
                bpl+=1
            j+=-1
            if j==-1:
                break
r=8
c=8
wpl=0
bpl=0
for i in range(100):
    game(r,c)
print(r,"x",c,"Game results:")
print("White Player:",wpl)
print("Black Player:",bpl)

r=7
c=7    
wpl=0
bpl=0
for i in range(100):
    game(r,c)
print(r,"x",c,"Game results:")
print("White Player:",wpl)
print("Black Player:",bpl)

r=7
c=8    
wpl=0
bpl=0
for i in range(100):
    game(r,c)
print(r,"x",c,"Game results:")
print("White Player:",wpl)
print("Black Player:",bpl)