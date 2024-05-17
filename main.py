from AsientoClass import Asiento
from SalaClass import Sala
from PeliculaClass import Pelicula
from FuncionClass import Funcion
from CineClass import Cine


asientoA1 = Asiento("A", 1)
asientoA2 = Asiento("A", 2)
asientoA3 = Asiento("A", 3)
asientoB1 = Asiento("B", 1)
asientoB2 = Asiento("B", 2)
asientoB3 = Asiento("B", 3)


lista_asientos = [asientoA1, asientoA2, asientoA3, asientoB1, asientoB2, asientoB3]


sala1 = Sala("Sala A1", "Regular", lista_asientos)
sala2 = Sala("Sala A2", "VIP", lista_asientos)
sala3 = Sala("Sala A3", "3D", lista_asientos)


#Creando peliculas  def __init__(self,nombre, descripcion, genero, duracion):

pelicula1 = Pelicula("Inception", "Un ladrón habilidoso ingresa a los sueños de las personas para robar información valiosa.","Ciencia ficción, Acción, Suspense"," 2 horas 28 minutos")
pelicula2 = Pelicula("Jurassic Park","Un parque temático de dinosaurios se convierte en un caos cuando los dinosaurios escapan y comienzan a causar estragos.","Ciencia ficción, Acción, Aventura","2 horas 7 minutos")

funcion1 = Funcion(pelicula1, sala1, "12:00PM")
funcion2 = Funcion(pelicula2, sala2, "12:00PM")
funcion3 = Funcion(pelicula1, sala3, "12:00PM")
funcion4 = Funcion(pelicula2, sala3, "02:00PM")

lista_funciones = [funcion1, funcion2, funcion3, funcion4]


cine = Cine("Cinépolis Diana", "Paseo Reforma", lista_funciones)


cine.obtenerLugares(0)

cine.funciones[0].ocuparAsiento(0)
cine.obtenerLugares(0)

cine.funciones[0].ocuparAsiento(0)
cine.funciones[0].ocuparAsiento(2)
cine.funciones[0].ocuparAsiento(4)

cine.obtenerLugares(0)
