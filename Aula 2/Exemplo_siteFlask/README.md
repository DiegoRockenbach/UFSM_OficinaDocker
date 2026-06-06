## Créditos desse exemplo à Dinei Rockenbach e ao grupo Larcc: <br> https://github.com/larcc-group/escola-inverno-2022-docker/tree/main/1.site-flask

# Exemplo de site simples usando Flask

Este é um exemplo de site simples usando o Flask. O código do website usando Flask está no arquivo [`app.py`](app.py). Ele simplesmente renderiza o template HTML do arquivo [`index.html`](templates/index.html).

Abaixo vamos ver como:
- Executar o site usando a [imagem do Python 3.7 no Linux Alpine do Docker Hub](https://hub.docker.com/_/python)

### Usando a imagem do Python 3.7 no Linux Alpine do Docker Hub

Primeiramente, execute o container com a imagem do Python, permitindo que ele acesse a pasta com o arquivo `app.py`. Esse acesso é fornecido através da flag `-v`, onde você deve passar o caminho da pasta atual. Por exemplo, se o projeto está na pasta C:/Projetos/1.site-flask, você deve trocar `-v <pasta>:/home` no comando abaixo por `-v "C:/Projetos/1.site-flask:/home"`.

```bash
docker run -it -v "<pasta>:/home" -w /home -p 5000:5000 python:3.7-alpine /bin/sh
```

Efetivamente, este comando vai baixar a imagem Docker `python:3.7-alpine` do Docker Hub (se você não tiver a imagem na sua máquina), executar um container com ela, e abrir um terminal para executarmos mais comandos dentro do container. Explicações sobre o comando:  
- `docker run`/`docker container run` - indica ao Docker que queremos que ele crie e execute um novo container.
- `-it` - indica que queremos um container interativo, porque vamos executar mais comandos nele.
- `-v "<pasta>:/home"` - conforme vimos acima, dá acesso ao container à pasta atual. Efetivamente criamos um atalho para a pasta do nosso computador no caminho `/home` do container.
- `-w /home` - indica ao container que vamos trabalhar na pasta `/home` (que o comando anterior já definiu que é um atalho para os nossos arquivos).
- `-p 5000:5000` - o Flask roda o site na porta 5000, portanto essa parte indica ao Docker para vincular a porta 5000 da nossa máquina para a porta 5000 do container.
- `python:3.7-alpine` - é a imagem e tag do Docker Hub que vamos usar no container. Veja no Docker Hub mais detalhes sobre a imagem Python: [https://hub.docker.com/_/python](https://hub.docker.com/_/python).
- `/bin/sh` - queremos abrir um terminal linux (`sh`) dentro do container para executarmos mais comandos

Feito isso, agora vamos instalar o Flask dentro do container com o comando:

```bash
pip install flask
```

Este comando instala o Flask usando o gerenciador de pacotes do Python, o [pip](https://pypi.org/project/pip/). Após a instalação do Flask, podemos executá-lo com o comando:

```bash
flask run --host 0.0.0.0
```

Pronto, agora acessando a porta 5000 do nosso computador pelo navegador ([http://localhost:5000/](http://localhost:5000/)) poderemos ver o site rodando no container que preparamos.

Para parar o servidor, basta apertar Ctrl+C. Depois, digitando o comando `exit` você sai do container. O container que você criou vai continuar existindo, você pode ver ele com `docker container ls -a`, e apagar ele com `docker container rm <nome>`.