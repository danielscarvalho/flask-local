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

- No Oracle Cloud o firewall iptables já vem instalado por padrão no servidor (VSP), tem que liberar a porta 5000
- Tem que liberar a porta 5000 no firewall, normalmente há uma interface WEB administrativa para isso
- Note que importamos o projeto usando HTTP do GitHub, apenas para não ter que criar e registrar uma chave ssh para o servidor (VSP) do GitHub
