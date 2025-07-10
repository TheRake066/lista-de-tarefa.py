# requisito: sudo apt install figlet

import time
import subprocess
import shelve
import sys
import emoji
import traceback

print('-'*20)
subprocess.run(["cat","desenho.txt"])
print('-'*20)

def mostrar_lista():
    with shelve.open('lista') as db:
        linha_maior = max(
            len(f"{i+1} - {t.split(':', 1)[0].strip()}: {emoji.emojize(t.split(':', 1)[1].strip())}")
            for i, t in enumerate(db['tarefas'])
        )

        devagar(f'  ' + 'LISTA'.center(linha_maior, '_'))
        print('#|' + " ".center(linha_maior,' ') + '|')
        if db['tarefas'] == []:
            print(f'#|'+'!Nada criado!'.center(linha_maior, ' ') + '|')

        for indice, tarefa in enumerate(db['tarefas'], start=1):
            tarefa_texto, emoji_codigo = tarefa.split(":", 1)
            emoji_real = emoji.emojize(emoji_codigo.strip())
            linha = f'{indice} - {tarefa_texto.strip()}: {emoji_real}'
            print(f"#|{linha.center(linha_maior)}|")
        print('#|' + " ".center(linha_maior,' ') + '|')
        print('#|' + "".center(linha_maior,'_') + '|')
        

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
devagar(' Digite 4 para ver a lista;\n digite 3 para adicionar a lista;\n digite 2 para remover algo da lista com base em seu numero;\n digite 1 para alterar os status da tarefa')

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
            carregamento(titulo='carregando lista', seg=2)
            print('\n')
            with shelve.open('lista') as db:
                if 'tarefas' not in db:
                    print('    !LISTA AINDA NÃO CRIADA!\n    !ADICIONE ALGO!')
                else:
                    mostrar_lista()
                    menu()

        elif sistema == 3:
            while True:
                with shelve.open('lista', writeback=True) as db:
                    if 'tarefas' not in db:
                        db['tarefas'] = []
                        devagar('LISTA CRIADA!')
                    sistema1 = input('[0]cancelar\nadd: ').lower().strip()
             
                    if sistema1 == '0':
                        print('!cancelado!')
                        break

                    existe = any(item.split(':')[0] == sistema1 for item in db['tarefas'])
                    
                    if existe:
                        print('!ITEM JÁ EXISTE!')
                        continue

                    db['tarefas'].append(f'{sistema1}: :check_mark_button:')
                    db.sync()
                    time.sleep(1)
                    mostrar_lista()
                    time.sleep(3)
                    break
                menu()
    
        elif sistema == 2:
            while True:
                try:
                    sistema2 = int(input('remove: '))
                except ValueError:
                    print('!Invalid Option!')
                else:
                    remover_item = sistema2 - 1
                    with shelve.open('lista', writeback=True) as db:            
                        if 0<= remover_item < len(db['tarefas']):
                            aswer = input('Are you sure? Y/n\n~ ').strip().lower()
          
                            if aswer == 'n':
                                print('CANCELED')
                                break
          
                            elif aswer == 'y':
                                teste = db['tarefas']
                                teste.pop(remover_item)
                                db['tarefas'] =teste
                                mostrar_lista()
                        else:
                            print('invalid aswer, please! try again')
                    break
        elif sistema == 1:
            while True:
                try:
                    sistema3 = int(input('numero do item: '))
                except ValueError:
                    print('!Invalid Option!')
                else:
                    sistema4 = input('\n[1] feito\n[2] pendente\n[3] não feito\nnovo status: ')
                    substituir_item = sistema3 - 1

                    with shelve.open('lista', writeback=True) as db:
                        if 0 <= substituir_item < len(db['tarefas']):
                            item = db['tarefas'][substituir_item]
                            tarefa, _ = item.split(":", 1)

                            if sistema4 == '1':
                                novo = f"{tarefa.strip()}: {':check_mark_button:'}"
                                db['tarefas'][substituir_item] = novo

                            elif sistema4 == '2':
                                novo = f"{tarefa.strip()}: {':minus:'}"
                                db['tarefas'][substituir_item] = novo
                            
                            elif sistema4 == '3':
                                novo = f"{tarefa.strip()}: {':cross_mark:'}"
                                db['tarefas'][substituir_item] = novo

                            db.sync()
                            mostrar_lista()
                            break
                        else:
                            print('deu merda!')
                    
        elif sistema == 0:
            carregamento(titulo='saindo', seg=1)
            break
    except ValueError:
        print(f'!Precisa ser um numero do Menu!')
