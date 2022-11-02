DROP TABLE IF EXISTS metrics;
CREATE TABLE metrics (
    id integer,
    val1 numeric(7,5),
    val2 numeric(7,5),
    cat varchar(100)
);

INSERT INTO metrics
SELECT
    generate_series(1, 10000) as id,
    random() as val1,
    random() as val2,
    (array['A', 'B', 'C'])[floor(random() * 3 + 1)] as cat
;