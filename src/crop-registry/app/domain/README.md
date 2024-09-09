# Capa de dominio

La parte más central de esta arquitectura es el modelo de dominio, este modelo de dominio no puede depender de alguna
capa más sino de si misma, este modelo de dominio se puede llamar modelo de objetos, capa de dominio, entidad de dominio
pero son lo mismo.

Alrededor de la capa de dominio, existen los servicios de dominio, son las interfaces que exponen los repositorios para
conectarse a las bases de datos, se conoce también como capa de repositorio

¡**Aquí es donde vive la lógica central de la aplicación**!

## Entities

Representan el concepto fundamental del dominio de negocioy la lógica central de la aplicación. Modelan elementos del
dominio como objetos reales, contienen atributos y comportamientos esenciales para el negocio

## Repositorios

Es la abstracción que permite interactuar **infraestructura de almacenamiento de datos**, dejando de lado la dependencia
del almacenamiento. Son un intermediario entre las entidades del dominio y la capa de persistencia. Proporcionan métodos
para realizar el CRUD sin importar el como se almacenan.

## Servicios

Conocidos como servicios de dominio, contienen la lógica de negocio que no pertenece a una sola entidad o contienen
reglas complejas. 
