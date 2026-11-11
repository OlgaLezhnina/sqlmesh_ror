MODEL (
  name ror.json_raw,
  kind VIEW,
  columns (
    json JSON
  )
);

SELECT
  *
FROM READ_JSON_OBJECTS('v2.15-2026-10-20-ror-data.json', format = 'array')
