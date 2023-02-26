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

