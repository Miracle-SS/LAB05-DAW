# Ajedrez en Python — DAW Lab 05

**Alumno:** Mario Miguel Choquecota Pandia  
**Curso:** Desarrollo de Aplicaciones Web  
**Universidad:** Universidad Nacional de San Agustín

---

## Descripción

Implementación de la clase `Picture` en Python para manipular imágenes representadas como arreglos de strings, aplicada al dibujo de un tablero de ajedrez con distintas configuraciones de piezas.

---

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/[tu-usuario]/ajedrez-python.git
cd ajedrez-python
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar un ejercicio

```bash
python ejercicios/ejercicio_g.py
python ejercicios/ejercicio_h.py
python ejercicios/ejercicio_i.py
```

---

## Métodos implementados en `Picture`

| Método | Descripción |
|--------|-------------|
| `verticalMirror()` | Devuelve el espejo vertical de la imagen |
| `horizontalMirror()` | Devuelve el espejo horizontal de la imagen |
| `negative()` | Devuelve el negativo de la imagen |
| `join(p)` | Une la imagen actual con `p` a su derecha |
| `up(p)` | Coloca `p` encima de la imagen actual |
| `under(p)` | Coloca `p` debajo de la imagen actual |
| `horizontalRepeat(n)` | Repite la imagen `n` veces en horizontal |
| `verticalRepeat(n)` | Repite la imagen `n` veces en vertical |
| `rotate()` | Rota la imagen 90° en sentido horario |
| `overlay(p)` | Superpone la imagen sobre `p` píxel a píxel |

---

## Ejercicios

| Ejercicio | Descripción |
|-----------|-------------|
| a | 4 caballos mirando a la izquierda, intercalados blanco-negro |
| b | Igual que a, pero los 2 de abajo miran a la derecha |
| c | 4 damas en fila |
| d | 8 casillas en fila empezando por blanca |
| e | 8 casillas en fila empezando por negra |
| f | Cuadrícula de 4 filas × 8 columnas empezando con blanca |
| g | Tablero completo con todas las piezas en posición inicial |
| h | Apertura Italiana: 1.e4 e5 2.Cf3 Cc6 3.Ac4 |
| i | Apertura Escocesa: 1.e4 e5 2.Cf3 Cc6 3.d4 |

---

## Referencias

-	Escobedo, R. (s.f.). ajedrez [Repositorio de GitHub]. GitHub. https://github.com/rescobedoq/daw/tree/main/lab04/ajedrez
-	Python Software Foundation. (2026). Python Documentation. https://docs.python.org/3/
