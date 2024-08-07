CREATE SEQUENCE member_id_sq
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;


CREATE TABLE Member (
    member_id NUMBER PRIMARY KEY ,
    name VARCHAR2(100) NOT NULL,
    address VARCHAR2(200),
    phone VARCHAR2(20) UNIQUE
);

CREATE SEQUENCE author_id_sq 
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

CREATE TABLE Author (
    author_id NUMBER PRIMARY KEY ,
    name VARCHAR2(100) NOT NULL,
    biography VARCHAR2(400)
);

CREATE SEQUENCE genre_id_sq  
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

CREATE TABLE Genre (
    genre_id NUMBER PRIMARY KEY ,
    genre_name VARCHAR2(50) UNIQUE NOT NULL
);

CREATE SEQUENCE library_id_sq  
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

CREATE TABLE Library (
    library_id NUMBER PRIMARY KEY ,
    phone VARCHAR2(20) UNIQUE,
    address VARCHAR2(200) NOT NULL
);
CREATE SEQUENCE book_id_sq
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

CREATE TABLE Book (
    book_id NUMBER,
    isbn VARCHAR2(20) PRIMARY KEY,
    title VARCHAR2(200) NOT NULL,
    genre_id NUMBER,
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE SEQUENCE borrowing_id_sq  
    START WITH 0
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

CREATE TABLE Borrowing (
    borrowing_id NUMBER PRIMARY KEY ,
    isbn VARCHAR2(20),
    member_id NUMBER,
    return_date DATE,
    borrow_date DATE,
    FOREIGN KEY (isbn) REFERENCES Book(isbn),
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

-- Constraints
ALTER TABLE Author ADD CONSTRAINT author_biography_check CHECK (LENGTH(biography) <= 400);
ALTER TABLE Library ADD CONSTRAINT library_address_unique UNIQUE (address);
ALTER TABLE Book ADD CONSTRAINT book_title_unique UNIQUE (title);
ALTER TABLE Borrowing ADD CONSTRAINT borrowing_return_date_check CHECK (return_date > borrow_date);

-- Inserting data
-- Member
INSERT INTO Member (member_id,name, address, phone) VALUES (member_id_sq.nextval,'John Doe', '123 Main St', '555-1234');
INSERT INTO Member (member_id,name, address, phone) VALUES (member_id_sq.nextval,'Jane Smith', '456 Elm St', '555-5678');
INSERT INTO Member (member_id,name, address, phone) VALUES (member_id_sq.nextval,'Bob Johnson', '789 Oak St', '555-9012');
INSERT INTO Member (member_id,name, address, phone) VALUES (member_id_sq.nextval,'Alice Brown', '101 Pine St', '555-3456');
INSERT INTO Member (member_id,name, address, phone) VALUES (member_id_sq.nextval,'Michael Lee', '202 Maple St', '555-7890');
-- Author
INSERT INTO Author (author_id,name, biography) VALUES (author_id_sq.nextval,'Stephen King', 'Stephen King is an American author known for his horror and suspense novels.');
INSERT INTO Author (author_id,name, biography) VALUES (author_id_sq.nextval,'J.K. Rowling', 'J.K. Rowling is a British author best known for her Harry Potter series.');
INSERT INTO Author (author_id,name, biography) VALUES (author_id_sq.nextval,'Agatha Christie', 'Agatha Christie was an English writer known for her detective novels and short story collections.');
INSERT INTO Author (author_id,name, biography) VALUES (author_id_sq.nextval,'George Orwell', 'George Orwell was an English novelist and essayist known for his dystopian fiction, including "1984" and "Animal Farm".');
INSERT INTO Author (author_id,name, biography) VALUES (author_id_sq.nextval,'Harper Lee', 'Harper Lee was an American novelist best known for her novel "To Kill a Mockingbird".');

-- Genre
INSERT INTO Genre (genre_id,genre_name) VALUES (genre_id_sq.nextval,'Horror');
INSERT INTO Genre (genre_id,genre_name) VALUES (genre_id_sq.nextval,'Fantasy');
INSERT INTO Genre (genre_id,genre_name) VALUES (genre_id_sq .nextval,'Mystery');
INSERT INTO Genre (genre_id,genre_name) VALUES (genre_id_sq .nextval,'Science Fiction');
INSERT INTO Genre (genre_id,genre_name) VALUES (genre_id_sq .nextval,'Classics');

-- Library
INSERT INTO Library (library_id,phone, address) VALUES (library_id_sq.nextval,'555-1111', '321 Oak St');
INSERT INTO Library (library_id,phone, address) VALUES (library_id_sq.nextval,'555-2222', '654 Pine St');
INSERT INTO Library (library_id,phone, address) VALUES (library_id_sq.nextval,'555-3333', '987 Elm St');
INSERT INTO Library (library_id,phone, address) VALUES (library_id_sq.nextval,'555-4444', '210 Maple St');
INSERT INTO Library (library_id,phone, address) VALUES (library_id_sq.nextval,'555-5555', '753 Main St');

-- Book
INSERT INTO Book (book_id,isbn, title, genre_id) VALUES ( book_id_sq.nextval,'978-1982105402', 'The Shining', 1);
INSERT INTO Book (book_id,isbn, title, genre_id) VALUES (book_id_sq.nextval,'978-0439554930', 'Harry Potter and the Sorcerer''s Stone', 2);
INSERT INTO Book (book_id,isbn, title, genre_id) VALUES (book_id_sq.nextval,'978-0312983477', 'Murder on the Orient Express', 3);
INSERT INTO Book (book_id,isbn, title, genre_id) VALUES (book_id_sq.nextval,'978-0451526342',   '1984', 4);
INSERT INTO Book (book_id,isbn, title, genre_id) VALUES (book_id_sq.nextval,'978-0061120084',   'To Kill a Mockingbird', 5);


-- Borrowing
INSERT INTO Borrowing (borrowing_id, isbn, member_id, return_date, borrow_date) VALUES (borrowing_id_sq.nextval, '978-1982105402', 1, TO_DATE('2024-06-05', 'YYYY-MM-DD'), TO_DATE('2024-05-05', 'YYYY-MM-DD'));
INSERT INTO Borrowing (borrowing_id,isbn, member_id, return_date, borrow_date)VALUES (borrowing_id_sq .nextval,'978-0439554930', 2,  TO_DATE('2024-06-12', 'YYYY-MM-DD'), TO_DATE('2024-05-05', 'YYYY-MM-DD'));
INSERT INTO Borrowing (borrowing_id,isbn, member_id, return_date, borrow_date) VALUES (borrowing_id_sq .nextval,'978-0312983477', 3, TO_DATE('2024-06-19', 'YYYY-MM-DD'), TO_DATE('2024-05-05', 'YYYY-MM-DD'));
INSERT INTO Borrowing (borrowing_id,isbn, member_id, return_date, borrow_date) VALUES (borrowing_id_sq .nextval,'978-0451526342', 4,TO_DATE('2024-06-26', 'YYYY-MM-DD'), TO_DATE('2024-05-05', 'YYYY-MM-DD'));
INSERT INTO Borrowing (borrowing_id,isbn, member_id, return_date, borrow_date) VALUES (borrowing_id_sq .nextval,'978-0061120084', 5, TO_DATE('2024-07-03', 'YYYY-MM-DD'), TO_DATE('2024-05-05', 'YYYY-MM-DD'));
