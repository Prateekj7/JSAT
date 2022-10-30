DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS supplier_item;
DROP TABLE IF EXISTS order_item;

CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category (id)
);

CREATE TABLE supplier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL
);

CREATE TABLE supplier_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES supplier (id),
    FOREIGN KEY (item_id) REFERENCES item (id)
);

CREATE TABLE order_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employee (id),
    FOREIGN KEY (item_id) REFERENCES item (id)
);