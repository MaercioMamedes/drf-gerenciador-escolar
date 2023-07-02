# Gerenciador Escolar
## CRUD em Python Utilizando Django Rest Framework

#### Este projeto é um sistema de gerenciamento escolar que permite cadastrar, consultar, atualizar e excluir alunos, cursos e matrículas. O sistema utiliza o framework Django REST para criar uma API RESTful que expõe os recursos do modelo de dados. O sistema utiliza o banco de dados PostgreSQL para armazenar as informações. 

| :placard: Vitrine.Dev |                                         |
| --------------------- | --------------------------------------- |
| :sparkles: Nome       | **Gerenciador escolar**                 |
| :label: Tecnologias   | python, django, django rest, postgresql |
| :rocket: URL          |                                         |
| :fire: Desafio        |                                         |

<!-- Inserir imagem com a #vitrinedev ao final do link -->
![](https://github.com/MaercioMamedes/drf-gerenciador-escolar/blob/master/docs/images/capa_vitrine-dev.png#vitrinedev)

## Detalhes do projeto




### Endpoints


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


### Estruturas de dados

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