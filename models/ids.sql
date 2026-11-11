MODEL (
  name ror.ids,
  kind FULL,
  grain id,
  columns (
    id text
  )
);

SELECT
  json->>'$.id' as id
FROM ror.json_raw;
