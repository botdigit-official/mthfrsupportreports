import pandas as pd
from io import BytesIO
from flask import Flask, request, send_file, jsonify
import compute

app = Flask(__name__)


def _parse_genotypes(data):
    """Convert incoming JSON data to DataFrame."""
    if not isinstance(data, list):
        raise ValueError("'genotypes' must be a list of objects")
    return pd.DataFrame(data)


@app.route("/report/variant", methods=["POST"])
def variant_report():
    try:
        body = request.get_json(force=True)
        df = _parse_genotypes(body.get("genotypes", []))
        file_name = body.get("file_name", "Variant Report")
        folder_name = body.get("folder_name", "")
        dataf = compute.create_dataframe(df)
        pdf_bytes = compute.generate_pdf(dataf, file_name, folder_name)
        return send_file(BytesIO(pdf_bytes), mimetype="application/pdf", as_attachment=True, download_name="variant_report.pdf")
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.route("/report/methylation", methods=["POST"])
def methylation_report():
    try:
        body = request.get_json(force=True)
        df = _parse_genotypes(body.get("genotypes", []))
        file_name = body.get("file_name", "Methylation Report")
        folder_name = body.get("folder_name", "")
        dataf = compute.create_meth_dataframe(df)
        pdf_bytes = compute.generate_pdf(dataf, file_name, folder_name)
        return send_file(BytesIO(pdf_bytes), mimetype="application/pdf", as_attachment=True, download_name="methylation_report.pdf")
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.route("/report/covid", methods=["POST"])
def covid_report():
    try:
        body = request.get_json(force=True)
        df = _parse_genotypes(body.get("genotypes", []))
        file_name = body.get("file_name", "Covid Report")
        folder_name = body.get("folder_name", "")
        dataf = compute.create_covid_dataframe(df)
        pdf_bytes = compute.generate_covid_pdf(dataf, file_name, folder_name)
        return send_file(BytesIO(pdf_bytes), mimetype="application/pdf", as_attachment=True, download_name="covid_report.pdf")
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
