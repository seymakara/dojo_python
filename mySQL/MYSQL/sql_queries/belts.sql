SET SQL_SAFE_UPDATES = 0;

INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ('Seyma', 'Akin', NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ('Halil', 'Akin', NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ('Nuri', 'Kara', NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ('Cansu', 'Comak', NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ('Hilal', 'Kuntuz', NOW(), NOW());

DELETE FROM belts.users WHERE id=1 or id = 2 or id=3 or id=4 or id=5 or id=6;

SELECT * from users;

INSERT INTO belts (name, created_at, updated_at) VALUES ('yellow belt', NOW(), NOW());
INSERT INTO belts (name, created_at, updated_at) VALUES ('red belt', NOW(), NOW());
INSERT INTO belts (name, created_at, updated_at) VALUES ('black belt', NOW(), NOW());

SELECT * FROM belts;

INSERT INTO belt_certifications (user_id, belt_id) VALUES (12,6);
INSERT INTO belt_certifications (user_id, belt_id) VALUES (13,6);
INSERT INTO belt_certifications (user_id, belt_id) VALUES (14,5);
INSERT INTO belt_certifications (user_id, belt_id) VALUES (15,4);
INSERT INTO belt_certifications (user_id, belt_id) VALUES (16,5);

SELECT * FROM belt_certifications;





