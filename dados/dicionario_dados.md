# Dicionário de dados — Unidade 1

Camada: `02_processados/cefet_campus_nova_gameleira.geojson`.

| Coluna | Significado | Base de origem | Tipo | Unidade | Cálculo | Observações |
|---|---|---|---|---|---|---|
| `nome` | Nome do local | Nominatim/OSM | Texto | — | Campo original `name` | Identificação institucional |
| `endereco` | Logradouro e número | Nominatim/OSM e CEFET-MG | Texto | — | Padronização didática | Conferido no portal institucional |
| `bairro` | Bairro do campus | Nominatim/OSM | Texto | — | Extraído de `display_name` | Nova Gameleira |
| `municipio` | Município | Nominatim/OSM | Texto | — | Extraído de `display_name` | Belo Horizonte |
| `lat` | Latitude geográfica | Nominatim/OSM | Decimal | grau | Conversão de texto para número | WGS 84 |
| `lon` | Longitude geográfica | Nominatim/OSM | Decimal | grau | Conversão de texto para número | WGS 84 |
| `osm_type` | Tipo do objeto OSM | Nominatim/OSM | Texto | — | Campo original | Resultado original é `way` |
| `osm_id` | Identificador no OSM | Nominatim/OSM | Inteiro | — | Campo original | Não é identificador interno da disciplina |
| `fonte` | Serviço de origem | Documentação da etapa | Texto | — | Valor atribuído | Exige atribuição ao OSM |
| `consulta_em` | Data da consulta | Documentação da etapa | Data ISO | — | Valor atribuído | 2026-07-29 |
| `geometry` | Ponto de referência do campus | Derivada | Geometria Point | grau | `Point(lon, lat)` | Não representa o perímetro |

