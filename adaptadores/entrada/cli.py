import argparse

from dominio.modelos import ConfigExplosion
from dominio.puertos import PuertoEntrada
from adaptadores.entrada.yaml_config import cargar_config_yaml


class EntradaCLI(PuertoEntrada):
    def __init__(self, ruta_config: str = "config.yaml"):
        self.ruta_config = ruta_config

    def obtener_config(self) -> ConfigExplosion:
        config = cargar_config_yaml(self.ruta_config)

        parser = argparse.ArgumentParser(
            description="Simulacion Monte Carlo de una explosion"
        )

        parser.add_argument("--n", type=int, default=config.n_proyectiles)
        parser.add_argument("--v-min", type=float, default=config.v_min)
        parser.add_argument("--v-max", type=float, default=config.v_max)
        parser.add_argument("--g", type=float, default=config.g)
        parser.add_argument("--dt", type=float, default=config.dt)
        parser.add_argument("--semilla", type=int, default=config.semilla)

        parser.add_argument(
            "--tipo",
            choices=["ligero", "pesado", "arrastre"],
            default=config.tipo,
        )

        parser.add_argument(
            "--metodo",
            choices=["euler", "verlet"],
            default=config.metodo,
        )

        parser.add_argument(
            "--salida",
            choices=["animacion", "csv", "ambos"],
            default=config.salida,
        )

        parser.add_argument(
            "--dist-angulo",
            choices=["uniforme", "normal", "vonmises"],
            default=config.dist_angulo,
        )

        parser.add_argument(
            "--dist-vel",
            choices=["uniforme", "normal", "exponencial"],
            default=config.dist_velocidad,
        )

        args = parser.parse_args()

        config.n_proyectiles = args.n
        config.v_min = args.v_min
        config.v_max = args.v_max
        config.g = args.g
        config.dt = args.dt
        config.semilla = args.semilla
        config.tipo = args.tipo
        config.metodo = args.metodo
        config.salida = args.salida
        config.dist_angulo = args.dist_angulo
        config.dist_velocidad = args.dist_vel

        return config