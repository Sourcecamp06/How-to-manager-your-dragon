# How to Manager Your Dragon – Informe Extendido

## Introducción

Érase una vez en la Isla de Berk un programador (sí, un programador en esa era) que recibió una misión muy importante: construir un sistema capaz de organizar, administrar y supervisar los diferentes eventos realizados por los habitantes de la isla. Aunque los vikingos eran expertos en combate, exploración y domesticación de dragones, llevar el control manual de cada actividad representaba un desafío cada vez más grande. Por esta razón surge **How to Manager Your Dragon**, una aplicación diseñada para facilitar la planificación de eventos y la gestión eficiente de los recursos disponibles en Berk.

El objetivo principal del proyecto consiste en garantizar que cada evento pueda programarse respetando todas las reglas establecidas por la comunidad, evitando conflictos de horarios, reutilización indebida de recursos y violaciones a las restricciones definidas para cada actividad. El sistema automatiza la validación de reglas, controla la disponibilidad de participantes y ofrece una interfaz amigable para que los organizadores puedan crear y consultar eventos de manera sencilla.

Además de representar una solución práctica para el problema planteado, el proyecto permite aplicar conceptos fundamentales de programación como la modularización, la validación de datos, la persistencia de información, la organización de recursos y la construcción de interfaces gráficas mediante Streamlit.

---

# Objetivos del Proyecto

## Objetivo General

Desarrollar una aplicación capaz de administrar eventos de la Isla de Berk, garantizando el cumplimiento automático de las reglas establecidas y gestionando adecuadamente todos los recursos involucrados.

## Objetivos Específicos

- Permitir la creación de distintos tipos de eventos.
- Administrar la disponibilidad de guerreros, dragones y equipamiento.
- Evitar conflictos de programación entre arenas.
- Validar automáticamente todas las reglas del negocio.
- Facilitar la visualización de los eventos creados.
- Mantener un registro persistente de la información.
- Proporcionar una experiencia de usuario intuitiva mediante Streamlit.

---

# Contexto de la Isla de Berk

La isla de Berk es una comunidad donde conviven vikingos y dragones. A lo largo del año se realizan numerosas actividades recreativas, deportivas y de entrenamiento. Estas actividades requieren una correcta coordinación de recursos debido a que algunos guerreros poseen dragones exclusivos, existen limitaciones físicas de equipamiento y ciertas actividades solamente pueden desarrollarse en ubicaciones específicas.

Sin un sistema de organización adecuado podrían ocurrir problemas como:

- Programar dos eventos en una misma arena.
- Utilizar el mismo dragón en varias actividades simultáneamente.
- Asignar guerreros incompatibles dentro de un mismo evento.
- Sobrepasar la cantidad de armas o armaduras disponibles.
- Realizar eventos en ubicaciones incorrectas.

Por ello se implementa un sistema que actúa como administrador centralizado de todas las actividades de Berk.

---

# Tipos de Eventos Disponibles

El sistema contempla los siguientes eventos:

## 1. Peleas entre Vikingos

Competencia tradicional donde participan exclusivamente guerreros. En este tipo de evento no se permite la utilización de dragones.

Características:

- Participan únicamente vikingos.
- Requieren armas y armaduras.
- Deben respetar todas las restricciones de convivencia.

## 2. Peleas entre Vikingos Montados en Dragones

Modalidad avanzada donde cada guerrero combate mientras monta un dragón.

Características:

- Debe existir la misma cantidad de dragones y guerreros.
- Los dragones con dueño solamente pueden ser utilizados por su propietario.
- Los Cremallerus Espantosus requieren dos jinetes.

## 3. Peleas de Vikingos contra Dragones

Evento de entrenamiento donde un grupo de guerreros enfrenta dragones.

Características:

- Debe existir al menos un dragón.
- Requiere equipamiento de combate.
- Debe respetar la disponibilidad diaria.

## 4. Excursiones para Domesticar Dragones

Actividad orientada a la captura y domesticación de nuevas especies.

Características:

- Solamente puede realizarse en la Guarida de Dragones.
- Permite la interacción con dragones salvajes.
- Requiere supervisión y recursos especiales.

## 5. Competencia de Encestar la Oveja

Actividad recreativa inspirada en las tradiciones de vuelo de Berk.

Características:

- Solo puede realizarse en la Playa.
- Utiliza exclusivamente las ovejas disponibles.
- Necesita dragones y jinetes.

## 6. Entrenamiento de Vuelo

Sesiones destinadas a mejorar las habilidades de vuelo de los participantes.

Características:

- Obliga a utilizar dragones.
- Debe existir correspondencia entre jinetes y monturas.
- Respeta todas las restricciones de propiedad.

---

# Arenas Disponibles

