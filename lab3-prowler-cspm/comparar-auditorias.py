import csv
from pathlib import Path

carpeta = Path.home() / "lab3-prowler-cspm/evidencias"

informes = [
    ("Inicial", "prowler-output-000000000000-20261014163343.csv"),
    ("Política de contraseñas", "prowler-output-000000000000-20261014164028.csv"),
    ("Roles de auditoría y soporte", "prowler-output-000000000000-20261014164540.csv"),
]

print("\nCOMPARACIÓN DE AUDITORÍAS")
print(f"{'ETAPA':<32} {'FAIL':>6} {'PASS':>6} {'TOTAL':>7}")
print("-" * 53)

for etapa, nombre in informes:
    ruta = carpeta / nombre

    if not ruta.exists():
        print(f"\nERROR: No se encuentra el informe {ruta}")
        continue

    conteos = {"FAIL": 0, "PASS": 0}
    fallos = []

    with ruta.open(encoding="utf-8-sig", newline="") as archivo:
        for fila in csv.DictReader(archivo, delimiter=";"):
            estado = (fila.get("STATUS") or "").strip().upper()

            if estado in conteos:
                conteos[estado] += 1

            if estado == "FAIL":
                fallos.append((
                    fila.get("CHECK_ID", ""),
                    fila.get("SEVERITY", ""),
                    fila.get("CHECK_TITLE", ""),
                ))

    total = conteos["FAIL"] + conteos["PASS"]
    print(
        f"{etapa:<32} {conteos['FAIL']:>6} "
        f"{conteos['PASS']:>6} {total:>7}"
    )

    print(f"\nHallazgos fallidos — {etapa}:")
    for control, severidad, titulo in fallos:
        print(f"  [{severidad}] {control}: {titulo}")
    if not fallos:
        print("  Ninguno")

    print()

print("Comparación finalizada.")
