# Problema Cine

El siguiente codigo cumple con el flujo de como seria la reserva de asientos del cine con un sencillo menu por consola.
El menu tiene las siguientes secciones:
- 1. Mostrar los asientos (Disponibles o No Disponibles)
- 2. Reservar Asiento
  - Se muestra los asientos disponibles
  - Se van seleccionando los asientos que desea reservar
  - Se solicita el Rut a la persona que reserva
    - En caso de que exista el Rut solo agrega los asientos al usuario correspondiente
    - De no existir el Rut se solicitan Nombre y Numero de Telefono para agregar este nuevo usuario con los asientos seleccionado
- 3. Anular Reserva
    - Se solicita Rut de la persona que reservo
        - En caso de que no se haya reservado con el Rut se devuelve al menu principal
        - Si es que el Rut tiene reservas se muestran los asientos que tiene reservados
            - Se solicita ingresar el asiento que desea anular
- 0. Salir de la aplicacion

### Como ejecutar
El ejercicio se realizo en python por lo que se debe tener instalado python en el equipo.
Si no lo tiene instalado descargue el controlador en el siguiente enlace y instale [Descarga Python](https://www.python.org/downloads/)
Una vez instalado python y descargado el repositorio se puede ejecutar haciendo click en el archivo **cineGraiph.py** o ingresando por consola CMD a la carpeta donde esta el archivo y ejecutar lo siguiente.
`python cineGraiph.py`