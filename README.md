# trabalhoextrafp
1135335 - Alan Godoi
1134870 - Guilherme Tagliari


resumo:
O código simula o download de vários arquivos em paralelo, usando threads para que cada download ocorra "ao mesmo tempo". Após a conclusão de todos os downloads, o programa imprime uma mensagem final.

passo a passo:

passo 1: importação dos módulos
'threading' módulo permite criar e controlar múltiplas threads, que são linhas de execução separadas.
'time' esse fornece funções relacionadas ao tempo, como pausas na execução (sleep).
'random' ele é usado para gerar números aleatórios, o que neste código simula tempos de download variados.

passo 2: simular a função 
 Quando a função é chamada, o programa imprime uma mensagem indicando que o download do arquivo file_name começou.
 A função então usa random.randint(1, 5) para escolher aleatoriamente um número entre 1 e 5, representando quantos segundos o download levará.
 O programa faz uma pausa (time.sleep(time_to_download)) por essa quantidade de segundos, simulando o tempo necessário para o download.
 Após ter tido a pausa, a função imprime uma mensagem indicando que o download foi concluído, mencionando o tempo gasto.

 passo 3: definição da função 'main()'
  ele gerencia a criação e execução das threads
  define uma lista com 'files'
  cria umas lista vazia 'threads' para armazenar os threads que serão criadas

  passo 4: criar uma thread separada que simula do dwnld do arquivo
  o código percorre a lista 'files'
  para cada arquivo, o código cria uma nova thread
  Cada thread criada é adicionada à lista threads, e a execução da thread é iniciada imediatamente com thread.start().

passo 5:   esperar a conclusão de todos os threads
garantir que o programa so continue quando todos os downloads estiverem concluidos
o programa fica em um loop, até todos estiverem concluidos

passo 6: é informar que todos os downloads foram concluidos 

apos ele concluir todos os downloads ele imprime uma mensagem

passo 7: é o programa ser executado

o código verifica se o script que está sendo executado diretamente e, se estiver, chama a função main() para poder inciar o processo
 

