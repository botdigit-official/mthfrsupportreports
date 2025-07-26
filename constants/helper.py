def create_link(url):
    """
    Creates an HTML anchor tag <a> given the text and URL.

    :param text: The text to display for the link.
    :param url: The URL to link to.
    :return: A string containing the HTML <a> tag.
    """
    return f'<a href="{url}" color="blue"><u>{url}</u></a>'


def create_link_text(url, text):
    """
    Creates an HTML anchor tag <a> given the text and URL.

    :param text: The text to display for the link.
    :param url: The URL to link to.
    :return: A string containing the HTML <a> tag.
    """
    return f'<a href="{url}" color="blue"><u>{text}</u></a>'


def check_result(row):
    """Return a result string based on genotype and risk allele."""
    genotype = str(row.get("genotype", "")).upper()
    risk = str(row.get("Risk", "")).upper()
    if not genotype or not risk:
        return ""
    risk_alleles = list(risk)
    matches = sum(1 for a in genotype if a in risk_alleles)
    if matches == 2:
        return "+/+"
    if matches == 1:
        return "+/-"
    return "-/-"


def get_result_color(result):
    """Map a result string to a table background colour."""
    mapping = {
        "+/+": "#FC787F",  # red
        "+/-": "#FBFBC0",  # yellow
        "-/-": "#75B776",  # green
    }
    return mapping.get(result.strip(), "white")


def create_primary_snps(story, header, points, studies):
    """Append primary SNP information to the story list."""
    from reportlab.lib.enums import TA_LEFT
    from reportlab.platypus import Paragraph, Spacer, ListFlowable, ListItem
    from reportlab.lib.styles import getSampleStyleSheet, ListStyle

    styles = getSampleStyleSheet()
    header_style = styles["Heading2"]
    header_style.fontName = "Times-Bold"
    header_style.alignment = TA_LEFT
    story.append(Paragraph(header, header_style))

    bullet_style = ListStyle("bullet")
    items = []
    for item in points:
        items.append(ListItem(Paragraph(item.get("point", ""), styles["Normal"])) )
        for sub in item.get("subpoint", []):
            items.append(ListItem(Paragraph(sub, styles["Normal"]), level=1))
    story.append(ListFlowable(items, bulletType="bullet", style=bullet_style))

    if studies:
        story.append(Paragraph("Associated Studies", header_style))
        study_items = [ListItem(Paragraph(s, styles["Normal"])) for s in studies]
        story.append(ListFlowable(study_items, bulletType="bullet", style=bullet_style))

    story.append(Spacer(1, 12))
    return story


def create_secondary_snps(story, header, paragraphs):
    """Append secondary SNP text to the story list."""
    from reportlab.lib.enums import TA_LEFT
    from reportlab.platypus import Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet

    styles = getSampleStyleSheet()
    header_style = styles["Heading2"]
    header_style.fontName = "Times-Bold"
    header_style.alignment = TA_LEFT
    story.append(Paragraph(header, header_style))

    for p in paragraphs:
        story.append(Paragraph(p, styles["Normal"]))
        story.append(Spacer(1, 12))

    return story
