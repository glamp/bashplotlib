SELECT
  lat::varchar || ',' || lng
FROM
  sf_coords
WHERE
    lng < -107
;
