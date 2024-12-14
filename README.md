# Busca por Vulnerabilidades com Desafios de Código em Python - Dio Santander Bootcamp Cibersegurança #2
Este repositório reúne as soluções dos desafios propostos no Santander Bootcamp Cibersegurança #2. Os desafios focam na identificação de vulnerabilidades em sistemas, explorados por meio de exercícios práticos com código em Python. São dois desafios onde cada um aborda uma parte específica no contexto da Cibersegurança.

# Primeiro Desafio - Detecção de Phishing por Padrões de E-mail

## Descrição
Crie uma solução para analisar uma lista de e-mails recebidos, verificando padrões comuns de phishing nas mensagens. Se um e-mail contiver palavras suspeitas como "ganhe", "prêmio", "urgente", "desconto", "click" e "promoção" ele deve ser classificado como "Phishing" e "Seguro".

## Entrada
Uma String contendo um conteúdo único representando o corpo do e-mail.

## Saída
"Phishing" ou "Seguro" para cada e-mail.

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                                    | Saída                   |
|--------------------------------------------|-------------------------|
| Ganhe um prêmio incrível hoje!             | Classificação: Phishing |
| Não perca esta promoção exclusiva!         | Classificação: Phishing |
| Você está convidado para a reunião amanhã! | Classificação: Seguro   |

* Primeiro Desafio: Concluído em 14 de dezembro de 2024.

# Segundo Desafio - Detecção de Tentativas de Invasão em Logs

## Descrição
Você é responsável por implementar um sistema de monitoramento de segurança para um sistema de acesso. Seu objetivo é analisar registros de log de tentativas de acesso para detectar possíveis invasões. Cada registro contém um identificador de usuário e um status que indica se a tentativa de acesso foi bem-sucedida ou falhou.
A detecção de tentativas de invasão é essencial para a segurança do sistema, e a análise de logs é uma prática comum para identificar comportamentos suspeitos. O sistema deve emitir um alerta se detectar mais de 3 tentativas consecutivas de falha para o mesmo usuário.

## Entrada
Uma lista de registros de log no formato id_usuario:status, onde:

* id_usuario é uma string que representa o identificador do usuário (exemplo: "user1").

* status pode ser uma das seguintes strings:

"sucesso" – indica que a tentativa de acesso foi bem-sucedida.

"falha" – indica que a tentativa de acesso falhou.

A lista pode conter qualquer número de registros.

## Saída
O sistema deve retornar:

* O id_usuario que teve mais de 3 tentativas consecutivas de falha.

* Se nenhum usuário tiver mais de 3 tentativas de falha consecutivas, o sistema deve retornar a mensagem "Nenhum invasor detectado".

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                                                           | Saída                    |
|-------------------------------------------------------------------|--------------------------|
| user1:falha, user1:falha, user1:falha, user1:sucesso              | Nenhum invasor detectado |
| user2:falha, user2:falha, user2:falha, user2:falha                | user2                    |
| user3:sucesso, user3:falha, user3:falha, user3:falha, user3:falha | user3                    |

* Segundo Desafio: Concluído em 14 de dezembro de 2024.
