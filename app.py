## tarea de python con sqlite3 de DANIEL QUISPE GUTIERREZ
import sqlite3
conn =  sqlite3.connect("instituto_de _daniel.db")

conn.execute(
    """
    CREATE TABLE if not exists cursos (
        id INTEGER PRIMARY KEy,
        descripcion TEXT not null,
        horas INTEGER not null
        )
        """
    
)

conn.execute(
    """
    CREATE TABLE if not exists estudiantes (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        fecha_nacimiento TEXT NOT NULL
    )
    """
)

conn.execute(
    """
    create table if not exists inscripciones (
        id INTEGER PRIMARY KEY,
        fecha text not null,
        curso_id INTEGER not null,
        estudiante_id INTEGER not null,
        foreign key (curso_id) references cursos(id),
        foreign key (estudiante_id) references estudiantes(id)
    )
    """
)

# incripcion a los cursos a Daniel
conn.execute(
    """
    insert into inscripciones (fecha, curso_id, estudiante_id)
    values ('2023-10-01', 1, 1)
    """
)

conn.execute(
    """
    insert into inscripciones (fecha, curso_id, estudiante_id)
    values ('2023-10-01', 1, 2)
    """
)


# conn.execute(
#     """
#     insert into cursos (descripcion, horas)
#     values ('java  principiante', 20)
#     """
# )
# conn.commit()

# conn.execute(
#     """
#     insert into estudiantes (nombre, apellidos, fecha_nacimiento)
#     values
#     ('Daniel', 'Quispe Gutierrez', '2004-09-30')
#     """
# )
# conn.commit()

print("\nCursos:")

cursor = conn.execute("select * from cursos")
for row in cursor:
    print(row)

print("\nEstudiantes:")
cursor = conn.execute("select * from estudiantes")
for fila in cursor:
    print(fila)
    

    
print("\ninscripciones:")
cursor = conn.execute("select * from inscripciones")
for fila in cursor:
    print(fila)
    
    
    
conn.execute("DELETE FROM estudiantes WHERE id IN (2, 3)")
conn.commit()