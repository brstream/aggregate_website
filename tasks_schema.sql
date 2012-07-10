CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(100) NOT NULL,
    closed BOOL NOT NULL
);

INSERT OR IGNORE INTO tasks (id, name, closed) VALUES (1, 'Start learning Pyramid', 0);
INSERT OR IGNORE INTO tasks (id, name, closed) VALUES (2, 'Do quick tutorial', 0);
INSERT OR IGNORE INTO tasks (id, name, closed) VALUES (3, 'Have some beer!', 0);

CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text CHAR(100) NOT NULL,
    url CHAR(1000) NOT NULL
);

INSERT OR IGNORE INTO urls (id, text, url) VALUES (1, 'The Python website', 'http://python.org');
INSERT OR IGNORE INTO urls (id, text, url) VALUES (2, 'The Deer Park website', 'http://deerparkmonastery.org');
INSERT OR IGNORE INTO urls (id, text, url) VALUES (3, 'The Plum Village website', 'http://plumvillage.org');