Las actividades se desarrollan en distintas ubicaciones de Berk.

## Arena Legendaria de Berk

Principal centro de combate y espectáculos.

## Cúspide de los Guerreros Caídos

Ubicación ceremonial destinada a competencias especiales.

## Arena del Jefe Vikingo

Escenario utilizado para eventos oficiales.

## Playa

Área exclusiva para la Competencia de Encestar la Oveja y otras actividades permitidas.

## Guarida de Dragones

Lugar reservado para las excursiones de domesticación.

Importante: ninguna arena puede albergar más de un evento simultáneamente.

---

# Guerreros Disponibles

## Personajes Principales

- Hippo
- Astrid
- Patán
- Patapez
- Brutacio
- Brutilda
- Estoico
- Bocón
- Valkia

## Habitantes Genéricos

- Guerreros de Berk: 5
- Guerreras de Berk: 5
- Ancianos de Berk: 5

Cada participante posee disponibilidad diaria limitada, por lo que únicamente puede formar parte de un evento por día.

---

# Dragones Disponibles

## Dragones con Propietario

- Chimuelo
- Tormenta
- Colmillo
- Albóndiga
- Eructo y Guácara
- Rompecráneos
- Gruñón
- Brincanubes

## Dragones Generales

- Terror Terrible: 5
- Nadder Mortal: 3
- Gronckle: 2
- Cremallerus Espantosus: 3
- Monstrous Nightmare: 3
- Light Fury: 1
- Thunderdrum: 1

Los dragones representan uno de los recursos más importantes del sistema, ya que varias reglas giran alrededor de su disponibilidad y propiedad.

---

# Armamento Disponible

## Armas

- Escudos: 8
- Mazos: 8
- Espadas: 8
- Ballestas: 3
- Catapulta: 1

## Armaduras

- Cascos Vikingos: 10
- Pecheras de Cuero: 10
- Pantalones de Cuero: 10
- Botas de Hierro: 10

El sistema debe garantizar que nunca se asignen más recursos de los realmente disponibles.

---

# Recursos Especiales

## Ovejas

Cantidad disponible: 20.

Distribución:

- 20% de probabilidad de oveja negra.
- 80% de probabilidad de oveja blanca.

Las ovejas solamente pueden utilizarse en la Competencia de Encestar la Oveja.

---

# Reglas del Sistema

Las siguientes reglas constituyen el núcleo funcional del proyecto y deben respetarse exactamente.

## Regla 1

No puede ocurrir más de un evento simultáneamente en una arena.

## Regla 2

Un guerrero de la franquicia y su dragón solo pueden participar en un evento al día.

## Regla 3

Para peleas montados en dragones, competencia de encestar la oveja y entrenamiento de vuelo, cada guerrero de la franquicia tiene asignado su dragón por defecto:

- Chimuelo → Hippo
- Tormenta → Astrid
- Albóndiga → Patapez
- Gruñón → Bocón
- Eructo y Guácara → Brutacio
- Eructo y Guácara → Brutilda
- Colmillo → Patán
- Rompecráneos → Estoico
- Brincanubes → Valkia

Además, ningún otro guerrero puede utilizar un dragón que ya posee propietario.

## Regla 4

Los eventos de Peleas entre Vikingos Montados en Dragones, Competencia de Encestar la Oveja y Entrenamiento de Vuelo deben tener la misma cantidad de dragones que de vikingos.

Si se utiliza un Cremallerus Espantosus, este debe ser montado por dos jinetes.

## Regla 5

La Competencia de Encestar la Oveja solo puede realizarse en la Playa y las ovejas son exclusivas para este evento.

## Regla 6

Las Excursiones para Domar Dragones solo pueden realizarse en la Guarida de Dragones.

## Regla 7

Los eventos de Peleas entre Vikingos Montados en Dragones, Peleas de Vikingos contra Dragones, Competencia de Encestar la Oveja y Entrenamiento de Vuelo requieren obligatoriamente al menos un dragón.

## Regla 8

Las Peleas entre Vikingos no permiten la participación de dragones.

## Regla 9

Hippo no puede participar junto con Patán y Bocón no puede participar junto con Estoico en ningún evento.

---

# Arquitectura General

El proyecto se encuentra dividido en módulos especializados para favorecer la mantenibilidad y escalabilidad.

## Principios Aplicados

- Separación de responsabilidades.
- Modularización.
- Reutilización de código.
- Organización por capas.
- Validación centralizada.

---

# Estructura del Proyecto

