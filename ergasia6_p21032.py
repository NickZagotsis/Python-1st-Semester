

import random
import time
whplayer=0
blplayer=0
n=8
for ep in range(100):
    board=[[" 0 "]*n for i in range(8)]
    w_rook_row=random.randint(0,7)
    w_rook_col=random.randint(0,7)
    while(True):
        end=False
        w_bishop_row=random.randint(0,7)
        if(w_bishop_row!=w_rook_row):
            end=True
        w_bishop_col=random.randint(0,7)
        if(w_bishop_col!=w_rook_col):
            end=True
        if end:
            break
    while(True):   
        end=False 
        b_queen_row=random.randint(0,7)
        if ( b_queen_row!=w_bishop_row and b_queen_row!=w_rook_row ):
            end=True
        b_queen_col=random.randint(0,7)
        if (b_queen_col!=w_rook_col and b_queen_col!=w_bishop_col):
            end=True
        if end:
            break
    board[w_rook_row][w_rook_col]=" R "
    board[w_bishop_row][w_bishop_col]=" B "
    board[b_queen_row][b_queen_col]=" Q "
    # print("--------------------------")
    # for row in board:
    #     print(row)
    # print(w_rook_row,w_rook_col,"rook")
    # print(w_bishop_row,w_bishop_col,"bishop")
    # print(b_queen_row,b_queen_col,"queen")
    # print("--------------------------")
    #auto edo einai gia na deite to checkboard me ta pionia
    if (b_queen_col == w_rook_col or b_queen_row==w_rook_row):
        blplayer+=1 #edo an einai sthn idia sthlh or idia grammh, h Queen me ton Rook, tote o enas troei ton allon
        whplayer+=1
        #diagonia pano aristera
    j=b_queen_col
    for step in range(b_queen_row,-1,-1):   
        if (step==w_rook_row and j==w_rook_col):
            blplayer+=1 #h Queen troei ton rook xoris aftos na kanei kati         
        if (step==w_bishop_row and j==w_bishop_col):
            whplayer+=1
            blplayer+=1 #edo vazo kai gia tous duo ena ponto giati h Queen Troei ton bishop omos kai o bishop troei th Queen epeidh einai diagonia      
        j+=-1
        if j==-1:
            break
    j=b_queen_col
    #diagonia kato deksia
    for step in range(b_queen_row,8):     
        if step==w_rook_row and j==w_rook_col:
            blplayer+=1
        if step==w_bishop_row and j==w_bishop_col:
            blplayer+=1
            whplayer+=1
        j+=1
        if j==8:
            break
    j=b_queen_col
    #diagonia pano deksia
    for step in range(b_queen_row,-1,-1):      
        if step==w_rook_row and j==w_rook_col:
            blplayer+=1
        if step==w_bishop_row and j==w_bishop_col:
            blplayer+=1
            whplayer+=1
        j+=1
        if j==8:
            break
    j=b_queen_col
    #diagonia kato aristera
    if j > 0:
        for step in range(b_queen_row,8):
                    
            if step==w_bishop_row and j==w_bishop_col:
                blplayer+=1
                whplayer+=1
            if step==w_rook_row and j==w_rook_col:
                blplayer+=1
            j+=-1
            if j==-1:
                break
    if(b_queen_row==w_bishop_row or b_queen_col==w_bishop_col):
        blplayer+=1
    # time.sleep(1) 
    # afto gia na ginei ligo pio omorfh h emfanish
    
print ("White player:",whplayer)
print("Black Player:",blplayer)

        
    
