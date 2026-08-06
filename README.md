# Unidade 1 – Fundamentos de Geomarketing

**Disciplina:** Tópicos Especiais Mercadológicos: Geomarketing  
**Instituição:** CEFET-MG – Campus II, Belo Horizonte  
**Carga horária:** 4 horas/aula  
**Docente:** Prof.ª Renata Oliveira

## Conteúdo

Esta unidade introduz o pensamento espacial aplicado a mercados e realiza a
primeira prática no QGIS. Os slides permanecem em Xaringan/R Markdown, conforme
o padrão já adotado nas oito unidades. A análise geoespacial ensinada ao
estudante é realizada no QGIS.

## Como usar

**Ambiente de referência:**

- **QGIS 3.44 LTR**;
- **QuickOSM 2.5.3** ou versão compatível — consulta a dados do OpenStreetMap
  por meio da API Overpass.

MMQGIS, ORS Tools e qgis2web pertencem a etapas posteriores. Eles não precisam
ser instalados no Encontro 1.

Antes da aula, execute:

```bash
python3 scripts/01_preparar_referencia_cefet.py
```

O script preserva a resposta original do Nominatim e cria a camada pontual do
Campus Nova Gameleira, além de amostra e log de auditoria. Para recriar saídas
já conferidas, use `--overwrite`.

**Renderizar os slides** (o formato de apresentação continua sendo Xaringan/R Markdown):

```r
# Instalar pacotes necessários apenas para renderizar os slides
install.packages(c("xaringan", "xaringanExtra"))

# Renderizar slides
rmarkdown::render("index.Rmd")
```

## Publicar no GitHub Pages

```bash
git add .
git commit -m "Adicionar slides Unidade 1"
git push -u origin main
```

Após o push, ativar GitHub Pages (branch `main`, pasta `/root`) em Settings > Pages.

## Estrutura

```
geomarketing_01_fundamentos_geomarketing/
├── slides/             # Fonte, HTML e recursos empacotados da apresentação
│   └── img/cartografia/ # Cópias locais das 20 figuras usadas pelos slides
├── planos_aula/        # Plano docente do Encontro 1
├── praticas_qgis/      # Roteiro operacional no QGIS
├── atividades_em_sala/ # Atividade discente e guia docente
├── avaliacao/          # Rubrica e checklist pré-aula
├── dados/
│   ├── 01_originais/   # Resposta preservada do Nominatim
│   ├── 02_processados/ # Camada de referência para o QGIS
│   └── 03_auditoria/   # Amostra e log de transformação
├── scripts/            # Processamento numerado e reproduzível
├── outputs/            # Projetos e mapas produzidos em aula
├── img/                # Imagens e figuras já existentes
└── README.md
```

## Sequência recomendada

1. Ler `planos_aula/encontro_01.md`.
2. Executar o script de preparação.
3. Conferir o dicionário e a auditoria.
4. Testar `praticas_qgis/01_primeiro_mapa_osm.md`.
5. Renderizar os slides.
6. Distribuir apenas a atividade discente e manter o guia docente restrito.

## Validação da apresentação

- Nenhum texto renderizado utiliza fonte menor que 30 px; esse também é o
  menor tamanho computado na versão atual.
- Não há conteúdo transbordando a área dos slides nem imagens quebradas.
- As figuras usam caminhos internos a `slides/` para funcionar tanto em
  arquivo local quanto no servidor de visualização do R/RStudio.
- As 20 figuras de conteúdo podem ser ampliadas por clique ou teclado e
  fechadas pelo botão × ou pela tecla `Esc`.
- A apresentação contém 39 slides de conteúdo, sem lâmina em branco após a
  abertura.
- Os slides operacionais reproduzem os arquivos, parâmetros, produtos e
  critérios definidos em `praticas_qgis/01_primeiro_mapa_osm.md` e apontam
  separadamente para o entregável da atividade discente.

## GitHub

Repositório registrado no `origin` local:
[github.com/gradgeomarketing/01_fundamentos_geomarketing](https://github.com/gradgeomarketing/01_fundamentos_geomarketing)
