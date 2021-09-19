# COVID-19 - Dados clínicos para avaliar o diagnóstico

O texto a seguir, foi retirado da pagina do [Kaggle](https://www.kaggle.com/S%C3%ADrio-Libanes/covid19), e foi transcrito e traduzido.
- [Descrição](#descrição)
- [Contexto](#contexto)
	- [Call to action](#call-to-action)
		* [Tarefa 01](#tarefa-01)
		* [Tarefa 02](#tarefa-02)
- [Os dados](#os-dados)
	- [Etiqueta de saída](#etiqueta-de-saída)
	- [Conceito de janela (window)](#conceito-de-janela-window)
	- [Conjunto de dados](#conjunto-de-dados)
	- [Dados disponível](#dados-disponível)
- [Envio esperado](#envio-esperado)
- [Dúvidas e informações](#dúvidas-e-informações)
- [Kernel Interessante Selecionado](#kernel-interessante-selecionado)
- [Perguntas frequentes](#perguntas-frequentes)
- [Compartilhamento e uso de dados](#compartilhamento-e-uso-de-dados)
- [Dicas e
 truques](#dicas-e-truques)
	- [Dados ausentes](#dados-ausentes)
	- [Quanto mais cedo melhor](#quanto-mais-cedo-melhor)
- [Reconhecimento](#reconhecimento)



# Descrição
## Contexto

A pandemia de COVID-19 atingiu o mundo inteiro, sobrecarregando os sistemas de saúde - despreparados para uma solicitação tão intensa e demorada de leitos de UTI, profissionais, equipamentos de proteção individual e recursos de saúde.

O Brasil registrou o primeiro caso COVID-19 em 26 de fevereiro e atingiu a transmissão na comunidade em 20 de março.

## Call to action 
Há urgência na obtenção de dados precisos para melhor prever e preparar os sistemas de saúde e evitar colapsos, definidos pela necessidade de leitos de UTI acima da capacidade (presumindo-se que haja recursos humanos, EPIs e profissionais disponíveis), utilizando dados clínicos individuais - em vez de dados epidemiológicos e populacionais .
![](https://img.medscape.com/thumbnail_library/cdc_200313_flatten_the_curve_800x450.jpg)


#### Tarefa 01
Prever admissão na UTI de casos confirmados de COVID-19.
Com base nos dados disponíveis, é viável prever quais pacientes precisarão de suporte em unidade de terapia intensiva?
O objetivo é fornecer aos hospitais terciários e trimestrais a resposta mais precisa, para que os recursos da UTI possam ser arranjados ou a transferência do paciente possa ser agendada.

#### Tarefa 02
Prever NÃO admissão à UTI de casos COVID-19 confirmados.
Com base na subamostra de dados amplamente disponíveis, é viável prever quais pacientes precisarão de suporte de unidade de terapia intensiva?
O objetivo é fornecer aos hospitais locais e temporários uma resposta boa o suficiente, para que os médicos de linha de frente possam dar alta com segurança e acompanhar remotamente esses pacientes.

## Os dados
### Etiqueta de saída 
A UTI deve ser considerada, como primeira versão desse conjunto de dados, a variável de destino.

### Conceito de janela (window)
Tivemos o cuidado de incluir cenários da vida real com janela de eventos e dados disponíveis.
Os dados foram obtidos e agrupados

* paciente
-- encontro com o paciente
-- agregado por janelas em ordem cronológica

| Window | Descrição |
|--|--|
| 0-2 | De 0 á 2 horas da admissão |
| 2-4 | De 2 a 4 horas da admissão |
| 4-6 | De 4 a 6 horas da admissão |
| 6-12 | De 6 a 12 horas da admissão |
| Above-12 | Acima de 12 horas da admissão |

* Cuidado para NÃO usar os dados quando a variável de destino estiver presente, pois a ordem do evento é desconhecida (talvez o evento de destino tenha acontecido antes de os resultados serem obtidos). Eles foram mantidos lá para que possamos aumentar este conjunto de dados em outros resultados posteriormente.

Exemplos:


![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F1591620%2Fb1bc424df771a4d2d3b3088606d083e6%2FTimeline%20Example%20Best.png?generation=1594740856017996&alt=media)
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F1591620%2F77ca2b4635bc4dd7800e1c777fed9de1%2FTimeline%20Example%20No.png?generation=1594740873237462&alt=media)



### Conjunto de dados
Este conjunto de dados contém dados anônimos do Hospital Sírio-Libanês, São Paulo e Brasília. Todos os dados foram tornados anônimos de acordo com as melhores práticas e recomendações internacionais.
Os dados foram limpos e escalados por coluna de acordo com o Min Max Scaler para caber entre -1 e 1.

### Dados disponível
1. Informações demográficas do paciente (03)
2. Doenças anteriores agrupadas de pacientes (09)
3. Resultados de sangue (36)
4. Sinais vitais (06)

   No total, são 54 recursos, expandidos quando pertinentes à média, mediana, max, min, diff e diff relativo.
5. diff = max - min
6. diff relativo = diff / mediano


## Envio esperado
Envie um bloco de notas que implemente o ciclo de vida completo de preparação de dados, criação de modelo e avaliação.

## Dúvidas e informações
Use os kernels e a discussão, pois a Equipe Sírio-Libanês de Inteligência de Dados estará respondendo às suas dúvidas.
Dúvidas adicionais, corporativas e esclarecimentos: data.intelligence@hsl.org.br

## Kernel Interessante Selecionado
Soluções interessantes divulgadas neste concurso de conjunto de dados serão convidadas a discutir e apresentar suas descobertas e abordagem a um grupo de pesquisadores e especialistas na área, juntamente com a equipe de ciência de dados do Sírio-Libanês.

# Perguntas frequentes
## Compartilhamento e uso de dados
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F1591620%2Fa6d09844fc8030e0f06f03e0c9e6c76d%2FLicence.png?generation=1587074246329486&alt=media)

## Dicas e Truques
### Dados ausentes
Problema: um dos maiores desafios de trabalhar com dados de saúde é que a taxa de amostragem varia entre os diferentes tipos de medições. Por exemplo, os sinais vitais são coletados com mais frequência (geralmente de hora em hora) do que os laboratórios de sangue (geralmente diariamente).

Dicas e truques: É sensato supor que um paciente que não tem uma medição registrada em uma janela de tempo esteja clinicamente estável, podendo apresentar sinais vitais e exames de sangue semelhantes às janelas vizinhas. Portanto, pode-se preencher os valores ausentes usando a entrada seguinte ou anterior. Atenção aos problemas de multicolinearidade e variância zero nesses dados ao escolher seu algoritmo.

### Quanto mais cedo melhor!
Problema: A identificação precoce dos pacientes que desenvolverão um curso adverso da doença (e precisam de cuidados intensivos) é a chave para um tratamento adequado (salvar vidas) e para gerenciar leitos e recursos.

Dicas e truques: Considerando que um modelo preditivo usando todas as janelas de tempo provavelmente produzirá uma maior precisão, um bom modelo usando apenas o primeiro (0-2) provavelmente será mais clinicamente relevante. A criatividade é muito bem-vinda, sinta-se à vontade com a engenharia de recursos e as janelas de tempo. Atenção às medidas repetidas em indivíduos, uma vez que esses valores são (positivamente) correlacionados ao brincar com os dados.

## Reconhecimento
A Sociedade Beneficiente de Senhoras Sírio-Libanês está comprometida com a filantropia e a ciência para oferecer melhores resultados de saúde aos necessitados. Gostaríamos de agradecer especialmente a nossa equipe jurídica, nosso Instituto de Pesquisa e Educação e o Esquadrão de Arquitetura e Inteligência de Dados Clínico-Radiológicos.
