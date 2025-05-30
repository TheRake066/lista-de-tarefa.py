# requisito: sudo apt install figlet

import time
import subprocess
print('-'*20)
subprocess.run(["cat","desenho.txt"])
print('-'*20)

tarefa = input('Adicionar a lista: ')

lista = []
lista.append(tarefa)

def menu():
  print('\n')
  print('-'*20)
  print('[4] show the lista')
  print('[3] add item to the lista')
  print('[2] remove itens of lista')
  print('[1] mark an item of lista')
menu()

while True:
  sistema = int(input('~ '))
  
  if sistema == 4:
    print('LISTA'.center(20,'-'))
    for indice,tarefa1 in enumerate(lista, start=1):
      print(f'{indice} - {tarefa1}')
    time.sleep(3)
    menu()
      
  elif sistema == 3:
    sistema1 = input('add: ')
    lista.append(sistema1)
    time.sleep(1)
    
    for indice, tarefa1 in enumerate(lista, start=1):
      print(f'{indice} - {tarefa1}')
    time.sleep(3)
    menu()
    
  elif sistema == 2:
    while True:
      try:
        sistema2 = int(input('remove: '))
      except ValueError:
        print('!Invalid Option!')
        break
      except NameError:
        print('Invalid Option!')
        break
      else:
          
          
        remover_item = sistema2 - 1
        
        if 0<= remover_item < len(lista):
          aswer = input('Are you sure? Y/n\n~ ').strip().lower()
          
          if aswer == 'n':
            print('CANCELED')
            break
          
          elif aswer == 'y':
            lista.pop(remover_item)
            for n, item in enumerate(lista, start=1):
              print(f'{n} - {item}')
              break
            break
          
          else:
            print('invalid aswer, please! try again')
        else:
          print('Digita certo mano!')
