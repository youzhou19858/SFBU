SELECT
weight_pounds,
mother_age,
father_age,
gestation_weeks,
weight_gain_pounds,
apgar_5min
FROM
`bigquery-public-data.samples.natality`
WHERE
weight_pounds IS NOT NULL
AND mother_age IS NOT NULL
AND father_age IS NOT NULL
AND gestation_weeks IS NOT NULL
AND weight_gain_pounds IS NOT NULL
AND apgar_5min IS NOT NULL
LIMIT 256;