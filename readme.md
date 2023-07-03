# Gerenciador Escolar
## CRUD em Python Utilizando Django Rest Framework

#### Este projeto é um sistema de gerenciamento escolar que permite cadastrar, consultar, atualizar e excluir alunos, cursos e matrículas. O sistema utiliza o framework Django REST para criar uma API REST que expõe os recursos do modelo de dados. O sistema utiliza o banco de dados PostgreSQL para armazenar as informações. 

O desenvolvimento desse projeto está sendo realizado a partir das resolução das atividades da trilha de formação [Django REST APIs: crie aplicações REST em Python](https://cursos.alura.com.br/formacao-django-rest) da escola de tecnologia [Alura](https://www.alura.com.br/sobre). A estrutura básica, e principais funcionalidades foram proposta nas atividades, porém até a conclusão desse projeto, será implementado diversas outras que não estavam prevista no escopo da trilha de formação.


## :dart: Objetivos

Esse projeto tem como objetivo implementar técnicas de desenvolvimento de tecnologia para web, utilizando a linguagem Python e o framework Django.

| :placard: Vitrine.Dev |                                         |
| --------------------- | --------------------------------------- |
| :sparkles: Nome       | **Gerenciador escolar**                 |
| :label: Tecnologias   | python, django, django rest, postgresql |
| :rocket: URL          |                                         |
| :fire: Desafio        |                                         |

<!-- Inserir imagem com a #vitrinedev ao final do link -->
![](https://github.com/MaercioMamedes/drf-gerenciador-escolar/blob/master/docs/images/capa_vitrine-dev.png#vitrinedev)

## :pencil: Funcionalidades da aplicação

- :arrow_forward: -----> Em Desenvolvimento
- :x: -----> Não implementado
- :heavy_check_mark: -----> Implementado

| ITEM  |      ATIVO      |     FUNCIONALIDADE     |                               DESCRIÇÃO                               |
| :---: | :-------------: | :--------------------: | :-------------------------------------------------------------------: |
|   1   | :arrow_forward: |       CRUD Aluno       |          Criação, leitura, edição e exclusão da classe Aluno          |
|   2   | :arrow_forward: |       CRUD Curso       |          Criação, leitura, edição e exclusão da classe Curso          |
|   3   |       :x:       |     CRUD Matrícula     |        Criação, leitura, edição e exclusão da classe Matrícula        |
|   4   |       :x:       |     CRUD Professor     |        Criação, leitura, edição e exclusão da classe Professor        |
|   5   |       :x:       |    CRUD Funcionario    |       Criação, leitura, edição e exclusão da classe Funcionário       |
|   6   |       :x:       |    Busca de Alunos     |                    Buscar objetos da classe alunos                    |
|   7   |       :x:       | Validação de requisção | Validação das entradas de dados para criação e atualização de objetos |



## :computer: Building

* Versão das principais tecnologias utilizadas:


  * Python 3.10.6
  * Postgresql 15.3

Para rodar essa aplicação, é necessário ter uma conexão com um banco de dados já configurado dentro do projeto. Para este, foi utilizado o Postgresql versão 15.3. Caso, não tenha o Postgresql instalado em sua máquina, é possível rodar o projeto com um banco de dados SQLite. Para isso, é preciso ir dentro do diretório `setup/settings.py`e susbistituir o valor da variável `DATABASES` para:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
```

* realize o clone do repositório - `git clone https://github.com/MaercioMamedes/drf-gerenciador-escolar.git`
* [crie um ambiente virtual dentro do diretório do projeto e instale todas as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
  * as dependências necessárias para rodar o projeto, estão listadas no arquivo requirements.txt
* rode o comando `python manage.py runserver`

### :airplane: Endpoints


|               URI               |    MÉTODO    |                      RECURSO                       |
| :-----------------------------: | :----------: | :------------------------------------------------: |
|             /alunos             |     GET      |               lista todos os alunos                |
|             /alunos             |     POST     |                  Cria novo aluno                   |
|      /alunos/{ aluno_id }       |     GET      |                   retorna aluno                    |
|      /alunos/{ aluno_id }       | PUT ou PATCH |                   atualiza aluno                   |
|      /alunos/ { aluno_id }      |    DELETE    |                    exclui aluno                    |
| /alunos/{ aluno_id }/matriculas |     GET      | retorna lista cursos que o alunos está matriculado |
|             /cursos             |     GET      |               lista todos os cursos                |
|             /cursos             |     POST     |                 cria um novo curso                 |
|      /cursos/{ curso_id }       |     GET      |                   retorna curso                    |
|      /cursos/{ curso_id }       | PUT ou PATCH |                   atualiza curso                   |
|      /cursos/{ curso_id }       |    DELETE    |                    exclui curso                    |
| /cursos/{ curso_id }/matriculas |     GET      |   retorna lista de alunos matriculados no curso    |
|           /matriculas           |     GET      |               lista todas matriculas               |
|           /matriculas           |     POST     |                cria nova matrícula                 |
|  /matriculas/{ matricula_id }   |     GET      |                 retorna matrícula                  |
|  /matriculas/{ matricula_id }   | PUT ou PATCH |                 atualiza matricula                 |
|  /matriculas/{ matricula_id }   |    DELETE    |                  exclui matricula                  |


### :closed_lock_with_key: Estruturas de dados

#### CRIANDO CURSO

```
{
    "codigo_curso": "CÓDIGO DO CURSO",
    "descricao": "DESCRIÇÃO DO CURSO",
    "nivel": "B"
}

    # VALORES possíveis PARA A VARIÁVEL  nível
    
    {
      'B': 'Básico',
      'I': 'Intermediário',
      'A': 'Avançado',
    }

```

#### CRIANDO ALUNO

```
{
    "nome": "nome_aluno",
    "rg": "rg_aluno",
    "cpf": "cpf_aluno",
    "data_nascimento": "YYYY-MM-DD",
}

```