import json
#crear un archivo json
#crear diccionario
unisangil ={
    "unisangil": {
        "sedes": {
            "chiquinquira": {
               "Facultades": {
                    "Ingenierias y ciencias naturales": {
                        "Ingenieria de sistemas": {
                            "primer semestre": ["Calculo diferencial", "Fundamentos de programacion", "Algebra", "diseno prototipado", "Mecanica", "Expresion 1"],
                            "segundo semestre":                          
                        
                            { 
                               "Calculo integral": [],
                               "Matematicas discretas": [],
                               "Electromagnetismo": [],
                               "Proyecto integrador 1": [],
                               "expresion 2": [],

                                 
                

                                 "Programacion 1": 
                                 
                                 
                                 {
                                   "Docente": ["Jesus David Caro"],
                                    
                                    "Estudiantes": ["David Fernando Cano", "Haider Asdrubal Parra", "Santiago Monroy"]
                                 }
                                
                            },
                            

                            "tercer semestre": ["Hadware y sistemas operativos", "Estructura de datos", "Calculo en varias variables","modelado y analisis numerico", "sistemas bioticos", "proyecto integrador 2", "ciudadania"],
                            "cuarto semestre": ["Pensamiento sistemico", "redes", "analisis de algoritmos", "bases de datos", "Programacion 2", "Ecuaciones diferenciales", "proyecto integrador 3"],
                            "quinto semestre": ["Modelado de sistemas de informacion", "adiministracion y gestion de bases de datos", "Desarrollo web", "Electiva diciplinaria 1", "probabilidad y estadistica", "proyecto integrador 4", "electiva complementaria"],
                            "sexto semestre": ["Ingeniería de sofware","Seguridad informatica","electiva diciplinaria2","Inteligencia artificial","Etica y comportamiento profesional"],
                            "septimo semestre": ["Arquitectura de sofware", "ciencia de datos", "Administración de servidores}","investigacion de operaciones","gestion de proyectos1"],
                            "octavo semestre": ["modalidad de grado", "electiva diciplinaria3", "electiva de Ingenieria"]
                      
                
                    }
                    
                    },
                    "Ciencias economicas y administrativas": ["Contaduria publica", "Administracion de empresas", "tecnologia en gestion de empresas de economia solidaria"],
                    "Ciencias politicas y juridicas": ["Derecho"]
                }

               },
                           
             "Yopal": {
                "Facultades": {
                    "Ingenierias y ciencias naturales": ["Ingenieria de sistemas",""],
                    "Ciencias economicas y administrativas": ["Contaduria publica", "Administracion de empresas", "tecnologia en gestion de empresas de economia solidaria"],
                    "Ciencias politicas y juridicas": ["Derecho"]
                },
             "San Gil": {
                    "Facultades": ["Ingenierias y ciencias naturales", "Ciencias economicas y administrativas", "Ciencias educación y salud", "Ciencias politicas y juridicas"]}

                


        }
    }
}}

#variable para guardar el archivo
archivo = open("QuizProgramación", "w")
#escribir el archivo
json.dump(unisangil, archivo)

#cerrar el archivo
archivo.close() 


#unisangil, sedes, facultades, carreras por facultad, semestres, materias por semestres, ubicar materia en semestre, nombre del docente, nombre compañeros