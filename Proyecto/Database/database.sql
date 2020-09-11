DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS departamento;

CREATE TABLE productos( 
    id_product INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    precio INT
);

CREATE TABLE departamentos(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    FOREIGN KEY (id_product) REFERENCES productos(id_product)
);