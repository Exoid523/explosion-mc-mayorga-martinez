PYTHON ?= python
N ?= 300
G ?= 9.8

.PHONY: help install test run csv animacion ambos verlet arrastre lunar clean

help:
	@echo "Explosión Monte Carlo - comandos disponibles"
	@echo ""
	@echo "  make install     Instala dependencias"
	@echo "  make test        Ejecuta pruebas"
	@echo "  make run         Ejecuta simulación por defecto"
	@echo "  make csv         Genera resultados.csv"
	@echo "  make animacion   Ejecuta animación"
	@echo "  make ambos       Ejecuta animación y CSV"
	@echo "  make verlet      Ejecuta simulación con método Verlet"
	@echo "  make arrastre    Ejecuta proyectiles con arrastre"
	@echo "  make lunar       Ejecuta simulación con gravedad lunar"
	@echo "  make clean       Limpia archivos generados"
	@echo ""
	@echo "Variables opcionales:"
	@echo "  N=100            Cambia número de proyectiles"
	@echo "  G=1.62           Cambia gravedad"

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest tests/ -v

run:
	$(PYTHON) main.py --n $(N)

csv:
	$(PYTHON) main.py --salida csv --n $(N)

animacion:
	$(PYTHON) main.py --salida animacion --n $(N)

ambos:
	$(PYTHON) main.py --salida ambos --n $(N)

verlet:
	$(PYTHON) main.py --metodo verlet --salida csv --n $(N)

arrastre:
	$(PYTHON) main.py --tipo arrastre --salida csv --n $(N)

lunar:
	$(PYTHON) main.py --g 1.62 --salida csv --n $(N)

clean:
	$(PYTHON) -c "from pathlib import Path; [p.unlink() for patron in ('resultados.csv', '*.png') for p in Path('.').glob(patron) if p.exists()]"