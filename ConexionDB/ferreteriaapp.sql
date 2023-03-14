-- Active: 1678747281380@@127.0.0.1@3306@ferreteriaapp
    INSERT INTO productos(
            `cod_productos`, `descripcion`, `unidad`, `precio`
        )
        VALUES(
            "02ali",
            "alicate",
            "unidad",
            12
        );

    SELECT * FROM productos;

    CREATE VIEW vista_productos AS
    SELECT cod_productos, descripcion, unidad, precio
    FROM productos;

    INSERT INTO
    `usuarios` (
        `nombre`,
        `apellidos`,
        `nom_user`,
        `password`,
        `correo`,
        `numero`,
        `dni`
    )
VALUES (
        'Roy',
        'Flores',
        'fortalezawtf2',
        '123456789',
        'fortalezawtf2@gmail.com',
        '959596552',
        '749966281'
    );

    SELECT * FROM usuarios