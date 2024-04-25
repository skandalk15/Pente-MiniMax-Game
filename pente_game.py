import sys
import copy
import timeit
import os

myMove = None

def getMyMove(board, myagent_tile):
    global myMove
    myMove = alpha_beta_Pruning(board, 1, myagent_tile)
    return myMove

def getChildNodes(board, my_agent):
    children_states = []
    for x in range(n):
        for y in range(n):
            if isValidMove(board, (x, y)):
                children_states.append((copy.deepcopy(board), (x, y)))
                makeMove(children_states[-1][0], my_agent, children_states[-1][1])
    return children_states

def alpha_beta_Pruning(board, depth, my_agent):
    global remaining_play_time
    t1=timeit.default_timer()
    m = minValue((board,-1), depth, my_agent, (float("-inf"), -1), (float("inf"), -1))
    t2=timeit.default_timer()
    time_taken = t2 - t1
    print("Processing time: ", float(time_taken))
    return m[1]

def maxValue(board, depth, my_agent, alpha, beta):
    if my_agent == 'w':
        ta_agent = 'b'
    else:
        ta_agent = 'w'
    if depth == 0:
        if my_agent == 'w':
            return (eval(board[0]), board[1])
        else:
            return (eval(board[0]) * -1, board[1])
    for child in getChildNodes(board[0], my_agent):
        m = minValue(child, depth-1, ta_agent, alpha, beta)
        if m[0] > alpha[0]:
            alpha = m
        if alpha[0] >= beta[0]:
            return alpha
    return alpha
    
def minValue(board, depth, my_agent, alpha, beta):
    if my_agent == 'w':
        ta_agent = 'b'
    else:
        ta_agent = 'w'
    if depth == 0:
        if my_agent == 'w':
            return (eval(board[0]), board[1])
        else:
            return (eval(board[0]) * -1, board[1])
    for child in getChildNodes(board[0], my_agent):
        m = maxValue(child, depth-1 , ta_agent, alpha, beta)
        if m[0] < beta[0]:
            beta = m
        if alpha[0] >= beta[0]:
            return beta
    return beta


