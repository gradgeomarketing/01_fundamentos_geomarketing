# Unidade 1 – Fundamentos de Geomarketing

**Disciplina:** Tópicos Especiais Mercadológicos: Geomarketing  
**Instituição:** CEFET-MG – Campus II, Belo Horizonte  
**Carga horária:** 4 horas/aula  
**Docente:** Prof.ª Renata Oliveira

## Conteúdo

Slides em Xaringan (R Markdown, usado apenas como formato de apresentação) + planos de aula. O conteúdo técnico ensinado ao aluno é 100% baseado em QGIS.

## Como usar

**Plugins QGIS necessários** (instalar via *Complementos → Gerenciar e Instalar Complementos*):

- **QuickOSM** — extração de dados do OpenStreetMap (POIs, vias, edifícios) direto no QGIS
- **MMQGIS** — geocodificação de endereços/CEP (*Geocode → Geocode CSV with Web Service*) e outras utilidades de análise
- **ORS Tools** — cálculo de isócronas e áreas de influência (rotas/tempo de deslocamento)

As demais ferramentas usadas no módulo (Join attributes by location/by nearest, Field Calculator, K-means clustering, Simbologia, Layout de Impressão) já vêm nativas no QGIS, não exigem instalação de complemento.

Para exportar mapas interativos, usar o plugin **qgis2web** (exporta a camada como HTML/Leaflet a partir do QGIS).

**Renderizar os slides** (o formato de apresentação continua sendo Xaringan/R Markdown):

```r
# Instalar pacotes necessários apenas para renderizar os slides (não para análise geoespacial)
install.packages(c("xaringan", "xaringanExtra", "countdown", "conflicted"))

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
├── index.Rmd          # Slides Xaringan
├── setup.Rmd           # Setup compartilhado (knitr, xaringanExtra) via child doc
├── xaringan-themer.css # Tema visual (fontes, cores, classes .tip/.your-turn/.question)
├── slides.css          # Ajustes visuais específicos do módulo (carregado por último, após o tema)
├── dados/             # Dados secundários baixados
├── img/               # Imagens e figuras
├── planos_aula/       # Planos de aula por encontro
└── README.md
```

## GitHub

Repositório: [github.com/retaoliveira/geomarketing_01_fundamentos_geomarketing](https://github.com/retaoliveira/geomarketing_01_fundamentos_geomarketing)
