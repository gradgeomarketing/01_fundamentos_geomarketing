# Plano de Aula — Encontro 1
**Unidade:** 1 – Fundamentos de Geomarketing  
**Carga horária:** 4h/aula (200 min úteis)  
**Data prevista:** Semana 1 — Agosto 2026

---

## Objetivos do Encontro
1. Compreender o conceito e a evolução histórica do geomarketing.
2. Identificar a relação do geomarketing com marketing, geografia, estatística e SIG.
3. Reconhecer aplicações práticas em diferentes setores.
4. Compreender fundamentos de cartografia: geoide/elipsoide, datum, sistemas de coordenadas geográficas e projeções cartográficas.
5. Realizar primeira exploração de dados e ferramentas no QGIS.

---

## Programação Detalhada

| Horário | Duração | Atividade | Tipo |
|---------|---------|-----------|------|
| 0:00 | 10 min | Apresentação da disciplina: ementa, avaliação, ferramentas | Expositivo |
| 0:10 | 15 min | O que é geomarketing? Conceito e evolução histórica | Expositivo dialogado |
| 0:25 | 10 min | **Questão disparadora:** "Por que dois supermercados da mesma rede têm resultados tão diferentes?" | Discussão em plenário |
| 0:35 | 15 min | Relação geomarketing × marketing × geografia × estatística × SIG | Expositivo com slides |
| 0:50 | 10 min | **Pausa** | — |
| 1:00 | 15 min | Aplicações em varejo, setor público e organizações sociais | Expositivo + cases |
| 1:15 | 40 min | **Fundamentos de cartografia:** pensamento espacial, geoide/elipsoide, datum, coordenadas geográficas, projeções (tipos e classificação), UTM, SIG, vetor×raster, shapefile, distâncias e tipos de representação cartográfica | Expositivo com slides |
| 1:55 | 20 min | Introdução ao QGIS: instalação, interface e abertura de shapefile | Demonstração ao vivo |
| 2:15 | 10 min | **Pausa** | — |
| 2:25 | 50 min | **Atividade prática:** "Mapeando o entorno do CEFET" (grupos de 3–4) | Prática em sala |
| 3:15 | 15 min | Apresentação dos resultados por grupo | Socialização |
| 3:30 | 10 min | Resolução comentada + discussão de padrões encontrados | Plenário |
| 3:40 | 10 min | Conceitos-chave + orientações para próximo encontro | Síntese |
| 3:50 | 10 min | Dúvidas e encerramento | — |

---

## Fundamentos de Cartografia — Detalhamento (40 min)

**Roteiro expositivo (slides "Fundamentos de Cartografia e Representação Geográfica"), com figuras ilustrativas em `img/cartografia/`:**

1. **Pensamento espacial** (3 min) — 1ª Lei da Geografia de Tobler; encontrar significado em forma, tamanho, localização e trajetória de fenômenos.
2. **Geoide × Elipsoide de revolução** (5 min) — o geoide é a forma real (irregular) da Terra; o elipsoide é o modelo matemático usado como aproximação (parâmetros `a`, `b`, `f`), escolhido por país/região.
3. **Sistemas geodésicos e datum** (5 min) — o datum ancora o elipsoide à Terra real (vertical/altimétrico × horizontal/planimétrico); geocêntrico (**SIRGAS 2000**, EPSG:4674 — padrão do Brasil, usado em todo o curso) × topocêntrico (SAD-69).
4. **Coordenadas geográficas** (5 min) — meridianos e paralelos; latitude (distância angular ao Equador) e longitude (distância angular a Greenwich); diferença entre coordenadas geográficas (graus) e projetadas (metros).
5. **Projeções cartográficas** (8 min) — toda projeção deforma algo; não existe projeção ideal. Quatro famílias (conforme, equidistante, equivalente, afilática) e duas classificações (superfície de projeção; tipo de contato tangente/secante).
6. **Projeção UTM** (5 min) — 60 fusos de 6°; unidade em metros; fusos do Brasil (18–25); Belo Horizonte está no **Fuso 23**.
7. **O que é um SIG + por que cartografia digital** (4 min) — definições de Burrough, Cowen e Smith; vantagens práticas de mapear digitalmente.
8. **Vetor × Raster e estrutura do shapefile** (3 min) — formatos de dado espacial; extensões `.shp/.shx/.dbf/.prj` e por que shapefile é um conjunto de arquivos.
9. **Distâncias** (2 min) — euclidiana, Manhattan e em rede (prévia da Unidade 7).
10. **Tipos de representação cartográfica** (não contabilizado acima, ver Programação Detalhada) — coroplético, pontos, símbolos proporcionais, mapa de calor, fluxos, cartograma — com prévia de que serão praticados nas Unidades 4 e 6.

**Conexão com o restante do curso:** este bloco é a base conceitual que sustenta decisões práticas nas próximas unidades — verificação de SRC/datum e estrutura vetorial na Unidade 4, distâncias em rede na Unidade 7, e escolha do tipo de representação cartográfica na Unidade 6.

**Fonte:** OLIVEIRA, R. *Geocomputing e Análise Espacial*, [places.education/cursos/spatial/localizacao](https://www.places.education/cursos/spatial/localizacao/). Figuras reproduzidas do mesmo material, salvas em `img/cartografia/`.

---

## Atividade Prática — Detalhamento

**Nome:** "Mapeando o entorno do CEFET"  
**Duração:** 50 min  
**Grupos:** 3–4 estudantes

### Roteiro
1. Acessar [overpass-turbo.eu](https://overpass-turbo.eu)
2. Executar a seguinte query para extrair farmácias em BH:
```
[out:json][timeout:25];
area["name"="Belo Horizonte"]->.bh;
node["amenity"="pharmacy"](area.bh);
out body;
```
3. Exportar resultado como **GeoJSON**
4. Abrir no QGIS: Camada → Adicionar → Adicionar Camada Vetorial
5. Responder:
   - Qual bairro/região concentra mais farmácias?
   - Há áreas sem cobertura visível?
   - O que pode explicar a distribuição observada?

### Entregável
Print do mapa + 3 bullet points com observações.

---

## Resolução da Atividade

**Padrão esperado:**
- Alta concentração no Centro, Savassi, Funcionários (renda + fluxo)
- Menor densidade em Venda Nova, Barreiro, Ribeirão das Neves
- Clusters próximos a hospitais e UPAs

**Pontos para discussão:**
- Dados do OSM são completos para BH? (estimativa: ~70-80% de cobertura)
- Diferença entre ausência real de farmácias vs. ausência de dado
- Como renda e infraestrutura explicam o padrão?

---

## Recursos Necessários

- [ ] Projetor e tela
- [ ] Computadores com QGIS instalado (ou levar pendrive com instalador)
- [ ] Acesso à internet para Overpass API
- [ ] Slides do encontro (`index.Rmd` renderizado como HTML)

---

## Avaliação e Acompanhamento

**Participação esperada:** discussão ativa na questão disparadora e na socialização da prática.  
**Indicador de compreensão:** estudante consegue nomear pelo menos 3 aplicações setoriais do geomarketing.

---

## Para o Próximo Encontro (Encontro 2)

- Instalar QGIS 3.x LTR ([qgis.org](https://qgis.org))
- Instalar os plugins QGIS do módulo via *Complementos → Gerenciar e Instalar Complementos*: **QuickOSM**, **MMQGIS**, **ORS Tools**
- Leitura: OLIVEIRA, P.H.P. Cap. 1–2.