def eval(board):
    white_capture_count = 0
    black_capture_count = 0
    
    white_tile = 'w'
    black_tile = 'b'

    w2_ct = 0
    w3_ct = 0
    w4_ct = 0
    w5_ct = 0
    w6_ct = 0
    

    b2_ct = 0
    b3_ct = 0
    b4_ct = 0
    b5_ct = 0
    b6_ct = 0


    for x in range(n-4):
        for y in range(n):
            if (board[x][y] == white_tile and board[x+1][y] == black_tile and board[x+2][y] == black_tile and board[x+3][y] == '.') or (board[x][y] == '.' and board[x+1][y] == black_tile and board[x+2][y] == black_tile and board[x+3][y] == white_tile):
                white_capture_count += 2

            if (board[x][y] == black_tile and board[x+1][y] == white_tile and board[x+2][y] == white_tile and board[x+3][y] == '.') or (board[x][y] == '.' and board[x+1][y] == white_tile and board[x+2][y] == white_tile and board[x+3][y] == black_tile):
                black_capture_count += 2
                
    for x in range(n):
        for y in range(n-4):
        
            if (board[x][y] == white_tile and board[x][y+1] == black_tile and board[x][y+2] == black_tile and board[x][y+3] == '.') or (board[x][y] == '.' and board[x][y+1] == black_tile and board[x][y+2] == black_tile and board[x][y+3] == white_tile):
                white_capture_count += 2

            if (board[x][y] == black_tile and board[x][y+1] == white_tile and board[x][y+2] == white_tile and board[x][y+3] == '.') or (board[x][y] == '.' and board[x][y+1] == white_tile and board[x][y+2] == white_tile and board[x][y+3] == black_tile):
                black_capture_count += 2

    for x in range(n-3):
        for y in range(3, n):

            if (board[x][y] == white_tile and board[x+1][y-1] == black_tile and board[x+2][y-2] == black_tile and board[x+3][y-3] == '.') or (board[x][y] == '.' and board[x+1][y-1] == black_tile and board[x+1][y-2] == black_tile and board[x+2][y-3] == white_tile):
                white_capture_count += 2

            if (board[x][y] == black_tile and board[x+1][y-1] == white_tile and board[x+2][y-2] == white_tile and board[x+3][y-3] == '.') or (board[x][y] == '.' and board[x+1][y-1] == white_tile and board[x+1][y-2] == white_tile and board[x+2][y-3] == black_tile):
                black_capture_count += 2

    for x in range(n-4):
        for y in range(n-4):
            
            if (board[x][y] == white_tile and board[x+1][y+1] == black_tile and board[x+2][y+2] == black_tile and board[x+3][y+3] == '.') or (board[x][y] == '.' and board[x+1][y+1] == black_tile and board[x+2][y+2] == black_tile and board[x+3][y+3] == white_tile):
                white_capture_count += 2


            if (board[x][y] == black_tile and board[x+1][y+1] == white_tile and board[x+2][y+2] == white_tile and board[x+3][y+3] == '.') or (board[x][y] == '.' and board[x+1][y+1] == white_tile and board[x+2][y+2] == white_tile and board[x+3][y+3] == black_tile):
                black_capture_count += 2
                
    for x in range(n):
        for y in range(n-3):
            if ((board[x][y]==white_tile and board[x][y+1]==white_tile and board[x][y+2]=='.') or (board[x][y]=='.' and board[x][y+1]==white_tile and board[x][y+2]==white_tile)):
                w2_ct += 1
            if ((board[x][y]==black_tile and board[x][y+1]==black_tile and board[x][y+2]=='.') or (board[x][y]=='.' and board[x][y+1]==black_tile and board[x][y+2]==black_tile)):
                b2_ct += 1
        for y in range(n-4):
            if ((board[x][y]==white_tile and board[x][y+1]==white_tile and board[x][y+2]==white_tile and board[x][y+3]=='.') or (board[x][y]=='.' and board[x][y+1]==white_tile and board[x][y+2]==white_tile and board[x][y+3]==white_tile)):
                w3_ct += 1
            if ((board[x][y]==black_tile and board[x][y+1]==black_tile and board[x][y+2]==black_tile and board[x][y+3]=='.') or (board[x][y]=='.' and board[x][y+1]==black_tile and board[x][y+2]==black_tile and board[x][y+3]==black_tile)):
                b3_ct += 1
        for y in range(n-5):
            if((board[x][y]==white_tile and board[x][y+1]==white_tile and board[x][y+2]==white_tile and board[x][y+3]==white_tile and board[x][y+4]=='.') or (board[x][y]=='.' and board[x][y+1]==white_tile and board[x][y+2]==white_tile and board[x][y+3]==white_tile and board[x][y+4]==white_tile)):
                w4_ct += 1
            if((board[x][y]==black_tile and board[x][y+1]==black_tile and board[x][y+2]==black_tile and board[x][y+3]==black_tile and board[x][y+4]=='.') or (board[x][y]=='.' and board[x][y+1]==black_tile and board[x][y+2]==black_tile and board[x][y+3]==black_tile and board[x][y+4]==black_tile)):
                b4_ct += 1
            if(board[x][y]==white_tile and board[x][y+1]==white_tile and board[x][y+2]==white_tile and board[x][y+3]==white_tile and board[x][y+4]==white_tile):
                w5_ct += 1
            if(board[x][y]==black_tile and board[x][y+1]==black_tile and board[x][y+2]==black_tile and board[x][y+3]==black_tile and board[x][y+4]==black_tile):
                b5_ct += 1
            if(board[x][y]=='.' and board[x][y+1]==black_tile and board[x][y+2]==black_tile and board[x][y+3]==black_tile and board[x][y+4]=='.') or (board[x][y]==black_tile and board[x][y+1]=='.' and board[x][y+2]==black_tile and board[x][y+3]==black_tile and board[x][y+4]=='.') or (board[x][y]=='.' and board[x][y+1]==black_tile and board[x][y+2]==black_tile and board[x][y+3]=='.' and board[x][y+4]==black_tile):
                b6_ct += 1
            if(board[x][y]=='.' and board[x][y+1]==white_tile and board[x][y+2]==white_tile and board[x][y+3]==white_tile and board[x][y+4]=='.') or (board[x][y]==white_tile and board[x][y+1]=='.' and board[x][y+2]==white_tile and board[x][y+3]==white_tile and board[x][y+4]=='.') or (board[x][y]=='.' and board[x][y+1]==white_tile and board[x][y+2]==white_tile and board[x][y+3]=='.' and board[x][y+4]==white_tile):
                w6_ct += 1
            

    for x in range(n-3):
        for y in range(n):
            if((board[x][y]==white_tile and board[x+1][y]==white_tile and board[x+2][y]=='.') or (board[x][y]=='.' and board[x+1][y]==white_tile and board[x+2][y]==white_tile)):
                w2_ct+=1
            if((board[x][y]==black_tile and board[x+1][y]==black_tile and board[x+2][y]=='.') or (board[x][y]=='.' and board[x+1][y]==black_tile and board[x+2][y]==black_tile)):
                b2_ct+=1
          
    for x in range(n-4):
        for y in range(n):
            if((board[x][y]==white_tile and board[x+1][y]==white_tile and board[x+2][y]==white_tile and board[x+3][y]=='.') or (board[x][y]=='.' and board[x+1][y]==white_tile and board[x+2][y]==white_tile and board[x+3][y]==white_tile)):
                w3_ct+=1
            if((board[x][y]==black_tile and board[x+1][y]==black_tile and board[x+2][y]==black_tile and board[x+3][y]=='.') or (board[x][y]=='.' and board[x+1][y]==black_tile and board[x+2][y]==black_tile and board[x+3][y]==black_tile)):
                b3_ct+=1

    for x in range(n-5):
        for y in range(n):
            if((board[x][y]==white_tile and board[x+1][y]==white_tile and board[x+2][y]==white_tile and board[x+3][y]==white_tile and board[x+4][y]=='.') or (board[x][y]=='.' and board[x+1][y]==white_tile and board[x+2][y]==white_tile and board[x+3][y]==white_tile and board[x+4][y]==white_tile)):
                w4_ct+=1
            if((board[x][y]==black_tile and board[x+1][y]==black_tile and board[x+2][y]==black_tile and board[x+3][y]==black_tile and board[x+4][y]=='.') or (board[x][y]=='.' and board[x+1][y]==black_tile and board[x+2][y]==black_tile and board[x+3][y]==black_tile and board[x+4][y]==black_tile)):
                b4_ct+=1
            if(board[x][y]==white_tile and board[x+1][y]==white_tile and board[x+2][y]==white_tile and board[x+3][y]==white_tile and board[x+4][y]==white_tile):
                w5_ct+=1
            if(board[x][y]==black_tile and board[x+1][y]==black_tile and board[x+2][y]==black_tile and board[x+3][y]==black_tile and board[x+4][y]==black_tile):
                b5_ct+=1
            if(board[x][y]=='.' and board[x+1][y]==black_tile and board[x+2][y]==black_tile and board[x+3][y]==black_tile and board[x+4][y]=='.') or (board[x][y]==black_tile and board[x+1][y]=='.' and board[x+2][y]==black_tile and board[x+3][y]==black_tile and board[x+4][y]=='.') or (board[x][y]=='.' and board[x+1][y]==black_tile and board[x+2][y]==black_tile and board[x+3][y]=='.' and board[x+4][y]==black_tile):
                b6_ct+=1
            if(board[x][y]=='.' and board[x+1][y]==white_tile and board[x+2][y]==white_tile and board[x+3][y]==white_tile and board[x+4][y]=='.') or (board[x][y]==white_tile and board[x+1][y]=='.' and board[x+2][y]==white_tile and board[x+3][y]==white_tile and board[x+4][y]=='.') or (board[x][y]=='.' and board[x+1][y]==white_tile and board[x+2][y]==white_tile and board[x+3][y]=='.' and board[x+4][y]==white_tile):
                w6_ct+=1

    for x in range(n-3):
        for y in range(n-3):
            if((board[x][y]==white_tile and board[x+1][y+1]==white_tile and board[x+2][y+2]=='.') or (board[x][y]=='.' and board[x+1][y+1]==white_tile and board[x+2][y+2]==white_tile)):
                w2_ct+=1
            if((board[x][y]==black_tile and board[x+1][y+1]==black_tile and board[x+2][y+2]=='.') or (board[x][y]=='.' and board[x+1][y+1]==black_tile and board[x+2][y+2]==black_tile)):
                b2_ct+=1
    
    for x in range(n-4):
        for y in range(n-4):
            if((board[x][y]==white_tile and board[x+1][y+1]==white_tile and board[x+2][y+2]==white_tile and board[x+3][y+3]=='.') or (board[x][y]=='.' and board[x+1][y+1]==white_tile and board[x+2][y+2]==white_tile and board[x+3][y+3]==white_tile)):
                w3_ct+=1
            if((board[x][y]==black_tile and board[x+1][y+1]==black_tile and board[x+2][y+2]==black_tile and board[x+3][y+3]=='.') or (board[x][y]=='.' and board[x+1][y+1]==black_tile and board[x+2][y+2]==black_tile and board[x+3][y+3]==black_tile)):
                b3_ct+=1

            
    for x in range(n-5):
        for y in range(n-5):
            if((board[x][y]==white_tile and board[x+1][y+1]==white_tile and board[x+2][y+2]==white_tile and board[x+3][y+3]==white_tile and board[x+4][y+4]=='.') or (board[x][y]=='.' and board[x+1][y+1]==white_tile and board[x+2][y+2]==white_tile and board[x+3][y+3]==white_tile and board[x+4][y+4]==white_tile)):
                w4_ct+=1
            if((board[x][y]==black_tile and board[x+1][y+1]==black_tile and board[x+2][y+2]==black_tile and board[x+3][y+3]==black_tile and board[x+4][y+4]=='.') or (board[x][y]=='.' and board[x+1][y+1]==black_tile and board[x+2][y+2]==black_tile and board[x+3][y+3]==black_tile and board[x+4][y+4]==black_tile)):
                b4_ct+=1
            if(board[x][y]==white_tile and board[x+1][y+1]==white_tile and board[x+2][y+2]==white_tile and board[x+3][y+3]==white_tile and board[x+4][y+4]==white_tile):
                w5_ct+=1
            if(board[x][y]==black_tile and board[x+1][y+1]==black_tile and board[x+2][y+2]==black_tile and board[x+3][y+3]==black_tile and board[x+4][y+4]==black_tile):
                b5_ct+=1  
            if(board[x][y]=='.' and board[x+1][y+1]==black_tile and board[x+2][y+2]==black_tile and board[x+3][y+3]==black_tile and board[x+4][y+4]=='.') or (board[x][y]==black_tile and board[x+1][y+1]=='.' and board[x+2][y+2]==black_tile and board[x+3][y+3]==black_tile and board[x+4][y+4]=='.') or (board[x][y]=='.' and board[x+1][y+1]==black_tile and board[x+2][y+2]==black_tile and board[x+3][y+3]=='.' and board[x+4][y+4]==black_tile):
                b6_ct+=1 
            if(board[x][y]=='.' and board[x+1][y+1]==white_tile and board[x+2][y+2]==white_tile and board[x+3][y+3]==white_tile and board[x+4][y+4]=='.') or (board[x][y]==white_tile and board[x+1][y+1]=='.' and board[x+2][y+2]==white_tile and board[x+3][y+3]==white_tile and board[x+4][y+4]=='.') or (board[x][y]=='.' and board[x+1][y+1]==white_tile and board[x+2][y+2]==white_tile and board[x+3][y+3]=='.' and board[x+4][y+4]==white_tile):
                w6_ct+=1

    for x in range(n-3):
        for y in range(2,n):
            if((board[x][y]==white_tile and board[x+1][y-1]==white_tile and board[x+2][y-2]=='.') or (board[x][y]=='.' and board[x+1][y-1]==white_tile and board[x+2][y-2]==white_tile)):
                w2_ct+=1
            if((board[x][y]==black_tile and board[x+1][y-1]==black_tile and board[x+2][y-2]=='.') or (board[x][y]=='.' and board[x+1][y-1]==black_tile and board[x+2][y-2]==black_tile)):
                b2_ct+=1

    for x in range(n-4):
        for y in range(3,n):
            if((board[x][y]==white_tile and board[x+1][y-1]==white_tile and board[x+2][y-2]==white_tile and board[x+3][y-3]=='.') or (board[x][y]=='.' and board[x+1][y-1]==white_tile and board[x+2][y-2]==white_tile and board[x+3][y-3]==white_tile)):
                w3_ct+=1
            if((board[x][y]==black_tile and board[x+1][y-1]==black_tile and board[x+2][y-2]==black_tile and board[x+3][y-3]=='.') or (board[x][y]=='.' and board[x+1][y-1]==black_tile and board[x+2][y-2]==black_tile and board[x+3][y-3]==black_tile)):
                b3_ct+=1

    for x in range(n-5):
        for y in range(4,n):
            if((board[x][y]==white_tile and board[x+1][y-1]==white_tile and board[x+2][y-2]==white_tile and board[x+3][y-3]==white_tile and board[x+4][y-4]=='.') or (board[x][y]=='.' and board[x+1][y-1]==white_tile and board[x+2][y-2]==white_tile and board[x+3][y-3]==white_tile and board[x+4][y-4]==white_tile)):
                w4_ct+=1
            if((board[x][y]==black_tile and board[x+1][y-1]==black_tile and board[x+2][y-2]==black_tile and board[x+3][y-3]==black_tile and board[x+4][y-4]=='.') or (board[x][y]=='.' and board[x+1][y-1]==black_tile and board[x+2][y-2]==black_tile and board[x+3][y-3]==black_tile and board[x+4][y-4]==black_tile)):
                b4_ct+=1
            if(board[x][y]==white_tile and board[x+1][y-1]==white_tile and board[x+2][y-2]==white_tile and board[x+3][y-3]==white_tile and board[x+4][y-4]==white_tile):
                w5_ct+=1
            if(board[x][y]==black_tile and board[x+1][y-1]==black_tile and board[x+2][y-2]==black_tile and board[x+3][y-3]==black_tile and board[x+4][y-4]==black_tile):
                b5_ct+=1
            if(board[x][y]=='.' and board[x+1][y-1]==black_tile and board[x+2][y-2]==black_tile and board[x+3][y-3]==black_tile and board[x+4][y-4]=='.') or (board[x][y]==black_tile and board[x+1][y-1]=='.' and board[x+2][y-2]==black_tile and board[x+3][y-3]==black_tile and board[x+4][y-4]=='.') or (board[x][y]=='.' and board[x+1][y-1]==black_tile and board[x+2][y-2]==black_tile and board[x+3][y-3]=='.' and board[x+4][y-4]==black_tile):
                b6_ct+=1
            if(board[x][y]=='.' and board[x+1][y-1]==white_tile and board[x+2][y-2]==white_tile and board[x+3][y-3]==white_tile and board[x+4][y-4]=='.') or (board[x][y]==white_tile and board[x+1][y-1]=='.' and board[x+2][y-2]==white_tile and board[x+3][y-3]==white_tile and board[x+4][y-4]=='.') or (board[x][y]=='.' and board[x+1][y-1]==white_tile and board[x+2][y-2]==white_tile and board[x+3][y-3]=='.' and board[x+4][y-4]==white_tile):
                w6_ct+=1
            
    if(next_move_color=='BLACK'):
        w_points = 14*w5_ct+ 12*w4_ct+10*w6_ct+w3_ct+w2_ct
        b_points = 12*b5_ct+ 8*b4_ct+b6_ct+b3_ct+b2_ct
    else:
        w_points = 12 * w5_ct  +  8*w4_ct  +      w6_ct +w3_ct + w2_ct
        b_points = 14 * b5_ct  +  10*b4_ct +   10 * b6_ct +b3_ct + b2_ct
    
    return 4*(w_points - b_points) + 4*(white_capture_count - black_capture_count)

