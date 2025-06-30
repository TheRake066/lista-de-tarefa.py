# requisito: sudo apt install figlet

import time
import subprocess
import shelve
import sys
import emoji

print('-'*20)
subprocess.run(["cat","desenho.txt"])
print('-'*20)

def mostrar_lista():

    devagar(f'  ' + 'LISTA'.center(18, '_'))
    print('#|' + " ".center(18,' ') + '|')
    with shelve.open('lista') as db:
        if db['tarefas'] == []:
            print(f'#|'+'!Nada criado!'.center(18, ' ') + '|')

        for indice, tarefa in enumerate(db['tarefas'], start=1):
            print(emoji.emojize(f"#|{f'•{indice} - {tarefa}'.center(35)}|"))
        print('#|' + " ".center(18,' ') + '|')
        print('#|' + "".center(18,'_') + '|')
        

def carregamento(titulo='', seg=3):
    for i in range(seg*4):
        pontos = '.'*(i % 4)
        sys.stdout.write(f'\r{titulo}{pontos}')
        sys.stdout.flush()
        time.sleep(0.25)

def devagar(texto, delay=0.03):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()
time.sleep(1)
print('MANUAL: ')
devagar(' Digite 4 para ver a lista;\n digite 3 para adicionar a lista;\n digite 2 para remover algo da lista com base em seu numero.')

def menu():
  print('\n')
  print('-'*20)
  print('[4] show the lista')
  print('[3] add item to the lista')
  print('[2] remove itens of lista')
  print('[1] mark an item of lista')
  print('[0] leave')
menu()

while True:
    try:
        sistema = int(input('menu ~ '))
  
        if sistema == 4:
            carregamento(titulo='carregando lista')
            print('\n')
            with shelve.open('lista') as db:
                if 'tarefas' not in db:
                    print('    !LISTA AINDA NÃO CRIADA!\n    !ADICIONE ALGO!')
                else:
                    mostrar_lista()
                    menu()

        elif sistema == 3:
            with shelve.open('lista') as db:
                sistema1 = input('add: ').lower()
                if not 'tarefas' in db:
                    db['tarefas'] = []
                    devagar('LISTA CRIADA!')
                existe = any(item.split(':')[0] == sistema1 for item in db['tarefas'])
            
                if not existe:
                    db['tarefas'] = db['tarefas'] + [f'{sistema1}::check_mark_button:']

                time.sleep(1)
                mostrar_lista()
                time.sleep(3)
            menu()
    
        elif sistema == 2:
            while True:
                try:
                    sistema2 = int(input('remove: '))
                except ValueError:
                    print('!Invalid Option!')
                else:
                    remover_item = sistema2 - 1
                    with shelve.open('lista') as db:            
                        if 0<= remover_item < len(db['tarefas']):
                            aswer = input('Are you sure? Y/n\n~ ').strip().lower()
          
                            if aswer == 'n':
                                print('CANCELED')
                                break
          
                            elif aswer == 'y':
                                teste = db['tarefas'].copy()
                                teste.pop(remover_item)
                                db['tarefas'] = teste
                                mostrar_lista()
                        else:
                            print('invalid aswer, please! try again')
                    break
        elif sistema == 0:
            carregamento(titulo='saindo', seg=1)
            break
    except ValueError:
        print('!Precisa ser um numero do Menu!')
