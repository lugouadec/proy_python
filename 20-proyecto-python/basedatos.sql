create database if not exists master_python;

use master_python;

create table if not exists usuarios(
    id int auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(255),
    email       varchar(255),
    password    varchar(255),
    fecha       date not null,
    constraint pk_usuarios primary key(id),
    constraint uq_email unique (email)
)engine=Innodb;

create table if not exists notas(
    id          int auto_increment not null,
    usuario_id  int not null,
    titulo      varchar(255) not null,
    descripcion mediumtext,
    fecha       date not null,

    CONSTRAINT pk_notas primary key (id),
    CONSTRAINT fk_nota_usuario foreign key (usuario_id) references usuarios(id)
)engine=Innodb;