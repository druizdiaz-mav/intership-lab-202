CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    active INTEGER NOT NULL
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    price FLOAT NOT NULL
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    total FLOAT NOT NULL
);