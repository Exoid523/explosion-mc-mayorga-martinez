from pathlib import Path

import yaml

from dominio.modelos import ConfigExplosion


def cargar_config_yaml(ruta: str = "config.yaml") -> ConfigExplosion:
    base = ConfigExplosion()
    archivo = Path(ruta)

    if not archivo.exists():
        return base

    with open(archivo, "r", encoding="utf-8") as f:
        datos = yaml.safe_load(f) or {}

    simulacion = datos.get("simulacion", {})
    visualizacion = datos.get("visualizacion", {})
    distribucion = datos.get("distribucion", {})
    ejecucion = datos.get("ejecucion", {})

    angulo = distribucion.get("angulo", {})
    velocidad = distribucion.get("velocidad", {})

    return ConfigExplosion(
        n_proyectiles=simulacion.get("n_proyectiles", base.n_proyectiles),
        v_min=simulacion.get("v_min", base.v_min),
        v_max=simulacion.get("v_max", base.v_max),
        g=simulacion.get("g", base.g),
        dt=simulacion.get("dt", base.dt),
        semilla=simulacion.get("semilla", base.semilla),

        tipo=simulacion.get("tipo", base.tipo),
        metodo=simulacion.get("metodo", base.metodo),
        salida=simulacion.get("salida", base.salida),

        trail_length=visualizacion.get("trail", base.trail_length),

        modo_ejecucion=ejecucion.get("modo", base.modo_ejecucion),
        workers=ejecucion.get("workers", base.workers),

        dist_angulo=angulo.get("tipo", base.dist_angulo),
        angulo_media=angulo.get("media", base.angulo_media),
        angulo_sigma=angulo.get("sigma", base.angulo_sigma),
        angulo_kappa=angulo.get("kappa", base.angulo_kappa),

        dist_velocidad=velocidad.get("tipo", base.dist_velocidad),
        vel_media=velocidad.get("media", base.vel_media),
        vel_sigma=velocidad.get("sigma", base.vel_sigma),
    )