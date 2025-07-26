from reportlab.platypus import Paragraph, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, ListStyle

# Result colors used by the PDF tables
_RESULT_COLORS = {
    "-/ -": "#75B776",
    "-/-": "#75B776",
    "+/+": "#FC787F",
    "+/-": "#FBFBC0",
}


def get_result_color(result: str) -> str:
    """Return background color for a result string."""
    return _RESULT_COLORS.get(result.strip(), "white")


def check_result(row) -> str:
    """Calculate the result string for a dataframe row.

    This looks at the `genotype` column compared to the risk allele stored in
    the `Risk` column and returns one of ``+/+``, ``+/-`` or ``-/-``.
    """
    genotype = str(row.get("genotype", "")).upper()
    risk = str(row.get("Risk", "")).upper()

    if not genotype or not risk:
        return "-/-"

    count = sum(1 for allele in genotype if allele == risk)
    if count == 2:
        return "+/+"
    elif count == 1:
        return "+/-"
    else:
        return "-/-"


def _bullet_paragraph(text: str, level: int = 0) -> Paragraph:
    styles = getSampleStyleSheet()
    style = ParagraphStyle(
        f"bullet_level_{level}",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=12 - level,
        leftIndent=20 * (level + 1),
        bulletFontName="Times-Roman",
        bulletFontSize=12 - level,
    )
    return Paragraph(text, style, bulletText="\u2022")


def create_primary_snps(story, header, points, studies):
    """Append primary SNP information to the story list."""
    styles = getSampleStyleSheet()
    header_style = styles["Heading2"]
    header_style.fontName = "Times-Bold"

    story.append(Paragraph(header, header_style))

    for entry in points:
        story.append(_bullet_paragraph(entry.get("point", ""), 0))
        for sub in entry.get("subpoint", []):
            story.append(_bullet_paragraph(sub, 1))

    if studies:
        story.append(Paragraph("Associated Studies", header_style))
        for link in studies:
            story.append(Paragraph(link, styles["Normal"]))


def create_secondary_snps(story, header, paragraphs):
    """Append secondary SNP information to the story list."""
    styles = getSampleStyleSheet()
    header_style = styles["Heading2"]
    header_style.fontName = "Times-Bold"

    story.append(Paragraph(header, header_style))

    for section in paragraphs:
        para = section.get("para")
        if para:
            story.append(Paragraph(para, styles["Normal"]))
        for point in section.get("point", []):
            story.append(_bullet_paragraph(point, 0))
    return story
