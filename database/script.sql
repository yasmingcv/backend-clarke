create database db_clarke;
USE db_clarke;


CREATE TABLE tbl_state (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  state VARCHAR(5) NOT NULL,
  UNIQUE INDEX (id)
  
);

CREATE TABLE tbl_provider (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  logo TEXT NOT NULL,
  cost_per_kwh FLOAT NOT NULL,
  minimun_kwh_limit INT NOT NULL,
  average_rating FLOAT NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(32) NOT NULL,
  total_clients INT DEFAULT 0,
  id_state INT NOT NULL,
  
  UNIQUE INDEX (id),
 
  CONSTRAINT `fk_tbl_provider_tbl_state`
  FOREIGN KEY (id_state)
  REFERENCES tbl_state (`id`)
  
  );


CREATE TABLE tbl_client (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(32) NOT NULL,
  
  UNIQUE INDEX (id)
);


CREATE TABLE tbl_client_provider (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_client INT NOT NULL,
  id_provider INT NOT NULL,
 
  UNIQUE INDEX (id),
 
  CONSTRAINT `fk_tbl_client_provider_tbl_client1`
  FOREIGN KEY (id_client)
  REFERENCES tbl_client (id),
   
  CONSTRAINT `fk_tbl_client_provider_tbl_provider1`
  FOREIGN KEY (id_provider)
  REFERENCES tbl_provider (id)
    
);


DELIMITER $$
create trigger tgr_count_clients
after insert on tbl_client_provider
for each row
BEGIN
    update tbl_provider set total_clients = total_clients + 1
    where id = new.id_provider;
END;
$$