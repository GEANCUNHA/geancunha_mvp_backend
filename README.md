#Backend Lista de Tarefas

Estes são os arquivos do frontend do projeto de MVP da disciplina Desenvolvimento Full Stack Básico

Para uma melhor experiencia na execução da aplicação, obtenha tambem os arquivos de Frontend do projeto


## Como executar 

Importante retirar do nome do diretorio o termo "-main" apos dowload do repositorio do github, para garantir o funcionamento da aplicação. O nome do repositorio deve ficar:geancunha_mvp_backend

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz do projeto de backend, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

(env)$ python app.py

Abra o [http://127.0.0.1:5000] verificar a aplicação completa funcionando com o front.

Abra o [http://127.0.0.1:5000/tasks] verificar a documentação das APIs.

Atenção: Caso haja, mesmo apos instalação dos requirments, erros de compartibilidades relacionados ao SQLAlchemy durante a execução do app.py, experimente os seguintes comandos:

pip uninstall Flask-SQLAlchemy
pip uninstall SQLAlchemy

Em seguida:

pip install Flask-SQLAlchemy

Isso deve resolver os problemas de compatibilidade.





