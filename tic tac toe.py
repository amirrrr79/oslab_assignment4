import random
from colorama import Fore
from time import time

game= [['-','-','-'],
       ['-','-','-'],
       ['-','-','-']]

############# def ###############
def show_game():       
  for i in range(3):
    for j in range(3):
        if game[i][j]=='x':
           print(Fore.RED + 'x',end='')
        elif game[i][j]=='o':
            print(Fore.BLUE + 'o',end='')
        else:
            print(Fore.WHITE + '-',end='')    
    print(Fore.RESET)   

def check_win_palayer1_vs_palayer2(start_time=time()):
   if game[0][0]=='x' and game[0][1]=='x' and game[0][2]=='x':
        print('palayer1 win')
        print(time_game(start_time))
        exit() 
   elif game[1][0]=='x' and game[1][1]=='x' and game[1][2]=='x':
        print('palayer1 win')
        print(time_game(start_time))
        exit() 
   elif game[2][0]=='x' and game[2][1]=='x' and game[2][2]=='x':
        print('palayer1 win')
        print(time_game(start_time))
        exit() 
   elif game[0][0]=='x' and game[1][1]=='x' and game[2][2]=='x':
        print('palayer1 win')
        print(time_game(start_time))
        exit() 
   elif game[0][2]=='x' and game[1][1]=='x' and game[2][0]=='x':
        print('palayer1 win')
        print(time_game(start_time))
        exit() 
   elif game[0][0]=='o' and game[1][0]=='o' and game[2][0]=='o':
       print('palayer2 win')
       print(time_game(start_time))
       exit()
   elif game[0][1]=='o' and game[1][1]=='o' and game[2][1]=='o':
       print('palayer2 win')
       print(time_game(start_time))
       exit()
   elif game[0][2]=='o' and game[1][2]=='o' and game[2][2]=='o': 
       print('palayer2 win')
       print(time_game(start_time))
       exit()
   elif game[0][0]=='o' and game[1][1]=='o' and game[2][2]=='o':
       print('palayer2 win')
       print(time_game(start_time))
       exit()
   elif game[2][0]=='o' and game[1][1]=='o' and game[0][2]=='o':
       print('palayer2 win') 
       print(time_game(start_time))
       exit() 
   elif game[0][0]=='x' and game[1][0]=='x' and game[2][0]=='x':
        print('palayer1 win')
        print(time_game(start_time))
        exit()
   elif game[0][1]=='x' and game[1][1]=='x' and game[2][1]=='x':
        print('palayer1 win')
        print(time_game(start_time))
        exit() 
   elif game[0][2]=='x' and game[1][2]=='x' and game[2][2]=='x':
        print('palayer1 win')
        print(time_game(start_time))
        exit()
   elif game[0][0]=='o' and game[0][1]=='o' and game[0][2]=='o':
       print('palayer2 win')
       print(time_game(start_time))
       exit()
   elif game[1][0]=='o' and game[1][1]=='o' and game[1][2]=='o':
       print('palayer2 win')
       print(time_game(start_time))
       exit()
   elif game[2][0]=='o' and game[2][1]=='o' and game[2][2]=='o': 
       print('palayer2 win')
       print(time_game(start_time))
       exit() 


