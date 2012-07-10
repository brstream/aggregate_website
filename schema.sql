CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text CHAR(1000) NOT NULL
);

INSERT OR IGNORE INTO events (id, text) VALUES (1, 'Summer Opening 2011\nFriday, July 7, 2011 at 2:00pm\nWake Up London and 64 other guests\nPlum Village Meditation Practice Center');
