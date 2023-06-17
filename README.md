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

Comandos para preparar o ambiente em uma máquina virtual (VSP) Linux:

```bash
sudo apt install curl
sudo apt install wget
sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
sudo apt install python3-flask
git clone https://github.com/danielscarvalho/flask-local.git
cd flask-local
sh ./run.sh
```

- No Oracle Cloud o firewall **iptables** já vem instalado por padrão no servidor (VPS), tem que liberar a porta 5000
- Tem que liberar a porta 5000 no firewall, normalmente há uma interface WEB administrativa para isso
- Note que importamos o projeto usando HTTPS do GitHub. Apenas para não ter que criar e registrar uma chave ssh no servidor (VPS - maquina virtual)
- Estas operações podem ser bloqueadas pelo Proxy/Firewall da empresa ou faculdade... o sistema pode identificar como uma ameaça ou ataque hacker
- O acesso a nossa WEB API com Flask não em SSL (segurança) implementado, não tem senha nem token e nem criptografia

Este serviço temporário está acessível em:

http://lab.code.eng.br:5000/
