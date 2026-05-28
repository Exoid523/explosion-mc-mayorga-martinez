# Explosión Monte Carlo

Proyecto final de **Laboratorio de Simulación**.

**Integrantes:** Dulce Mayorga y Josué Martínez  
**Repositorio:** `explosion-mc-mayorga-martinez`

---

## Descripción

Este proyecto simula una explosión mediante el método Monte Carlo. Se generan muchos proyectiles desde un mismo punto, cada uno con ángulo y velocidad inicial aleatoria. Luego se calcula su trayectoria bajo la acción de la gravedad y, según el tipo de proyectil, también puede incluirse arrastre.

El proyecto permite:

- simular múltiples proyectiles;
- cambiar distribuciones de ángulo y velocidad;
- comparar los métodos numéricos Euler y Verlet;
- generar una animación;
- guardar resultados en CSV;
- validar el dominio con pruebas automáticas.

Además de la simulación física, el código fue organizado usando arquitectura hexagonal y patrones de diseño.

---

## Estructura del proyecto

```text
explosion-mc-mayorga-martinez/
│
├── main.py
├── config.yaml
├── requirements.txt
├── Makefile
├── README.md
│
├── dominio/
│   ├── modelos.py
│   ├── puertos.py
│   ├── explosion.py
│   └── patrones/
│       ├── fabrica.py
│       ├── estrategia.py
│       └── observador.py
│
├── adaptadores/
│   ├── entrada/
│   │   ├── cli.py
│   │   └── yaml_config.py
│   └── salida/
│       ├── animacion.py
│       └── csv_output.py
│
└── tests/
    └── test_dominio.py
```

---

## Instalación

Crear entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

---

## Ejecución

Simulación por defecto:

```bash
python main.py
```

Salida CSV:

```bash
python main.py --salida csv --n 300
```

Animación:

```bash
python main.py --salida animacion --n 300
```

CSV y animación:

```bash
python main.py --salida ambos --n 300
```

Usar Verlet:

```bash
python main.py --metodo verlet
```

Usar proyectiles con arrastre:

```bash
python main.py --tipo arrastre --salida csv --n 300
```

Simular gravedad lunar:

```bash
python main.py --g 1.62 --salida csv --n 300
```

---

## Opciones principales

| Opción | Descripción |
|---|---|
| `--n` | Número de proyectiles |
| `--v-min` | Velocidad mínima inicial |
| `--v-max` | Velocidad máxima inicial |
| `--g` | Gravedad |
| `--dt` | Paso temporal |
| `--semilla` | Semilla aleatoria |
| `--tipo` | `ligero`, `pesado`, `arrastre` |
| `--metodo` | `euler`, `verlet` |
| `--salida` | `animacion`, `csv`, `ambos` |
| `--dist-angulo` | `uniforme`, `normal`, `vonmises` |
| `--dist-vel` | `uniforme`, `normal`, `exponencial` |

Los valores por defecto están en `config.yaml`. Las opciones escritas en la terminal tienen prioridad sobre el YAML.

---

## Diseño del código

El proyecto sigue una organización tipo arquitectura hexagonal:

- `dominio/`: contiene la lógica central de la simulación.
- `adaptadores/entrada/`: maneja CLI y YAML.
- `adaptadores/salida/`: maneja CSV y animación.
- `main.py`: conecta todas las piezas.

El dominio no depende de librerías externas como `matplotlib`, `yaml` o `csv`.

---

## Patrones utilizados

### Factory Method

Implementado en:

```text
dominio/patrones/fabrica.py
```

Se usa para crear proyectiles ligeros, pesados o con arrastre sin modificar el motor de simulación.

### Strategy

Implementado en:

```text
dominio/patrones/estrategia.py
```

Permite cambiar entre Euler y Verlet sin modificar el motor.

### Observer

Implementado en:

```text
dominio/patrones/observador.py
adaptadores/salida/csv_output.py
```

Permite notificar eventos, como el aterrizaje de un proyectil, sin acoplar el motor a cada salida.

---

## Salida CSV

Al ejecutar:

```bash
python main.py --salida csv
```

se genera:

```text
resultados.csv
```

con una fila por proyectil y los campos:

```text
angulo_deg
v0
masa
alcance
altura_max
tiempo_vuelo
error_energia
```

Este archivo no se sube al repositorio porque es generado automáticamente.

---

## Animación

La animación muestra trayectorias, marcas de impacto, histograma de alcances, estadísticas, tiempo simulado y cantidad de proyectiles en vuelo o aterrizados.

Se usa `FuncAnimation` para la animación y `LineCollection` para dibujar muchas trayectorias de forma eficiente.

---

## Pruebas

Ejecutar pruebas:

```bash
python -m pytest tests/ -v
```

Las pruebas validan:

- creación correcta de proyectiles;
- alcance numérico frente al alcance analítico;
- mejor conservación de energía con Verlet;
- funcionamiento del patrón Observer;
- reproducibilidad con la misma semilla;
- funcionamiento general del motor.

---

## Makefile

El proyecto incluye comandos rápidos:

```bash
make help
make install
make test
make run
make csv
make animacion
make arrastre
make clean
```

---

## Nota;

El proyecto combina una simulación física con una estructura de software extensible. Se pueden cambiar proyectiles, métodos numéricos, distribuciones y salidas sin modificar el núcleo de la simulación.