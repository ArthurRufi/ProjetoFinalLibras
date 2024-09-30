# Backend provisorio do projeto Glossario Libras do Thiago Paiva

    Projeto desenvolvido por Arthur Santana de maneira voluntaria.
    O projeto Glossario preve atender todas as demandas necessarias previstas em sua tese de mestrado

# Documentação

    Projeto desenvolvido em Django, Django Rest Framework e PostgreSQL.

## Apps
    A logica dos apps foi colocada em Sinal, paginaprincipal, interpretes, curso e libras.

    Sinal:
        Responsavel por toda a logica e regras de negocios referentes ao sinais.
    Interpretes:
        Responsavel por toda  a logica relacionada aos Interpretes
    Curso:
        Responsavel por toda a logica relacionada aos Cursos, materia e sinais.
    Libras:
        app do projeto principal cuidando das logicas centrais.

# Arquitetura

    A arquitetura segue a seguinte:
        Backend
            Servidor: Apache
            Banco de Dados: PostreSQL (SQL)
            Cache: MemCached
            Linguagem: Python com Django e DRF



        Frontend: 
            Provisoriamente sendo entregue pelo backend mas com possibilidade de atualização para React.
            Proposta: React 