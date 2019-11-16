# App Venda de Ingressos em DJANGO

<h4 align="center">
  ☕ Web App em DJANGO para venda de ingressos um evento local.
</h4>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/brendonhc/venda-de-ingressos.svg">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/brendonhc/venda-de-ingressos.svg">
  
  <a href="https://github.com/brendonhc/venda-de-ingressos/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/brendonhc/venda-de-ingressos.svg">
  </a>

  <a href="https://github.com/brendonhc/venda-de-ingressos/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/brendonhc/venda-de-ingressos.svg">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
</p>

<p align="center">
  <a href="#motivação">Motivação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#como-usar">Como Usar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#implementação">Implementação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rodando-localmente">Rodando Localmente</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#subindo-no-heroku">Subindo no Heroku</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#licença">Licença</a>
</p>

Disponível em: https://venda-de-ingressos.herokuapp.com/

## Motivação

Uma disciplina de Bases de Dados que fiz durante a graduação me solicitou modelar toda a arquitetura de dados que envolvia a logística do evento com Modelos Entidade-Relacionamento e a criação das tabelas em SQL de fato, e por fim, foi necessário a implementação de um aplicativo em qualquer tecnologia que fizesse consultas nessa base de dados, então, desenvolvi essa aplicação para cuidar da parte de ingressos para os shows disponíveis no evento.

## Implementação

A implementação foi feita em cima do framework [*DJANGO*](https://www.djangoproject.com/), dentro dele codifiquei *templates* em [*HTML5*](https://developer.mozilla.org/pt-BR/docs/Web/HTML/HTML5) para estruturar as páginas do aplicativo e seus campos de entrada e saída de dados, [*Bootstrap*](https://getbootstrap.com/) para estilizar de maneira bonita e resposíva, toda a lógica do tratamento dos dados feita em [*Python*](https://www.python.org/), base de dados [PostgreSQL](https://www.postgresql.org/), e por fim, utilizei o [*Heroku*](https://www.heroku.com/) para fazer deploy da aplicação e tê-la disponível online em qualquer navegador.

## Rodando Localmente

Certifique-se de ter a versão do Python 3.7 [instalada localmente](http://install.python-guide.org). Para subir no Heroku, instale o [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), da mesma forma para o [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Agora o aplicativo estará disponível em [localhost:5000](http://localhost:5000/).

## Subindo no Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
ou

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.