def isValidMove(board, move):
    if move[0] >= 0 and move[0] < n and move[1] >= 0 and move[1] < n:
        return (board[move[0]][move[1]] == '.')
    return False

def makeMove(board, my_agent, move):
    global wcaptures, bcaptures
    captures = captureMove(board, my_agent, move)
    board[move[0]][move[1]] = my_agent

def makeCaptureMove(board, my_agent, move):
    global wcaptures, bcaptures
    captures = captureMove(board, my_agent, move)
    board[move[0]][move[1]] = my_agent
    if captures != 0:
        if my_agent == 'b':
            bcaptures += captures
        else:
            wcaptures += captures
    print(wcaptures, bcaptures)


def captureMove(board, my_agent, move):
    capture_count = 0
    if my_agent == 'b':
        ta_agent = 'w'
    else:
        ta_agent = 'b'

    if (move[1] > 2 and board[move[0]][move[1]-1] == ta_agent and board[move[0]][move[1]-2] == ta_agent and  board[move[0]][move[1]-3] == my_agent):
        board[move[0]][move[1]-1] = '.'
        board[move[0]][move[1]-2] = '.'
        capture_count += 2
        
    if (move[1] < n-3 and board[move[0]][move[1]+1] == ta_agent and board[move[0]][move[1]+2] == ta_agent and board[move[0]][move[1]+3] == my_agent):
        board[move[0]][move[1]+1] = '.'
        board[move[0]][move[1]+2] = '.'
        capture_count += 2
        
    if (move[0] > 2 and board[move[0]-1][move[1]] == ta_agent and board[move[0]-2][move[1]] == ta_agent and board[move[0]-3][move[1]] == my_agent):
        board[move[0]-1][move[1]] = '.'
        board[move[0]-2][move[1]] = '.'
        capture_count += 2


    if (move[0] > 2 and move[1] > 2 and board[move[0]-1][move[1]-1] == ta_agent and board[move[0]-2][move[1]-2] == ta_agent and board[move[0]-3][move[1]-3] == my_agent):
        board[move[0]-1][move[1]-1] = '.'
        board[move[0]-2][move[1]-2] = '.'
        capture_count += 2
        
    if (move[0] < n-3 and move[1] < n-3 and board[move[0]+1][move[1]+1] == ta_agent and board[move[0]+2][move[1]+2] == ta_agent and board[move[0]+3][move[1]+3] == my_agent):
        board[move[0]+1][move[1]+1] = '.'
        board[move[0]+2][move[1]+2] = '.'
        capture_count += 2
        
    if (move[0] < n-3 and move[1] < n-3 and board[move[0]+1][move[1]-1] == ta_agent and board[move[0]+2][move[1]-2] == ta_agent and board[move[0]+3][move[1]-3] == my_agent):
        board[move[0]+1][move[1]-1] = '.'
        board[move[0]+2][move[1]-2] = '.'
        capture_count += 2

    if (move[0] < n-3 and board[move[0]+1][move[1]] == ta_agent and board[move[0]+2][move[1]] == ta_agent and board[move[0]+3][move[1]] == my_agent):
        board[move[0]+1][move[1]] = '.'
        board[move[0]+2][move[1]] = '.'
        capture_count += 2
        
    
    if (move[0] > 2 and move[1] < n-3 and board[move[0]-1][move[1]+1] == ta_agent and board[move[0]-2][move[1]+2] == ta_agent and board[move[0]-3][move[1]+3] == my_agent):
        board[move[0]-1][move[1]+1] = '.'
        board[move[0]-2][move[1]+2] = '.'
        capture_count += 2

    return capture_count

