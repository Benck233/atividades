#!/usr/bin/env python3
"""Smoke tests publicos do TP2.

Roda um caso simples por exercicio para o aluno validar rapidamente o formato
basico de entrada e saida antes do push.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


CASES = [
    {
        "id": "ex01",
        "file": "ex01_estatisticas_notas.py",
        "input": "5\n7.0 4.5 9.0 6.5 8.0\n",
        "expected": "Menor: 4.5\nMaior: 9.0\nMediana: 7.0\nAprovados: 4",
        "mode": "exact",
    },
    {
        "id": "ex02",
        "file": "ex02_compressao_rle.py",
        "input": "C\naaabbbccddddee\n",
        "expected": "3a3b2c4d2e",
        "mode": "exact",
    },
    {
        "id": "ex03",
        "file": "ex03_janela_maxima.py",
        "input": "8 3\n2 1 5 3 6 4 8 7\n",
        "expected": "5 5 6 6 8 8",
        "mode": "exact",
    },
    {
        "id": "ex04",
        "file": "ex04_frequencia_palavras.py",
        "input": "a b c a b a c\n2\n",
        "expected": "a: 3\nb: 2",
        "mode": "exact",
    },
    {
        "id": "ex05",
        "file": "ex05_placar_campeonato.py",
        "input": "3\nX 0 0 Y\nX 0 0 Z\nY 1 0 Z\n",
        "expected": "1. Y 4",
        "mode": "included",
    },
    {
        "id": "ex06",
        "file": "ex06_indice_invertido.py",
        "input": "3\npython dados\njava web\npython ia\npython\n",
        "expected": "Documentos: 1 3",
        "mode": "exact",
    },
    {
        "id": "ex07",
        "file": "ex07_anagramas.py",
        "input": "4\nate eta tae sol\n",
        "expected": "ate eta tae\nsol",
        "mode": "exact",
    },
    {
        "id": "ex08",
        "file": "ex08_cobertura_habilidades.py",
        "input": "Python SQL Docker Kubernetes\n2\nAna: Python\nBruno: SQL Java\n",
        "expected": "Habilidades faltando: Docker Kubernetes",
        "mode": "exact",
    },
    {
        "id": "ex09",
        "file": "ex09_pontos_proximos.py",
        "input": "3\n0 0\n1 0\n3 0\n",
        "expected": "1.00",
        "mode": "included",
    },
    {
        "id": "ex10",
        "file": "ex10_biblioteca.py",
        "input": "2\nDuna\nSapiens\n5\nEMPRESTAR Duna Alice\nSTATUS Duna\nEMPRESTAR Duna Bob\nDEVOLVER Duna\nSTATUS Duna\n",
        "expected": "Duna: Alice\nIndisponivel: Duna\nDuna: disponivel",
        "mode": "exact",
    },
    {
        "id": "ex11",
        "file": "ex11_caminho_bfs.py",
        "input": "4 4\nA B\nB C\nC D\nA D\nA D\n",
        "expected": "1",
        "mode": "exact",
    },
    {
        "id": "ex12",
        "file": "ex12_cache_lru.py",
        "input": "2\n6\nPUT 1 100\nPUT 2 200\nGET 1\nPUT 3 300\nGET 2\nGET 1\n",
        "expected": "100\nNenhum\n100",
        "mode": "exact",
    },
]


def run_case(case: dict[str, str]) -> tuple[bool, str]:
    target = ROOT / case["file"]
    proc = subprocess.run(
        [sys.executable, str(target)],
        input=case["input"],
        text=True,
        capture_output=True,
        cwd=ROOT,
        timeout=10,
    )

    out = proc.stdout.strip()
    err = proc.stderr.strip()

    if proc.returncode != 0:
        return False, f"erro de execucao (codigo {proc.returncode}): {err}"

    expected = case["expected"].strip()
    mode = case["mode"]

    if mode == "exact":
        ok = out == expected
    else:
        ok = expected in out

    if ok:
        return True, "ok"

    detail = f"saida esperada ({mode}): {expected!r} | saida recebida: {out!r}"
    return False, detail


def main() -> int:
    parser = argparse.ArgumentParser(description="Roda smoke tests publicos do TP2.")
    parser.add_argument(
        "--exercise",
        choices=[case["id"] for case in CASES],
        help="Roda apenas um exercicio (ex: ex04).",
    )
    args = parser.parse_args()

    selected = CASES
    if args.exercise:
        selected = [case for case in CASES if case["id"] == args.exercise]

    total = len(selected)
    passed = 0

    print("== Smoke tests TP2 ==")
    for case in selected:
        ok, detail = run_case(case)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {case['id']} - {case['file']}")
        if not ok:
            print(f"  -> {detail}")
        else:
            passed += 1

    print(f"\nResumo: {passed}/{total} testes passaram")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
