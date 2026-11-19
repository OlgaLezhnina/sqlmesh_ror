MODEL (
  name ror.wikidata_lookup,
  kind FULL,
  grain id, -- TODO: check what value makes sense
  columns (
    ror text,
    wikidata text,
  )
);

SELECT
  id as ror,
  external_id as wikidata,
FROM ror.external_ids
WHERE type = 'wikidata'
;
