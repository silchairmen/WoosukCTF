CREATE TABLE users (
  idx int auto_increment primary key,
  username varchar(64) not null,
  password varchar(64) not null
);

-- sooooooooooooooo looooooooooooooooooooong password! you can't do bf attack
INSERT INTO users (username, password) values ('admin', '17751860592b0b43054b745a01ef534c7f08aab58b1f871b127aaee074a2fbe5');

-- guest password is guest
-- guest의 비밀번호는 guest입니다.
INSERT INTO users (username, password) values ('guest', '84983c60f7daadc1cb8698621f802c0d9f9a3c3c295c810748fb048115c186ec');