def isWinner(board, my_agent_tile):
    for y in range(n):
        for x in range(n - 4):
            if board[x][y] == my_agent_tile and board[x+1][y] == my_agent_tile and board[x+2][y] == my_agent_tile and board[x+3][y] == my_agent_tile and board[x+4][y] == my_agent_tile:
                return True

    for x in range(n):
        for y in range(n - 4):
            if board[x][y] == my_agent_tile and board[x][y+1] == my_agent_tile and board[x][y+2] == my_agent_tile and board[x][y+3] == my_agent_tile and board[x][y+4] == my_agent_tile:
                return True

    for x in range(n - 4):
        for y in range(4, n):
            if board[x][y] == my_agent_tile and board[x+1][y-1] == my_agent_tile and board[x+2][y-2] == my_agent_tile and board[x+3][y-3] == my_agent_tile and board[x+4][y-4] == my_agent_tile:
                return True

    for x in range(n - 4):
        for y in range(n - 4):
            if board[x][y] == my_agent_tile and board[x+1][y+1] == my_agent_tile and board[x+2][y+2] == my_agent_tile and board[x+3][y+3] == my_agent_tile and board[x+4][y+4] == my_agent_tile:
                return True

    if my_agent_tile == 'w':
        if wcaptures >= 10:
            return True
    else:
        if bcaptures >= 10:
            return True
    return False

