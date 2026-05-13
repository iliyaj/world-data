# World Data Repository

A data repository containing world country reference data as CSV files sourced from the World Bank, UN Population Division, and ISO 3166-1 standards.

## Data Files

All data lives in the `data/` directory:

| File | Columns | Records | Source |
|------|---------|---------|--------|
| **country_name.csv** | `alpha_3_code`, `common_english_name`, `official_country_name` | ~197 | ISO 3166-1 |
| **country_area.csv** | `Alpha 3 code`, `Land` (km²), `Water` (km²) | ~195 | World Bank |
| **country_name_iso_3166.csv** | `english_short_name`, `french_short_name`, `alpha_2_code`, `alpha_3_code`, `numeric` | ~249 | ISO 3166-1 Standard |
| **country_population.csv** | `alpha_3_code`, `population`, `year` | 215 (2024) | World Bank SP.POP.TOTL |
| **country_gdp.csv** | `alpha_3_code`, `gdp_usd`, `year` | 191 (2024) | World Bank NY.GDP.MKTP.CD |
| **un_locations.csv** | `id`, `parentId`, `iso3`, `iso2`, `name`, `locationType`, `locationTypeId`, `longitude`, `latitude` | 237 (real locations) | UN Population Division API |
| **missing_population_data.csv** | `alpha_3_code`, `country_name`, `notes` | 34 | Reference for data collection |

### Join Key

The **ISO Alpha-3 code** (`alpha_3_code`) is the primary join key across all files.

## Extraction Notebooks

Extraction notebooks live in `extract/` and produce the CSVs above from raw World Bank downloads in `raw/`.

- **`population_extract.ipynb`** — produces `country_population.csv`
- **`gdp_extract.ipynb`** — produces `country_gdp.csv`

### Running Extraction Notebooks

Execute from the repo root using `--output-dir` to avoid path issues:

```bash
python -m nbconvert --to notebook --execute extract/<notebook>.ipynb --output <notebook>.ipynb --output-dir extract
```

**Important:** nbconvert runs from the notebook's directory, so each notebook includes an `os.chdir` cell to step back to the repo root. Do NOT use `--output extract/<notebook>.ipynb` (it doubles the path).

## Data Coverage

- **Countries with population data**: 215 / 249 ISO entries
- **Countries with GDP data**: 191 / 249 ISO entries
- **Missing territories**: 34 (documented in `missing_population_data.csv`)
  - 22 available in UN Population Division API
  - 12 not tracked by UN (mostly uninhabited or disputed territories)

## Data Quality Notes

- Population and GDP use `year` column (currently 2024)
- Large numeric values (GDP, population) are stored as `int64` to avoid overflow
- World Bank data is filtered to ISO 3166-1 codes only (excludes regional aggregates like WLD, ARB)
- All CSV files use UTF-8 encoding

## World Data Notebook

`world_data.ipynb` combines and analyzes the data across all files for exploratory work and validation.

## Contributing

When adding new World Bank indicators:

1. Create `extract/<indicator>_extract.ipynb` following the standard cell structure
2. Filter to ISO 3166-1 codes using `country_name_iso_3166.csv`
3. Include a `year` column
4. Use `int64` for large numeric values
5. Save to `data/<name>.csv`

See CLAUDE.md for detailed extraction guidelines and common gotchas.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

Data sourced from public domain sources:
- **World Bank**: Public domain
- **UN Population Division**: Public domain
- **ISO 3166-1**: Public information
