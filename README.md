# MTHFR Support Reports

This repository contains utilities for building MTHFR Support PDF reports. It includes
helper functions for assembling report data and a small Flask API that exposes
endpoints for generating the PDFs.

## Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Running the API

Start the server by executing `main.py`:

```bash
python main.py
```

The application listens on port `8000` by default.

## Testing with `curl`

After starting the server you can verify an endpoint with a simple `curl` request.
For example, to generate a variant report run:

```bash
curl -X POST http://localhost:8000/report/variant \
     -H "Content-Type: application/json" \
     -d '{"genotypes": [{"rsid": "rs123", "genotype": "AA"}]}' \
     --output variant_report.pdf
```

This saves the generated PDF to `variant_report.pdf`.

## Endpoints

### `POST /report/variant`
Generate the standard variant report. The request body should be JSON with a
`genotypes` list containing objects with at least `rsid` and `genotype` keys.
Optional keys `file_name` and `folder_name` can be provided to customize the
resulting PDF headers.  A body key `output` can be set to `"file"` to save the
resulting PDF under the repository `tmp/` directory instead of streaming the
binary back in the response.

### `POST /report/methylation`
Create a methylation report using the same payload format as `/report/variant`.
The optional `output` field behaves the same as the variant endpoint.

### `POST /report/covid`
Create the COVID‑19 report. The payload format matches the previous endpoints
and also accepts the `output` field.

All endpoints return the generated PDF as an attachment. If an error occurs a
JSON response with an `error` key is returned instead.

## Generating Reports Manually

The `compute.py` module exposes helper functions that can be used without the
API. For example:

```python
import pandas as pd
import compute

# dataframe with columns 'rsid' and 'genotype'
df = pd.DataFrame([...])
result = compute.create_dataframe(df)
report_bytes = compute.generate_pdf(result, "My Report", "folder")

# or save directly to a file
compute.generate_pdf(result, "My Report", "folder", output_path="tmp/my.pdf")
```

The output bytes can then be written to a file or specify ``output_path`` to let
the function handle saving.