```text
How-to-manager-your-dragon/
│
├── .gitignore
├── Informe.pdf
├── main.py
├── report.md
├── requirements.txt
│
├── assets/
│    ├── armors/ 
│    ├── dragons/
│    ├── sheeps/
│    ├── warriors/
│    ├── weapons/
│    ├── icon.png
│    └── main.png
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
```
(Este proyecto posee dos archivos explicativos, el report.md y el Informe.pdf, ambos cumplen funciones cruciales en dicho proyecto. La función del report.md es dar una vista detallada de cada punto del proyecto sin dejar un ningún detalle al margen de la ilegibilidad. La función del Informe.pdf es un resumen de este report.md para que la persona encargada de revisar este proyecto no se le dificulte a la hora de la interpretación, pero ambos en resumen cumplen la misma función de informe - reporte)


---

# Descripción de los Componentes

## main.py

Actúa como punto de entrada de la aplicación.

Responsabilidades:

- Inicializar Streamlit.
- Configurar la interfaz principal.
- Coordinar los distintos módulos.

## data/eventos.json

Archivo destinado a almacenar la información de los eventos creados.

Ventajas:

- Persistencia simple.
- Fácil lectura.
- Fácil mantenimiento.

## models/creador_de_eventos.py

Encargado de construir las estructuras que representan cada evento.

Funciones principales:

- Creación de eventos.
- Organización de datos.
- Integración con validaciones.

## models/gestor_de_recursos.py

Administra todos los recursos disponibles.

Funciones:

- Control de inventario.
- Verificación de disponibilidad.
- Actualización de recursos utilizados.

## models/validador_de_reglas.py

Implementa las reglas de negocio.

Responsabilidades:

- Validar restricciones.
- Evitar inconsistencias.
- Generar mensajes de error.

## UI/page/form.py

Contiene el formulario para registrar eventos.

## UI/page/events.py

Presenta los eventos almacenados al usuario.

---

# Flujo de Funcionamiento

1. El usuario abre la aplicación.
2. Selecciona el tipo de evento.
3. Escoge arena, participantes y recursos.
4. El sistema verifica disponibilidad.
5. El validador revisa todas las reglas.
6. Si todo es correcto, el evento se registra.
7. El evento queda almacenado en eventos.json.
8. Los recursos utilizados quedan marcados como ocupados.

---

# Gestión de Recursos

La administración de recursos es fundamental para garantizar la coherencia del sistema.

El gestor verifica constantemente:

- Guerreros disponibles.
- Dragones disponibles.
- Armas restantes.
- Armaduras restantes.
- Ovejas disponibles.
- Disponibilidad de arenas.

Gracias a este mecanismo se evita la sobreasignación de recursos y se garantiza la consistencia de la información.

---

# Interfaz de Usuario

La aplicación utiliza Streamlit para proporcionar una experiencia visual sencilla y moderna.

Características:

- Formularios interactivos.
- Selección dinámica de recursos.
- Mensajes de validación.
- Visualización de eventos.
- Navegación intuitiva.

El uso de Streamlit permite crear una solución web funcional sin necesidad de desarrollar interfaces complejas mediante HTML, CSS o JavaScript.

---

# Ventajas de la Solución

- Automatización de reglas complejas.
- Reducción de errores humanos.
- Gestión centralizada.
- Facilidad de uso.
- Arquitectura modular.
- Fácil mantenimiento.
- Escalabilidad futura.

---

# Posibles Mejoras Futuras

Aunque el proyecto cumple con todos los requerimientos establecidos, podría ampliarse mediante:

- Base de datos relacional.
- Sistema de autenticación.
- Historial de eventos.
- Reportes estadísticos.
- Exportación a PDF.
- Calendario visual.
- Gestión avanzada de temporadas.
- Sistema de puntuaciones.

---

# Conclusiones

How to Manager Your Dragon constituye una solución integral para la administración de eventos dentro de la Isla de Berk. El sistema permite organizar actividades complejas respetando todas las reglas establecidas, controlar la disponibilidad de recursos y ofrecer una experiencia de usuario clara mediante una interfaz desarrollada con Streamlit.

La división modular del proyecto facilita la comprensión del código y demuestra la aplicación práctica de conceptos fundamentales de desarrollo de software como la separación de responsabilidades, la validación de reglas de negocio y la gestión eficiente de recursos. Asimismo, la implementación de controles automáticos garantiza que cada evento registrado sea coherente con las restricciones definidas para la isla.

En conjunto, el proyecto representa una aplicación funcional, organizada y escalable que resuelve exitosamente el problema planteado, proporcionando una herramienta útil para coordinar la intensa vida de los vikingos y dragones de Berk.

## Instalación

### Prerrequisitos
- Python 3.8+
- Git

### Instalación
```bash
git clone https://github.com/Sourcecamp06/How-to-manager-your-dragon.git
cd how-to-manager-your-dragon
pip install -r requirements.txt
streamlit run main.py