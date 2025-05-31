## REQUISITOS
embora o código seja simples, ele usa um arquivo de desenho para
deixar a lista de tarefas minimante bonito, então para instalar o figlet
use:
```bash
sudo apt update && sudo apt install figlet
```
---
## Como usar
Após o você instalar o figlet na sua máquina, você pode testar com
```bash
figlet teste
```
logo você vai ver o figlet em ação👍

---
## Criação do desenho
depois disso tudo basta entrar na pasta Downloads do seu sistema
```bash
cd ~/Downloads
{
paste <(figlet -f small "Notas") <(echo "
 ______________________
|   📒 ANOTAÇÕES       |
|----------------------|
|  • Python 🐍         |
|  • Bash 🖥️           |
|  • Café ☕ + Paz 🕊️    |
|                      |
|  Página: 1           |
|______________________|") <(echo "
 /\_/\  
( o.o ) 
 > ^ < 
")
} > desenho.txt
```

---

Pronto, após isso o desenho já pode ser usado, mas é _importante_
lembrar que precisa está sempre na pasta downloads.
---
## Windows
Caso sua distro seja windows ou você esteja com preguiça de ler tudo
isso, eu criei o arquivo que você precisa aqui:

[Download/Desenho](https://github.com/TheRake066/lista-de-tarefa.py/releases/download/Arquivo/desenho.txt)
