## Créditos desse exemplo à Dinei Rockenbach e ao grupo Larcc: <br> https://github.com/larcc-group/escola-inverno-2022-docker/tree/main/1.site-flask

# Preparando uma imagem própria do site

É muito trabalhoso preparar o container sempre que se quer executar o site, então é muito melhor deixá-lo preparado (com Flask instalado, por exemplo) e simplesmente executar a imagem com o site já embutido nela. Para isso, vamos criar um arquivo `Dockerfile` com o seguinte conteúdo:

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /home
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

Esses comandos especificam uma imagem construída com praticamente os mesmos comandos que fizemos antes diretamente no container: a partir da imagem do Python 3.7 (`FROM python:3.7-alpine`), vamos trabalhar na pasta `/home` (`WORKDIR /home`), vamos usar um arquivo `requirements.txt` (`COPY requirements.txt requirements.txt`) com a lista de pacotes do pip que precisamos (`RUN pip install -r requirements.txt`), que no caso é só o Flask, mas é uma boa prática usar este arquivo para listar os pacotes, e vamos expor a porta 5000 (`EXPOSE 5000`). Por fim, vamos copiar todos os arquivos do site para dentro do container (`COPY . .`) e automaticamente executar `flask run` quando o container for iniciado (`CMD ["flask", "run"]`). Aqui nós usamos uma variável de ambiente para definir o host (`ENV FLASK_RUN_HOST=0.0.0.0`) e o arquivo (`ENV FLASK_APP=app.py`) que o Flask vai executar, mas é efetivamente a mesma coisa que fizemos antes passando `--host 0.0.0.0` no comando `flask run`.

Com este arquivo `Dockerfile`, podemos construir uma imagem do nosso site:

```bash
docker build -t meu-site-flask:latest .
```

Com a flag `-t`, demos o nome de `meu-site-flask` (e a tag `latest`) para a imagem que estamos construindo. Neste momento o Docker já vai executar os comandos para instalar o Flask (`pip install`) e copiar os arquivos do site para dentro da imagem. Depois, quando quisermos executar o site basta executarmos:

```bash
docker run -it -p 5000:5000 meu-site-flask:latest
```

Pronto, agora acessando a porta 5000 do nosso computador pelo navegador ([http://localhost:5000/](http://localhost:5000/)) poderemos ver o site rodando no container com a imagem que preparamos.

Note que não precisamos dar acesso aos arquivos do site com a flag `-v`, pois os arquivos do site já estão dentro da imagem. As configurações de pasta (`/home`) também já estão prontas, e não precisamos usar o terminal (`/bin/sh`) para executar o Flask pois a imagem já está preparada para rodar ele automaticamente. A flag `-it` nesse caso é opcional, apenas para podermos ver os logs do servidor Flask sendo executado. Apesar de termos identificado a porta 5000 no Dockerfile, ainda precisamos mapear ela no `docker run`, pois o Docker nos permite escolher a porta que será vinculada no momento da execução.

Caso queira verificar o resultado final no seu computador sem precisar compilar a imagem, ela está disponível já compilada no repositório de pacotes do GitHub:

```bash
docker run -it -p 5000:5000 ghcr.io/larcc-group/escola-inverno-2022-docker:1-site-flask
```
