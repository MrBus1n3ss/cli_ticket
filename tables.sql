CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY, title TEXT, priority INTEGER, project TEXT, description TEXT, completed TEXT, start_date TIMESTAMP, finish_date TIMESTAMP);
CREATE TABLE IF NOT EXISTS application_properties(id INTEGER PRIMARY KEY, name TEXT, value TEXT);
