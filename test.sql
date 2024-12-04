-- Table "users" : utilisateurs
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

-- Table "products" : produits
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Table "orders" : commandes
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Table "order_details" : détails des commandes
CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- Données des utilisateurs
INSERT INTO users (user_id, name, email) VALUES
(1, 'Alice', 'alice@example.com'),
(2, 'Bob', 'bob@example.com'),
(3, 'Charlie', 'charlie@example.com');

-- Données des produits
INSERT INTO products (product_id, name, price) VALUES
(1, 'Laptop', 1000.00),
(2, 'Mouse', 25.00),
(3, 'Keyboard', 45.00);

-- Données des commandes
INSERT INTO orders (order_id, user_id, order_date) VALUES
(1, 1, '2024-12-01'),
(2, 2, '2024-12-02');

-- Données des détails des commandes
INSERT INTO order_details (order_detail_id, order_id, product_id, quantity) VALUES
(1, 1, 1, 1),
(2, 1, 2, 2),
(3, 2, 2, 1),
(4, 2, 3, 1);

SELECT o.order_id, u.name AS user_name, o.order_date FROM orders o JOIN users u ON o.user_id = u.user_id;
SELECT od.order_detail_id, u.name AS user_name, p.name AS product_name, od.quantity, p.price, (od.quantity * p.price) AS total_price FROM order_details od JOIN orders o ON od.order_id = o.order_id JOIN users u ON o.user_id = u.user_id JOIN products p ON od.product_id = p.product_id;
SELECT  u.user_id, u.name AS user_name, SUM(od.quantity * p.price) AS total_spent FROM users u JOIN orders o ON u.user_id = o.user_id JOIN order_details od ON o.order_id = od.order_id JOIN products p ON od.product_id = p.product_id GROUP BY u.user_id, u.name;