def check_first_move_pattern(input_matrix):
    pattern = ['...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................']
    pattern_rows = [row for row in pattern]
    input_rows = ["".join(row) for row in input_matrix]
    if input_rows == pattern_rows:
        return True
    else:
        return False

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "input.txt"), "r").read()
    input_lines = file.split("\n")
    output_file = 'output.txt'
    next_move_color = str(input_lines[0])
    remaining_play_time = float(input_lines[1])
    wcaptures,bcaptures = [int(i) for i in input_lines[2].split(',')]
    board2 = [[]]
    n=19
    for grid_rows in input_lines[3:22]:
        grid_row=[]
        for grid_cell in grid_rows.split(' '):
            grid_row.append(str(grid_cell))
        board2.append(grid_row)
    board = board2[1:]
    li2=[[]]
    for b in board:
        li3=[]
        for i in b[0]:
            li3.append(i)
        li2.append(li3)
    pente_board=li2[1:]
    if(next_move_color=="BLACK"):
        my_agent_tile , ta_agent_tile = ('b','w')
        my_move = getMyMove(pente_board,my_agent_tile)
    else:
        my_agent_tile , ta_agent_tile = ('w','b')
        if(check_first_move_pattern(pente_board)):
            my_move=(9,9)
        else:
            for i in range(first_move_row-3, first_move_row+4):
                for j in range(first_move_col-3, first_move_col+4):
                    if i < 0 or i >= board_size or j < 0 or j >= board_size:
                        continue  # skip out-of-bounds positions
                    if board[i][j] == 0 and abs(i - first_move_row) >= 3 and abs(j - first_move_col) >= 3:
                # Place a white stone at the first available position
                        board[i][j] = 1
            return
                my_move = getMyMove(pente_board,my_agent_tile)    
    if isValidMove(pente_board, my_move):
        makeCaptureMove(pente_board, my_agent_tile, my_move)
        print(my_move)
    if isWinner(pente_board, my_agent_tile):
        print("MY AGENT HAS WON")   
    row_num_conversion = {0:19,1:18,2:17,3:16,4:15,5:14,6:13,7:12,8:11,9:10,10:9,11:8,12:7,13:6,14:5,15:4,16:3,17:2,18:1}
    result = []
    result.append(row_num_conversion[my_move[0]])
    if(my_move[1]<=7):
        result.append(chr(65+my_move[1]))
    else:
        result.append(chr(66+my_move[1]))
    output_file = open(output_file,'w')
    output_string = ''.join(str(res) for res in result)
    output_file.write(output_string)