def check_win_computer_vs_palayer(start_time=time()):
   if game[0][0]=='x' and game[0][1]=='x' and game[0][2]=='x':
        print('palayer win')
        print(time_game(start_time))
        exit() 
   elif game[1][0]=='x' and game[1][1]=='x' and game[1][2]=='x':
        print('palayer win')
        print(time_game(start_time))
        exit() 
   elif game[2][0]=='x' and game[2][1]=='x' and game[2][2]=='x':
        print('palayer win')
        print(time_game(start_time))
        exit() 
   elif game[0][0]=='x' and game[1][1]=='x' and game[2][2]=='x':
        print('palayer win')
        print(time_game(start_time))
        exit() 
   elif game[0][2]=='x' and game[1][1]=='x' and game[2][0]=='x':
        print('palayer win')
        print(time_game(start_time))
        exit() 
   elif game[0][0]=='o' and game[1][0]=='o' and game[2][0]=='o':
       print('computer win')
       print(time_game(start_time))
       exit()
   elif game[0][1]=='o' and game[1][1]=='o' and game[2][1]=='o':
       print('computer win')
       print(time_game(start_time))
       exit()
   elif game[0][2]=='o' and game[1][2]=='o' and game[2][2]=='o': 
       print('computer win')
       print(time_game(start_time))
       exit()
   elif game[0][0]=='o' and game[1][1]=='o' and game[2][2]=='o':
       print('computer win')
       print(time_game(start_time))
       exit()
   elif game[2][0]=='o' and game[1][1]=='o' and game[0][2]=='o':
       print('computer win')
       print(time_game(start_time))
       exit()
   elif game[0][0]=='x' and game[1][0]=='x' and game[2][0]=='x':
        print('palayer win')
        print(time_game(start_time))
        exit()
   elif game[0][1]=='x' and game[1][1]=='x' and game[2][1]=='x':
        print('palayer win')
        print(time_game(start_time))
        exit() 
   elif game[0][2]=='x' and game[1][2]=='x' and game[2][2]=='x':
        print('palayer win')
        print(time_game(start_time))
        exit()
   elif game[0][0]=='o' and game[0][1]=='o' and game[0][2]=='o':
       print('computer win')
       print(time_game(start_time))
       exit()
   elif game[1][0]=='o' and game[1][1]=='o' and game[1][2]=='o':
       print('computer win')
       print(time_game(start_time))
       exit()
   elif game[2][0]=='o' and game[2][1]=='o' and game[2][2]=='o': 
       print('computer win')
       print(time_game(start_time))
       exit()           
   

def check_draw(start_time=time()):
    for i in range(3):
        for j in range(3):
            if game[i][j]=='-':
               return False
    print(time_game(start_time))          
    return True
   
def time_game(start_time):
    return time() - start_time                   

############# main ############

while True:
    print('welcome')
    print('1.computer_vs_palayer')
    print('2.palayer1_vs_palayer2')
    print('3.exit')
    op=int(input('Enter number:'))

#### palayer_vs_computer ####
    if op==1:
        show_game()
        
        while True:
            start_time=time()
            while True:
                print('palayer')
                row=int(input('row:'))    
                col=int(input('col:'))  
                if 0<= row <=2 and 0<= col <=2:
                   if game[row][col]=='-':
                      game[row][col]='x'
                      break
                   else:
                      print('not empty')
                else:
                 print('col and row must be betwin 0,2')
            show_game()
            check_win_computer_vs_palayer()
            if check_draw():
               print('tasavi')
               exit()

            while True:
                print('computer')
                row=random.randint(0,2)
                col=random.randint(0,2)
                if 0<= row <=2 and 0<= col <=2:
                    if game[row][col]=='-':
                       game[row][col]='o'
                       break
                    else:
                     print('not empty')
                else:
                  print('col and row must be betwin 0,2')
            show_game()
            check_win_computer_vs_palayer()
            if check_draw():
                print('tasavi')
                exit()


##### palayer1_vs_palayer2 ######
    if op==2:
       show_game()
       while True:
           start_time=time()
           while True:
               print('palayer1')
               row=int(input('row:'))    
               col=int(input('col:'))    
               if 0<= row <=2 and 0<= col <=2:
                   if game[row][col]=='-':
                      game[row][col]='x'
                      break
                   else:
                      print('not empty')
               else:
                 print('col and row must be betwin 0,2') 
           show_game()
           check_win_palayer1_vs_palayer2()
           if check_draw():
            print('tasavi')
            exit()
           
                
           while True:
               print('palayer2')
               row=int(input('row:'))    
               col=int(input('col:'))
               if 0<= row <=2 and 0<= col <=2:
                  if game[row][col]=='-':
                     game[row][col]='o'
                     break
                  else:
                     print('not empty')
               else:
                  print('col and row must be betwin 0,2')
           show_game()  
           check_win_palayer1_vs_palayer2()
           if check_draw():
            print('tasavi')
            exit()

    if op==3:
       print('goodby')
       exit()

              
    






