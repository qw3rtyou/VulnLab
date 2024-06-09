CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL
);

-- 게시물 테이블 생성
CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    content TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES user(id)
);

-- 기본 관리자 계정 추가
INSERT INTO user (username, password) VALUES ('admin', 'shfyjgukhfsd,r,ghakuhafuerhguhtgjtkhu');

-- 기본 관리자 계정이 작성한 기본 게시글 추가
INSERT INTO post (content, author_id) VALUES ('K0{IDOR_is_very_easy}', 1);