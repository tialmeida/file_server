# Cliente-Servidor para envio e recebimento de arquivos

> :technologist: Aluno: Tiago Almeida Santos - 2022134470

Esse trabalho tem o objetivo de criar um servidor que compartilhe arquivos com clientes simultaneamente. 
Quaisquer arquivos disponíveis na máquina onde o servidor será executado podem ser compartilhados, basta passar por parâmetro a pasta contendo os arquivos.
<br>O cliente pode solicitar quaisquer arquivos disponíveis na pasta compartilhada e pode também listar os arquivos disponíveis. 

A tecnologia selecionada foi a Linguagem Python com algumas bibliotecas. Sendo elas:
- os
- socket
- sys
- _thread
- tqdm

## Instruções de uso
1. Instale o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download);
2. Execute o comando `pip install tqdm`;
3. Execute o arquivo [server.py](code/server.py) utilizando o comando `python client.py port directory_of_files_to_share`;
4. Execute o arquivo [client.py](code/client.py) utilizando os comandos abaixo.

### Comandos cliente
Para iniciar o cliente é necessário utilizar um dos dois comandos abaixo:
1. :arrow_down: Solicita o download do arquivo `python client.py host port directory_of_file directory_to_save`
2. :page_facing_up: Lista os arquivos do servidor `python client.py host port list` 

## O Projeto
Não foi adotado nenhum padrão arquitetural por se tratar de uma aplicação simples que se assemelha muito a uma POC (prova de conceito).
Contudo, foi feita a separação de responsabilidades.
<br>Foi criado um arquivo para conter valores padrões que precisavam ser compartilhados entre cliente e servidor, sem a necessidade de manter esses valores nos dois arquivos. Um arquivo de constantes, [utils.py](code/utils.py).
<br>No lado do cliente a aplicação é bem simples e se resumiu ao arquivo [client.py](code/client.py) que se conecta ao servidor, envia o comando, obtém uma resposta segundo o que foi solicitado e com os possíveis erros.
<br>Quanto ao servidor, existe um model para os arquivos em cache, [file_in_cache.py](code/file_in_cache.py)
<br>Há também um arquivo para gerenciar a memória cache, ele é responsável por adicionar arquivos, limpar a memória, liberar espaço para novos arquivos, verificar se o arquivo existe na memória e obter o arquivo solicitado, sendo o arquivo [memory_cache.py](code/memory_cache.py).
<br>E o arquivo [server.py](code/server.py) é o orquestrador do que acontece do lado do servidor. Além de ouvir uma porta e aceitar novas conexões, ele lida com os comandos do cliente e responde de acordo. No caso do comando de obtenção de arquivo, ele faz a orquestração com a memória cache para obter o arquivo ou adicionar.
<br>Quase todo o projeto foi feito usando código imperativo, exceto a memória cache e seu model que foi utilizada a Orientação a Objetos.