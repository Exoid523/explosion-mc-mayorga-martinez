import csv 
from pathlib import Path

from dominio.puertos import PuertoObservador


class SalidaCSV(PuertoObservador):
    def __init__(self, ruta: str = "resultados.csv"):
        self.ruta = ruta = Path(ruta)
        self.ruta = Path(ruta)
        self.iniciado = False

        self.campos = [
            "angulo_deg",
            "v0",
            "masa",
            "alcance",
            "altura_max",
            "tiempo_vuelo",
            "error_energia",
        ]
    def al_iniciar(self, config) -> None:
        with open(self.ruta,"w", newline="", encoding="utf-8") as archivos:
            writer = csv.DictWriter(archivos, fieldnames=self.campos)
            writer.writeheader()

        self.iniciado = True
    def al_aterrizar(self, resultado) -> None:
        if not self.iniciado:
            return

        with open(self.ruta,"a", newline="", encoding="utf-8") as archivos:
            writer = csv.DictWriter(archivos, fieldnames=self.campos)
            writer.writerow({
                "angulo_deg": resultado.angulo_deg,
                "v0": resultado.v0,
                "masa": resultado.masa,
                "alcance": resultado.alcance,
                "altura_max": resultado.altura_max,
                "tiempo_vuelo": resultado.tiempo_vuelo,
                "error_energia": resultado.error_energia,
            })