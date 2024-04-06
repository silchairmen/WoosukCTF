CREATE TABLE users (
  idx int auto_increment primary key,
  username varchar(64) not null,
  password varchar(64) not null
);

INSERT INTO users (username, password) values ('admin119', '17751860592b0b43054b745a01ef534c7f08aab58b1f871b127aaee074a2fbe5');
INSERT INTO users (username, password) values ('admin112', 'af2722a4545f43e8dfe32e81b00d65d039260514ea9cc22cbf44c975f45576ee');

