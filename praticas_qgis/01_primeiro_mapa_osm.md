# Prática QGIS 01 — Mapeando o entorno do CEFET

## Objetivo

Criar o primeiro projeto QGIS da disciplina, localizar o Campus Nova Gameleira,
consultar farmácias do OpenStreetMap e distinguir observação cartográfica de
conclusão analítica.

## Requisitos

- QGIS 3.44 LTR.
- Plugin QuickOSM 2.5.3 ou versão compatível.
- Acesso à internet.
- Arquivo
  `../dados/02_processados/cefet_campus_nova_gameleira.geojson`.

## Produto esperado

Três produtos intermediários:

- projeto `outputs/encontro_01.qgz`, salvo com caminhos relativos;
- camadas consultadas em `outputs/farmacias_entorno_cefet.gpkg`;
- mapa `outputs/mapa_entorno_cefet.png`, contendo campus, farmácias, título,
  legenda, escala e atribuição ao OpenStreetMap.

Na atividade em sala, o grupo incorpora o mapa e as respostas analíticas em um
único PDF ou página no ambiente da disciplina, conforme
`../atividades_em_sala/atividade_01_mapeando_entorno_cefet.md`.

## Parte 1 — Preparar o projeto

1. Abra o QGIS e crie um projeto em branco.
2. Em **Projeto → Propriedades → Geral**, marque a opção para salvar caminhos
   relativos.
3. Salve o projeto como `outputs/encontro_01.qgz`.
4. No painel **Navegador**, expanda **XYZ Tiles** e adicione
   **OpenStreetMap** ao mapa.
5. Adicione a camada
   `dados/02_processados/cefet_campus_nova_gameleira.geojson`.
6. Clique com o botão direito na camada e escolha **Aproximar à camada**.
7. Defina uma escala aproximada de `1:35.000`. O enquadramento servirá como
   recorte operacional do “entorno”.

## Parte 2 — Consultar estabelecimentos no QGIS

1. Abra **Vetor → QuickOSM → QuickOSM**.
2. Em **Quick query**, preencha:
   - **Key:** `amenity`
   - **Value:** `pharmacy`
   - **In:** `Canvas extent`
3. Execute a consulta.
4. Mantenha a camada pontual e, caso exista, a camada de polígonos. Registre
   quantas feições foram retornadas em cada camada.
5. Salve os resultados em um GeoPackage:
   `outputs/farmacias_entorno_cefet.gpkg`.
6. Renomeie as camadas de modo compreensível e aplique uma simbologia que
   diferencie campus e farmácias.

## Parte 3 — Ler o mapa criticamente

Use a ferramenta **Identificar Feições** e a tabela de atributos para responder:

1. Quantas farmácias foram retornadas no recorte?
2. Em quais direções, tomando o campus como referência, os pontos parecem se
   concentrar?
3. Há trechos do mapa sem registros? Isso prova ausência de farmácias?
4. Quais atributos estão completos e quais apresentam valores nulos?
5. Que outros dados seriam necessários para recomendar a abertura de uma nova
   unidade?

## Parte 4 — Compor a evidência

1. Abra **Projeto → Novo Layout de Impressão**.
2. Insira mapa, título, legenda, escala e a nota
   `© OpenStreetMap contributors — consulta em 29/07/2026`.
3. Exporte como `outputs/mapa_entorno_cefet.png`.
4. Salve novamente o projeto.

## Contingência

Se a API Overpass estiver indisponível, a turma deve:

1. manter o mapa-base e a camada do campus;
2. observar estabelecimentos visíveis no mapa-base sem tratá-los como uma base
   completa;
3. registrar a indisponibilidade como limitação;
4. retomar a consulta QuickOSM quando o serviço voltar.

Não substitua a falha por números presumidos.

## Critérios de conclusão

- Projeto QGIS salvo e reaberto sem caminhos quebrados.
- Campus e farmácias distinguíveis.
- Fonte OSM atribuída.
- Respostas separam achado, hipótese e limitação.
