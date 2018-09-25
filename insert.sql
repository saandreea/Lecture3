INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Shanghai', 'Paris', 760);
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Paris', 435);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Paris', 245);
INSERT INTO flights (origin, destination, duration) VALUES ('Lima', 'New York', 455);
INSERT INTO flights (origin, destination, duration) VALUES ('Bucharest', 'Bali', 540);

INSERT INTO locations (code, name) VALUES ('JFK', 'New York');
INSERT INTO locations (code, name) VALUES ('PVG', 'Shanghai');
INSERT INTO locations (code, name) VALUES ('IST', 'Istanbul');
INSERT INTO locations (code, name) VALUES ('LHR', 'London');
INSERT INTO locations (code, name) VALUES ('SVO', 'Moscow');
INSERT INTO locations (code, name) VALUES ('LIM', 'Lima');
INSERT INTO locations (code, name) VALUES ('CDG', 'Paris');
INSERT INTO locations (code, name) VALUES ('NRT', 'Tokyo');
INSERT INTO locations (code, name) VALUES ('DPS', 'Bali');
INSERT INTO locations (code, name) VALUES ('OTP', 'Bucharest');

INSERT INTO flights2 (origin_id, destination_id, duration) VALUES (1, 4, 415);
INSERT INTO flights2 (origin_id, destination_id, duration) VALUES (2, 7, 760);
INSERT INTO flights2 (origin_id, destination_id, duration) VALUES (3, 8, 700);
INSERT INTO flights2 (origin_id, destination_id, duration) VALUES (1, 7, 435);
INSERT INTO flights2 (origin_id, destination_id, duration) VALUES (5, 7, 245);
INSERT INTO flights2 (origin_id, destination_id, duration) VALUES (6, 1, 455);
INSERT INTO flights2 (origin_id, destination_id, duration) VALUES (10, 9, 540);

INSERT INTO passangers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passangers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passangers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passangers (name, flight_id) VALUES ('Dave', 2);
INSERT INTO passangers (name, flight_id) VALUES ('Erin', 4);
INSERT INTO passangers (name, flight_id) VALUES ('Frank', 6);
INSERT INTO passangers (name, flight_id) VALUES ('Grace', 6);