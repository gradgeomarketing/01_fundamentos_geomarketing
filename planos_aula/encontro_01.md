# Plano de aula — Encontro 1

**Unidade:** 1 — Fundamentos de Geomarketing  
**Carga horária:** 4 horas-aula, equivalentes a 200 minutos  
**Período previsto:** agosto de 2026  
**Plataforma prática:** QGIS 3.44 LTR

## Questão orientadora

Por que estabelecimentos da mesma rede, com produtos semelhantes, podem
apresentar desempenhos diferentes em pontos distintos da cidade?

## Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de:

1. explicar geomarketing como integração entre decisões de marketing e
   inteligência geográfica;
2. formular perguntas espaciais aplicadas a mercados;
3. reconhecer aplicações em empresas, setor público e organizações sociais;
4. distinguir datum, coordenadas geográficas e coordenadas projetadas em nível
   introdutório;
5. criar e salvar um projeto QGIS com caminhos relativos;
6. consultar dados do OpenStreetMap no QGIS e produzir um mapa exploratório;
7. distinguir achado cartográfico, hipótese explicativa e conclusão.

## Evidências de aprendizagem

- participação na questão orientadora;
- projeto QGIS que reabre sem caminhos quebrados;
- mapa com elementos cartográficos básicos e atribuição;
- respostas da Atividade 01;
- bilhete individual de saída.

## Preparação docente

1. Executar `scripts/01_preparar_referencia_cefet.py`.
2. Conferir `dados/03_auditoria/amostra_cefet_campus.csv`.
3. Testar a consulta QuickOSM em um perfil limpo do QGIS.
4. Renderizar e abrir `slides/index.html`.
5. Revisar `avaliacao/checklist_pre_aula.md`.
6. Manter `atividades_em_sala/atividade_01_gabarito_docente.md` restrito.

## Programação — 200 minutos

| Intervalo | Duração | Atividade | Estratégia |
|---|---:|---|---|
| 0:00–0:10 | 10 min | Acolhimento, propósito da disciplina e projeto integrador | Exposição breve |
| 0:10–0:25 | 15 min | Questão orientadora: desempenho desigual de unidades semelhantes | Discussão em duplas e plenário |
| 0:25–0:45 | 20 min | Conceito de geomarketing e disciplinas que o sustentam | Exposição dialogada |
| 0:45–1:05 | 20 min | Aplicações e caso de expansão de uma rede de farmácias | Estudo de caso |
| 1:05–1:15 | 10 min | Pausa | — |
| 1:15–1:50 | 35 min | Pensamento espacial e fundamentos cartográficos essenciais | Exposição com perguntas |
| 1:50–2:10 | 20 min | QGIS: interface, projeto, camadas, atributos e SRC | Demonstração |
| 2:10–2:20 | 10 min | Pausa | — |
| 2:20–3:00 | 40 min | Atividade “Mapeando o entorno do CEFET” | Prática em grupos |
| 3:00–3:15 | 15 min | Socialização de achados, divergências e limitações | Plenário |
| 3:15–3:20 | 5 min | Bilhete individual de saída e encerramento | Avaliação formativa |

## Desenvolvimento

### 1. Questão orientadora

Apresente duas unidades hipotéticas de uma mesma rede com desempenho desigual.
Solicite que as duplas proponham explicações. Organize as respostas em quatro
famílias:

- características do mercado;
- acessibilidade e fluxos;
- concorrência e complementaridade;
- características internas da operação.

Conclua destacando que geomarketing não substitui marketing ou finanças: ele
torna explícita a dimensão territorial do problema.

### 2. Fundamentos de geomarketing

Trabalhe:

- espaço como variável estratégica;
- diferença entre “onde estão os clientes?” e “por que estão ali?”;
- escalas de análise;
- integração entre marketing, geografia, estatística e SIG;
- aplicações em localização, cobertura, expansão, logística e políticas
  públicas.

Evite apresentar o primeiro mapa como resposta final. O objetivo é formular um
problema que será enriquecido ao longo das unidades seguintes.

### 3. Fundamentos cartográficos essenciais

