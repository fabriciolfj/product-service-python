-- Criação da tabela categories
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    description VARCHAR NOT NULL
);

-- Criação da tabela products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    code VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    status VARCHAR NOT NULL,
    value NUMERIC NOT NULL,
    category_id BIGINT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);