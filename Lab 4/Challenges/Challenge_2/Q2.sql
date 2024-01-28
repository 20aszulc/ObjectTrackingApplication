CREATE TABLE teachers (
    id			      INT NOT NULL auto_increment,
    name		      VARCHAR(100) NOT NULL,
    primary key (id)
);

CREATE TABLE grades (
    id		          INT NOT NULL auto_increment,
    teacher_id	      integer NULL,
    grade	          VARCHAR(100) NOT NULL,
    primary key (id)
);

CREATE TABLE courses (
    id			      INT NOT NULL auto_increment,
    name		      VARCHAR(100) NOT NULL,
    teacher_id	      integer NULL,
    primary key (id)
);

CREATE TABLE students (
    id			      INT NOT NULL auto_increment,
    name		      VARCHAR(100) NOT NULL,
    email	          VARCHAR(100) NOT NULL,
    password    	  VARCHAR(100) NOT NULL,
    primary key (id)
);