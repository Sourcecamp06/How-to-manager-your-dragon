# How to manager your dragon

Érase una vez en la Isla de Berk un programador(sí, un programador en esa era) el cuál tenía una tarea: realizar un organizador de peleas vikingas y distintos tipos de eventos que se celebran en esta isla. Dicho organizador debía gestionar una serie de recursos para cada evento y seguir ciertas reglas de la isla.

## 📯 Tipos de eventos

- Peleas entre vikingos
- Peleas entre vikingos montados en dragones
- Peleas de vikingos contra dragones
- Excursiones para domesticar dragones
- Competencia de encestar la oveja
- Entrenamiento de vuelo

## 🏟 Arenas

- "Arena legendaria de Berk" 
- "Cúspide de los guerreros caídos" 
- "Arena del jefe vikingo"
- "Playa"
- "Guarida de dragones"

## 🤺 Guerreros

- Hippo
- Astrid
- Patán
- Patapez
- Brutacio
- Brutilda
- Estoico
- Bocón
- Valka

- Guerreros de Berk:5
- Guerreras de Berk:5
- Ancianos de Berk:5

## 🐉 Dragones 

- Chimuelo:1
- Tormenta:1
- Colmillo:1
- Albondiga:1
- Eructo y Guácara:1
- Rompecráneos:1
- Gruñón:1
- Brincanubes:1

- Terror Terrible: 5
- Nadder Mortal: 3
- Gronckle: 2
- Cremallerus Espantosus: 3
- Monstrous Nightmare: 3
- Light Fury: 1
- Thunderdrum: 1

## ⚔️ Armas

- Escudos: 8
- Mazos: 8
- Espadas: 8
- Ballestas: 3
- Catapulta: 1

## 🛡 Armaduras

- Cascos vikingos: 10
- Pecheras de cuero: 10
- Pantalones de cuero: 10
- Botas de hierro: 10

## 🐏 Extras

- Ovejas: 20

## 📋 Reglas a seguir
1. No puede ocurrir más de un evento simultáneamente en una arena
2. Un guerrero de la franquicia y su dragón solo pueden participar en un evento al día
3. Para peleas montados en dragones, competencia de encestar la oveja y entrenamiento de vuelo, cada guerrero de la franquicia tiene asignado su dragón por defecto[(Chimuelo - Hippo), (Tormenta - Astrid), (Albondiga - Patapez), (Gruñón - Bocón), (Eructo y Guácara - Brutacio), (Eructo y Guácara - Brutilda)(Los hermanos deben ir juntos a la batalla), (Colmillo - Patán), (Rompecráneos - Estoico(papá de Hippo)), (Brincanubes - Valka(mamá de Hippo))], además cada dragón con propietario no puede ser utilizado por otro guerrero
4. Los eventos: Pelea entre vikingos montados en dragones, Competencia de encestar la oveja, Entrenamiento de vuelo tienen que tener la misma cantidad de dragones q de vikingos, y si vas a montar un Cremallerus Espantosus debe tener dos jinetes que lo monten
5. La competencia de encestar la oveja solo se puede realizar en la playa y las ovejas son exclusivamente para este evento
6. Las excursiones para domar dragones solo pueden realizarse en la guarida de dragones
7. Para los eventos de Peleas entre vikingos montados en dragones, Peleas de vikingos contra
dragones, Competencia de encestar la oveja y Entrenamiento de vuelo es obligatorio escoger al menos un dragón
8. Para la competencia Pelea entre vikingos no se puede escoger dragones
9. Hippo no se lleva muy bien con Patán y Bocón no se lleva muy bien con Estoico, así q no pueden estar juntos en ningun tipo de evento

## 🚀 Características del Programa

### Gestión de Eventos
- Creación de eventos con múltiples tipos
- Validación automática de reglas de Berk
- Asignación inteligente de recursos

### Sistema de Recursos
- Inventario en tiempo real de dragones, guerreros y equipo
- Control de disponibilidad diaria
- Prevención de sobreasignación

### Interfaz de Usuario
- Dashboard interactivo con Streamlit
- Formularios intuitivos con validación
- Visualización de eventos programados

## 🏗️ Estructura del Proyecto

How-to-manager-your-dragon/
│
├── main.py
├── README.md
├── requirements.txt
│
├── assets/
│   ├── icon.png
│   └── main.png
│
├── data/
│   ├── eventos.json
│   └── __init__.py
│
├── models/
│   ├── creador_de_eventos.py
│   ├── gestor_de_recursos.py
│   ├── validador_de_reglas.py
│   └── __init__.py
│
└── UI/
    ├── __init__.py
    └── page/
        ├── events.py
        ├── form.py
        └── __init__.py

## 🛠️ Instalación

### Prerrequisitos
- Python 3.8+
- Git

### Instalación
```bash
git clone https://github.com/Sourcecamp06/How-to-manager-your-dragon.git
cd how-to-manager-your-dragon
pip install -r requirements.txt
