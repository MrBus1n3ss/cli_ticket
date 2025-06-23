CREATE TABLE IF NOT EXISTS project(id INTEGER PRIMARY KEY, name TEXT, description TEXT, created_at TIMESTAMP, modified_at TIMESTAMP);                    
CREATE TABLE IF NOT EXISTS ticket(id INTEGER PRIMARY KEY, project_id INTEGER, name TEXT, description TEXT, state INTEGER, priority TEXT, created_at TIMESTAMP, modified_at TIMESTAMP);
CREATE TABLE IF NOT EXISTS state(id INTEGER PRIMARY KEY, name TEXT);


INSERT INTO state (name) VALUES('todo'), ('hold'), ('progress'), ('testing'), ('finished');