Esta é uma introdução; o aprofundamento operacional ocorrerá na Unidade 4.

1. **Pensamento espacial:** localização, distância, direção, distribuição,
   associação e escala.
2. **Forma da Terra:** geoide como referência física e elipsoide como modelo
   matemático.
3. **Datum/SRC:** o sistema de referência permite interpretar coordenadas.
4. **Coordenadas geográficas:** latitude e longitude em graus.
5. **Coordenadas projetadas:** plano cartesiano, frequentemente em metros.
6. **Aplicação local:** SIRGAS 2000 geográfico — EPSG:4674 — e SIRGAS 2000 /
   UTM zona 23S — EPSG:31983 — para análises métricas em Belo Horizonte.
7. **Regra prática:** definir SRC não é o mesmo que reprojetar uma camada.

### 4. Demonstração do QGIS

Mostre apenas os componentes necessários à atividade:

- painel Navegador;
- painel Camadas;
- mapa e barra de status;
- tabela de atributos;
- SRC do projeto;
- salvamento do projeto;
- diferença entre camada temporária e persistida.

Abra a camada do campus e explique que um ponto de referência não representa o
perímetro institucional.

### 5. Prática

Use:

- `praticas_qgis/01_primeiro_mapa_osm.md`;
- `atividades_em_sala/atividade_01_mapeando_entorno_cefet.md`;
- `avaliacao/rubrica_encontro_01.md`.

Durante a prática, registre no quadro três colunas:

| Observamos | Podemos levantar como hipótese | Ainda não podemos concluir |
|---|---|---|
| Feições e vazios no recorte | Relação com vias, fluxos ou centralidades | Demanda, saturação ou viabilidade econômica |

## Resolução e mediação

Não há contagem fixa de farmácias: o resultado depende da data, do recorte e do
estado do OpenStreetMap. A correção deve confrontar as respostas com as
tabelas de atributos produzidas por cada grupo.

Valorize grupos que:

- informam o recorte utilizado;
- reconhecem pontos e polígonos retornados;
- evitam dupla contagem;
- apresentam explicações concorrentes;
- pedem dados adicionais antes de recomendar localização.

Intervenha quando houver:

- inferência causal baseada apenas em proximidade visual;
- uso de distância em graus como se fosse metro;
- ausência de atribuição ao OSM;
- afirmação de que área sem feição não possui farmácia.

## Recursos

- computador e projetor;
- QGIS 3.44 LTR;
- plugin QuickOSM;
- internet;
- slides renderizados;
- camada de referência do Campus Nova Gameleira;
- roteiro prático e atividade discente.

## Limitações e contingência

- A API Overpass pode ficar indisponível ou limitar consultas.
- O OSM é colaborativo e pode apresentar omissões ou classificações
  inconsistentes.
- O mapa-base não constitui cadastro completo de empresas.
- Se a consulta falhar, realizar a leitura do mapa-base e registrar a falha,
  sem substituir o resultado por contagens presumidas.

## Articulação com as demais unidades

- Unidade 2: espaço, centralidade, consumo e acessibilidade.
- Unidade 3: fontes, qualidade, escala e limitações dos dados.
- Unidade 4: estruturas espaciais, SRC e operações essenciais.
- Unidade 5: geocodificação e preparação de endereços.
- Unidade 6: cartografia temática e comunicação visual.
- Unidade 7: distância, cobertura e áreas de influência.
- Unidade 8: indicadores, segmentação e potencial de mercado.

## Para o próximo encontro

- Manter o projeto `encontro_01.qgz`.
- Registrar uma pergunta territorial que o grupo deseja investigar.
- Ler a introdução indicada no ambiente da disciplina.
- Não é necessário instalar MMQGIS ou ORS Tools nesta etapa; esses plugins serão
  introduzidos quando suas funções forem utilizadas.

## Referências operacionais

- QGIS Project. *QGIS 3.44 User Guide*.
- QuickOSM. *End User Guide*.
- OpenStreetMap Foundation. *Copyright and License*.
- CEFET-MG. Endereço do Campus Nova Gameleira.

