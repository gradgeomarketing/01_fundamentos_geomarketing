#!/usr/bin/env python3
"""
Objetivo
--------
Converter a resposta original do Nominatim sobre o Campus Nova Gameleira em
uma camada GeoJSON pontual para uso no primeiro encontro da disciplina.

Entrada
-------
dados/01_originais/nominatim_cefet_campus_nova_gameleira.json

Saídas
------
dados/02_processados/cefet_campus_nova_gameleira.geojson
dados/03_auditoria/amostra_cefet_campus.csv
dados/03_auditoria/log_preparacao_cefet.json

Transformações e variáveis
--------------------------
- Converte lon/lat textuais em números decimais.
- Representa o centro retornado pelo Nominatim como geometria Point.
- Cria campos didáticos de nome, endereço, bairro, município, fonte e data.

Critérios e suposições
---------------------
- O primeiro resultado da consulta é o Campus Nova Gameleira.
- O ponto é uma referência de localização, não o limite do campus.
- O SRC do GeoJSON é WGS 84 (EPSG:4326), conforme a especificação GeoJSON.

Limitações
----------
- A geometria simplifica uma área institucional a um ponto central.
- A posição e os atributos dependem do estado do OpenStreetMap na consulta.
- O script não sobrescreve saídas existentes sem a opção --overwrite.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "dados/01_originais/nominatim_cefet_campus_nova_gameleira.json"
OUTPUT = ROOT / "dados/02_processados/cefet_campus_nova_gameleira.geojson"
AUDIT_SAMPLE = ROOT / "dados/03_auditoria/amostra_cefet_campus.csv"
AUDIT_LOG = ROOT / "dados/03_auditoria/log_preparacao_cefet.json"


def refuse_overwrite(paths: list[Path], overwrite: bool) -> None:
    existing = [str(path) for path in paths if path.exists()]
    if existing and not overwrite:
        joined = "\n- ".join(existing)
        raise SystemExit(
            "Saídas já existentes. Use --overwrite somente após conferência:\n- "
            + joined
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Substitui somente as saídas derivadas; nunca altera o dado original.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Confere as saídas existentes sem modificar nenhum arquivo.",
    )
    args = parser.parse_args()

    raw_bytes = INPUT.read_bytes()
    records = json.loads(raw_bytes)
    if not records:
        raise SystemExit("A resposta original do Nominatim não contém registros.")

    source = records[0]
    lon = float(source["lon"])
    lat = float(source["lat"])
    properties = {
        "nome": source["name"],
        "endereco": "Avenida Amazonas, 7675",
        "bairro": "Nova Gameleira",
        "municipio": "Belo Horizonte",
        "lat": lat,
        "lon": lon,
        "osm_type": source["osm_type"],
        "osm_id": int(source["osm_id"]),
        "fonte": "Nominatim / OpenStreetMap",
        "consulta_em": "2026-07-29",
    }
    feature_collection = {
        "type": "FeatureCollection",
        "name": "cefet_campus_nova_gameleira",
        "features": [
            {
                "type": "Feature",
                "properties": properties,
                "geometry": {"type": "Point", "coordinates": [lon, lat]},
            }
        ],
    }

    input_hash = hashlib.sha256(raw_bytes).hexdigest()

    if args.check:
        missing = [
            str(path)
            for path in (OUTPUT, AUDIT_SAMPLE, AUDIT_LOG)
            if not path.exists()
        ]
        if missing:
            raise SystemExit("Saídas ausentes:\n- " + "\n- ".join(missing))

        current_geojson = json.loads(OUTPUT.read_text(encoding="utf-8"))
        if current_geojson != feature_collection:
            raise SystemExit("A camada GeoJSON não corresponde à entrada original.")

        with AUDIT_SAMPLE.open(encoding="utf-8", newline="") as handle:
            sample_rows = list(csv.DictReader(handle))
        if len(sample_rows) != 1:
            raise SystemExit("A amostra de auditoria deve conter exatamente uma linha.")
        if (
            sample_rows[0]["osm_id"] != str(properties["osm_id"])
            or sample_rows[0]["lat"] != str(properties["lat"])
            or sample_rows[0]["lon"] != str(properties["lon"])
        ):
            raise SystemExit("A amostra de auditoria diverge da camada preparada.")

        current_audit = json.loads(AUDIT_LOG.read_text(encoding="utf-8"))
        if current_audit.get("sha256_entrada") != input_hash:
            raise SystemExit("O hash da entrada diverge do log de auditoria.")
        print("Verificação concluída: saídas coerentes com a entrada original.")
        return

    refuse_overwrite([OUTPUT, AUDIT_SAMPLE, AUDIT_LOG], args.overwrite)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_SAMPLE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(feature_collection, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    with AUDIT_SAMPLE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(properties))
        writer.writeheader()
        writer.writerow(properties)

    audit = {
        "etapa": "Preparação da referência espacial do Campus Nova Gameleira",
        "executado_em": date.today().isoformat(),
        "entrada": str(INPUT.relative_to(ROOT)),
        "sha256_entrada": input_hash,
        "registros_entrada": len(records),
        "saida": str(OUTPUT.relative_to(ROOT)),
        "feicoes_saida": 1,
        "geometria": "Point",
        "crs": "EPSG:4326",
        "formula": "Point(lon, lat) usando as coordenadas retornadas pelo Nominatim",
        "limitacao": "O ponto não representa o perímetro do campus.",
    }
    AUDIT_LOG.write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Criado: {OUTPUT}")
    print(f"Criado: {AUDIT_SAMPLE}")
    print(f"Criado: {AUDIT_LOG}")


if __name__ == "__main__":
    main()
