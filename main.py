from AsientoClass import Asiento
from SalaClass import Sala
from PeliculaClass import Pelicula
from FuncionClass import Funcion

#Objetos: asientoA1 A2, es un objeto 
asientoA1 = Asiento("A", 1) #Asiento es la clase donde construyo el objeto
asientoA2 = Asiento("A", 2)
asientoA3 = Asiento("A", 2)
asientoB1 = Asiento("B", 1)
asientoB2 = Asiento("B", 2)
asientoB3 = Asiento("B", 2)

lista_asientos = [asientoA1, asientoA2, asientoA3, asientoB1, asientoB2, asientoB3]

sala1 = Sala("Sala A1", "Regular", lista_asientos)
sala1 = Sala("Sala A2", "VIP", lista_asientos)
sala3 = Sala("Sala A3", "3D", lista_asientos)


pelicula1 = Pelicula("Inception", "Un ladrón habilidoso ingresa a los sueños de las personas para robar información valiosa.","Ciencia ficción, Acción, Suspense"," 2 horas 28 minutos")
pelicula2 = Pelicula("Jurassic Park","Un parque temático de dinosaurios se convierte en un caos cuando los dinosaurios escapan y comienzan a causar estragos.","Ciencia ficción, Acción, Aventura","2 horas 7 minutos")

funcion1 = Funcion(pelicula1, sala1, "12:00PM")
funcion2 = Funcion(pelicula2, sala2, "12:00PM")
funcion3 = Funcion(pelicula3, sala3, "12:00PM")
