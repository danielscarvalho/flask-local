# Insper
## Deploy

Projeto básico em Flask

WEB API

Dica:

Documentação do Flask: https://flask.palletsprojects.com/en/2.3.x/

Por algum motivo esotérico, tive que instalar o flask no meu ambiente Linux da seguinte forma:

```bash
$ sudo apt install python3-flask
```
____

## Dicas

Comandos para preparar o ambiente em uma máquina virtual (VSP):

```bash
sudo apt install curl
sudo apt install wget
sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
sudo apt install python3-flask
git clone https://github.com/danielscarvalho/flask-local.git
cd flask-local
sh ./run.sh
```
