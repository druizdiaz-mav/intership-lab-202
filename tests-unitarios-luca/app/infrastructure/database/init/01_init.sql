-- DEFINICIÓN DE TABLAS 

-- CLIENTES
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    activo BOOLEAN DEFAULT TRUE
);

-- PRODUCTOS
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

-- ORDENES
CREATE TABLE IF NOT EXISTS ordenes (
    id SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2), -- Puede ser NULL al inicio, se calcula luego, yo no lo pondría ya que se puede obtener de los datos de los items (cantidad * precio_unitario)

    CONSTRAINT fk_cliente_orden
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id)
        ON DELETE RESTRICT
);

-- ITEMS DE ORDEN
CREATE TABLE IF NOT EXISTS orden_items (
    id_orden INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,

    -- DEFINICIÓN DE UNA PK COMPUESTA
    PRIMARY KEY (id_orden, id_producto),

    CONSTRAINT fk_orden_item
        FOREIGN KEY (id_orden)
        REFERENCES ordenes(id)
        ON DELETE CASCADE, --Si se borra una orden, se borran sus items
    CONSTRAINT fk_producto_item
        FOREIGN KEY (id_producto)
        REFERENCES productos(id)
        ON DELETE RESTRICT --No permite borrar un producto si está presente en una orden
);

-- INSERCIÓN DE DATOS INICIALES
INSERT INTO clientes (nombre, activo) VALUES 
    ('Juan Perez', true),
    ('Maria Garcia', true),
    ('Empresa Fantasma SA', false);

INSERT INTO productos (nombre, precio) VALUES 
    ('Laptop Developer', 1500.00),
    ('Mouse Ergonómico', 50.00),
    ('Monitor 4K', 400.00);