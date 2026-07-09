# Atividade em Sala — Unidade 1
## "Mapeando o Entorno do CEFET"

**Unidade:** 1 – Fundamentos de Geomarketing  
**Encontro:** 1 | **Duração:** 50 min | **Grupos:** 3–4 estudantes

---

## Objetivo
Realizar a primeira extração de dados espaciais via OpenStreetMap e identificar padrões de distribuição de estabelecimentos comerciais.

---

## Roteiro

### Parte A — Extração de dados (20 min)

1. Acessar [overpass-turbo.eu](https://overpass-turbo.eu)
2. Executar a query:
```
[out:json][timeout:25];
area["name"="Belo Horizonte"]->.bh;
node["amenity"="pharmacy"](area.bh);
out body;
```
3. Clicar em **Run** e aguardar
4. Exportar: *Export → GeoJSON → Download*
5. Abrir no QGIS: *Camada → Adicionar Camada Vetorial → Selecionar arquivo GeoJSON*

### Parte B — Análise (20 min)

Responda com base no mapa gerado:
1. Qual região/bairro concentra mais farmácias?
2. Existe alguma área visivelmente sem cobertura?
3. Que fatores (renda, hospitais, fluxo de pessoas) poderiam explicar esse padrão?
4. Os dados do OSM parecem completos? Justifique.

### Parte C — Apresentação (10 min)

Cada grupo apresenta 1 achado principal (máximo 2 minutos).

---

## Entregável

- Print do mapa gerado no QGIS
- 3 observações escritas sobre os padrões encontrados

---

## Gabarito Esperado

**Padrão de distribuição:**
- Alta concentração: Centro, Savassi, Funcionários, Lourdes (alta renda + fluxo)
- Menor densidade: Venda Nova, Barreiro, Ribeirão das Neves
- Clusters em torno de hospitais: Hospital das Clínicas, Biocor, Santa Casa

**Limitações do OSM:**
- Cobertura estimada: ~65-75% das farmácias reais
- Periferia tende a ser subrepresentada
- Dados podem estar desatualizados

---

## Recursos necessários
- Computador com QGIS e acesso à internet
- Conta/acesso ao [overpass-turbo.eu](https://overpass-turbo.eu)
