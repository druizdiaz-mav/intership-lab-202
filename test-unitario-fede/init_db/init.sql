CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS ordenes (
    id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_cliente
        FOREIGN KEY(cliente_id) 
        REFERENCES clientes(id)
);

-- Tabla para Items de Orden 
CREATE TABLE IF NOT EXISTS items_orden (
    id SERIAL PRIMARY KEY,
    orden_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_orden
        FOREIGN KEY(orden_id) 
        REFERENCES ordenes(id),
    CONSTRAINT fk_producto
        FOREIGN KEY(producto_id) 
        REFERENCES productos(id)
)
