# Asteroids
Projeto realizado durante graduação na Universidade Presbiteriana Mackenzie.
Jogo asteroids em python, refatorado em microserviços, seguindo os princípios SOLID:
As classes recebem heranças de classes base abstratas de responsabilidade única, sem problemas de segregação de interfaces, as classes base podem ser substituídas por suas classes derivadas sem problemas, e, por fim, nenhuma classe depende de implementações concretas, apenas de abstrações.

Como python não aceita importação cíclica, são usadas instâncias como parâmetros para classes com hierarquia.
