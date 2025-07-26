import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Spacer,
    PageBreak,
    Paragraph,
    Image,
    Flowable
)
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from helper import check_result, get_result_color, create_primary_snps, create_secondary_snps
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from constants.constants import primary_genes, secondary_genes, gene_references
from io import BytesIO

pathway_reversed = {
    'Liver Detox': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/Liver_detox.jpeg',
    'Yeast/Alcohol Metabolism': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/yeast.jpeg',
    'Methylation & Methionine/Homocysteine Pathways': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/Methylation.jpeg',
    'Trans-Sulfuration Pathway': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/Trans_sulfuration.jpeg',
    'Serotonin & Dopamine': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/Neuro_transmitter.jpeg',
    'Glutamate & GABA': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/neuro_transmitter_glutamate.jpeg',
    'COMT Activity': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/COMT.jpeg',
    'Mitochondrial Function': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/electron_transport.jpeg',
    'Pentose Phosphate Pathway': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/Pentose_phosphate_pathway.jpeg',
    'Glyoxylate Metabolic Process': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/Glyphosate_degradation.jpeg',
    'Thiamin/Thiamine Degradation': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/Glycolysis.jpeg',
    'HLA': 'https://mthfrsupport.org/wp-content/uploads/pathway-images/biotoxin_pathway.jpeg'
}

figure_numbers = {
    'Liver Detox': 1,
    'Methylation & Methionine/Homocysteine Pathways': 2,
    'Serotonin & Dopamine': 3,
    'COMT Activity': 4,
    'Glyoxylate Metabolic Process': 5,
    'HLA' : 6,
    'Yeast/Alcohol Metabolism': 7,
    'Trans-Sulfuration Pathway':8,
    'Glutamate & GABA': 9,
    'Pentose Phosphate Pathway':10,
    'Thiamin/Thiamine Degradation': 11,
    'Mitochondrial Function':12
}


def generate_pdf(content, file_name, folder_name, font_size=11):
    pdf_output = BytesIO()

    class bookmark_flowable(Flowable):
    
        def __init__(self, name):
            super().__init__()
            self.name = name
    
        def draw(self):
            # Ensure the canvas has a custom attribute for bookmarks
            if not hasattr(self.canv, 'bookmarks'):
                self.canv.bookmarks = {}  # Initialize an empty dictionary for bookmarks
    
            # Check if bookmark already exists on the current canvas
            if self.name not in self.canv.bookmarks:
                page_number = self.canv.getPageNumber()  # Get current page number
                # Save the bookmark information along with the page number
                self.canv.bookmarks[self.name] = page_number

    
    class HeaderFooterCanvas(canvas.Canvas):

        def __init__(self, *args, **kwargs):
            self.pathway_images = kwargs.pop('pathway_images', [])
            self.current_image_index = 0
            canvas.Canvas.__init__(self, *args, **kwargs)
            self.pages = []
            self.bookmarks = {}
            self.filtered_destinations = []

        def showPage(self):
            self.pages.append(dict(self.__dict__))

            self._startPage()

        def save(self):
            page_count = len(self.pages)
            for page in self.pages:
                self.__dict__.update(page)
                self.draw_header_footer(page_count)
                canvas.Canvas.showPage(self)

            if 'variant' in file_name.lower() or 'meth' in file_name.lower():
            # After all regular pages are done, add pathway images
                if self.pathway_images:
                    self._pagesize = landscape(letter)  # Switch to landscape
                    self.bookmarkPage('Figures')
                    self.addOutlineEntry('Figures','Figures',level=0)
                    for i, img_path in enumerate(self.pathway_images):
                        self.bookmarkPage(f'Figure {img_path}')
                        self.addOutlineEntry(f'Figure {img_path}', f'Figure {img_path}', level=1)
                        self.draw_centered_image(f'{self.pathway_images[img_path]}')
                        self.draw_header_footer(page_count + len(self.pathway_images))
                        canvas.Canvas.showPage(self)
                
        
            canvas.Canvas.save(self)

        def draw_header_footer(self, page_count):
            page = f"{self._pageNumber}/{page_count}"

            for key, page_num in self.bookmarks.items():
                if page_num == self._pageNumber:
                    
                    self.bookmarkPage(key)
                    self.addOutlineEntry(key, key)
            

            page_width, page_height = letter
            page_width, page_height = self._pagesize  # Get current page size
            if page_width > page_height:
                orientation = 'Landscape'
            else:
                orientation = 'Portrait'
            
            PageWidth, PageHeight = landscape(letter)  # This automatically switches the width and height for landscape
            
            
            # Header
            right_margin = 50
            top_margin = 710
            right_text_position = 550
            stroke_line_width = page_width - 50
            footer_paragraph_width = 400

            if orientation == 'Landscape':
                top_margin = PageHeight - 80
                right_text_position = 750
                footer_paragraph_width = 650 
            
            # Header
            try:
                self.drawImage(
                    "report_logo.png",
                    right_margin,
                    top_margin,
                    width=2 * inch,
                    height=1 * inch,
                    preserveAspectRatio=True,
                )
            except:
                self.rect(right_margin, top_margin, 1 * inch, 1 * inch)
                self.setFont("Times-Roman", 8)
                self.drawString(55, top_margin + 20, "Logo")

            self.setFont("Times-Roman", 16)
            self.setFillColor(colors.black)
            self.drawRightString(right_text_position, top_margin + 35, file_name)

            self.setFont("Times-Roman", 12)
            self.setFillColor(colors.gray)
            self.drawRightString(right_text_position, top_margin + 20, folder_name)

            self.setStrokeColor(colors.black)
            self.line(50, top_margin + 10, right_text_position, top_margin + 10)

            # Footer
            footer_text_y_position = 40
            self.setFont("Times-Roman", 6)
            self.setFillColor(colors.black)

            footer_text = (
                "This report is intended to translate your results into an easier to understand form. It is not intended to diagnose or treat. For diagnosis or treatment, please present this to your doctor (or find a doctor on MTHFRSupport™ website under 'Find a Practitioner'). Additionally, genetic mutations are flags that something **could** be wrong and not a guarantee that you are having all or any of the associated issues. Other factors like environment, ethnic background, diet, age, personal history, etc all have a factor in whether a mutation starts to present itself or not and when. Copyright all rights reserved MTHFR Support™"
            )

            footer_style = ParagraphStyle(
                "footer_style",
                fontSize=6,
                fontName="Times-Roman",
                alignment=0,
            )
            footer_paragraph = Paragraph(footer_text, footer_style)
            footer_paragraph.wrapOn(self, footer_paragraph_width, 20)
            footer_paragraph.drawOn(self, 50, footer_text_y_position)

            if orientation == 'Landscape':
                footer_text_y_position = footer_text_y_position + 30
            else:
                footer_text_y_position = footer_text_y_position + 40

            self.setFont("Times-Roman", 10)
            self.drawRightString(right_text_position, footer_text_y_position, page)

        def draw_centered_image(self, img_path):
            try:
                # Get the current page size
                page_width, page_height = self._pagesize
                
                # Create an ImageReader object
                image_reader = ImageReader(img_path)
                img_width, img_height = image_reader.getSize()
                
                # Calculate scaling factors to fit the page while maintaining aspect ratio
                width_ratio = (page_width - 100) / img_width  # Leave 50px margin on each side
                height_ratio = (page_height - 200) / img_height  # Leave 100px margin top/bottom
                scale_factor = min(width_ratio, height_ratio)
                
                # Calculate new dimensions
                new_width = img_width * scale_factor
                new_height = img_height * scale_factor
                
                # Calculate position to center the image
                x = (page_width - new_width) / 2
                y = (page_height - new_height) / 2
                
                # Draw the image
                self.drawImage(
                    img_path,
                    x, y,
                    width=new_width,
                    height=new_height,
                    preserveAspectRatio=True
                )
                return True
            except Exception as e:
                print(f"Error drawing image {img_path}: {e}")
                return False
    
    margin = 50
    doc = SimpleDocTemplate(
        pdf_output,
        pagesize=letter,
        rightMargin=margin,
        leftMargin=margin,
        topMargin=90,
        bottomMargin=120,
    )

    story = []
    grouped = content.groupby("rs10306114")
    styles = getSampleStyleSheet()
    text_style = ParagraphStyle(
        "tablecellStyle",
        parent=styles["Normal"],
        fontSize=font_size,
        fontName="Times-Roman",
        alignment=1,
    )

    page_width, page_height = letter
    left_margin = 50
    right_margin = 50
    available_table_width = page_width - left_margin - right_margin
    col_widths_proportion = [90, 120, 90, 90, 90]
    total_proportion = sum(col_widths_proportion)
    col_widths = [
        available_table_width * (w / total_proportion) for w in col_widths_proportion
    ]

    pathways_exist = {}
    pathway_to_figure = {}  # Dictionary to map pathway keys to figure numbers
    condition_to_figure = {}  # Dictionary to map conditions to figure numbers
    current_figure = 1   # Counter for figure numbers
    
    # First pass: collect all figure numbers based on pathway keys
    
    if 'variant' in file_name.lower():
        for condition, _ in grouped:
            for key in pathway_reversed:
                if key in condition:
                    # If this pathway hasn't been assigned a figure number yet
                    # if pathway_reversed[key] not in pathway_to_figure:
                    #    pathway_to_figure[pathway_reversed[key]] = current_figure
                    #    pathways_exist.append(pathway_reversed[key])
                    #    current_figure += 1

                    # Assign the figure number to this condition
                    condition_to_figure[condition] = figure_numbers[key]
                    pathways_exist[figure_numbers[key]] = pathway_reversed[key]
                    # condition_to_figure[condition] = pathway_to_figure[pathway_reversed[key]]
                    # condition_to_figure[condition] = figure_numbers[key]
                    break

    if 'meth' in file_name.lower():
        grouped = sorted(grouped, reverse=True)
        # pathways_exist.append(pathway_reversed['Methylation & Methionine/Homocysteine Pathways'])
        pathways_exist[figure_numbers['Methylation & Methionine/Homocysteine Pathways']] = pathway_reversed['Methylation & Methionine/Homocysteine Pathways']
    
    pathways_exist = dict(sorted(pathways_exist.items())) 
        
    for condition, group in grouped:
        if 'variant' in file_name.lower():
            figure_num = condition_to_figure.get(condition)
            figure_text = f"(Figure {figure_num})" if figure_num is not None else ""
            
            # Create table data with figure number if it exists
            table_data = [
                [f"{condition} {figure_text}"],
                ["SNP ID", "SNP Name", "Risk Allele", "Your Allele", "Result"],
            ]
        else:
            table_data = [
                [f"{condition}"],
                ["SNP ID", "SNP Name", "Risk Allele", "Your Allele", "Result"],
            ]

        for _, row in group.iterrows():
            table_data.append(
                [
                    Paragraph(row["SNP ID"], text_style),
                    Paragraph(row["SNP Name"], text_style),
                    Paragraph(row["Risk Allele"], text_style),
                    Paragraph(row["Your Allele"], text_style),
                    Paragraph(row["Result"], text_style),
                ]
            )

        table = Table(table_data, colWidths=col_widths, repeatRows=2)

        style = TableStyle(
            [
                ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                ("SPAN", (0, 0), (-1, 0)),
                ("FONTNAME", (0, 0), (-1, 0), "Times-Roman"),
                ("FONTSIZE", (0, 0), (-1, 0), font_size),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("BACKGROUND", (0, 0), (-1, 0), "#1B80B6"),
                ("ALIGN", (0, 1), (-1, 1), "CENTER"),
                ("FONTNAME", (0, 1), (-1, 1), "Times-Roman"),
                ("FONTSIZE", (0, 1), (-1, 1), font_size),
                ("TEXTCOLOR", (0, 1), (-1, 1), colors.whitesmoke),
                ("BACKGROUND", (0, 1), (-1, 1), "#1B80B6"),
                ("ALIGN", (0, 2), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 2), (-1, -1), "Times-Roman"),
                ("FONTSIZE", (0, 2), (-1, -1), font_size),
                ("TEXTCOLOR", (0, 2), (-1, -1), colors.black),
                ("BACKGROUND", (0, 2), (-1, -1), colors.whitesmoke),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )

        for i in range(2, len(table_data)):
            if i % 2 == 0:
                style.add("BACKGROUND", (0, i), (-1, i), colors.whitesmoke)
            else:
                style.add("BACKGROUND", (0, i), (-1, i), colors.white)

        for i in range(2, len(table_data)):
            style.add(
                "BACKGROUND",
                (4, i),
                (4, i),
                get_result_color(
                    table_data[i][4].text
                    if isinstance(table_data[i][4], Paragraph)
                    else table_data[i][4]
                ),
            )

        table.setStyle(style)
        bookmark = bookmark_flowable(condition)
        story.append(bookmark)
        story.append(table)
        story.append(Spacer(1, 12))
        story.append(PageBreak())

    doc.build(
        story,
        canvasmaker=lambda *args, **kwargs: HeaderFooterCanvas(
            *args,
            pathway_images=pathways_exist,
            **kwargs
        )
    )
    pdf_data = pdf_output.getvalue()
    pdf_output.close()
    
    return pdf_data


def create_dataframe(df):

    
    data = pd.read_excel(
        "Database.xlsx"
    )
    # data_clean = data.dropna(subset=["SNP"])
    data_clean = data
    # Step 2: Filter for common RSID values
    common_rsid = data_clean[data_clean["RSID"].isin(df["rsid"])]

    # Step 3: Merge common_rsid with df on RSID to align corresponding data
    merged_df = pd.merge(common_rsid, df, left_on="RSID", right_on="rsid", how="inner")

    # Step 5: Create the SNP Name and result column using vectorized operations
    merged_df["SNP Name"] = (
        merged_df["Gene"].astype(str) + " " + merged_df['SNP'].astype(str).replace(['nan', 'NaN'], '')
    )
    merged_df["Result"] = merged_df.apply(check_result, axis=1)

    # Step 6: Select the desired columns for the final result
    final_df = merged_df[['RSID', 'SNP Name', 'Risk', 'genotype', 'Result', 'rs10306114','Report Name', 'Info', 'Video', 'Tags']]

    # Step 7: Rename columns if needed
    final_df.columns = ['SNP ID', 'SNP Name', 'Risk Allele', 'Your Allele', 'Result', 'rs10306114', 'Report Name', 'Info', 'Video', 'Tags']
    
    final_df = (
        final_df.groupby('rs10306114', group_keys=False)
        .apply(lambda x: x.sort_values('SNP Name', ascending=True)[final_df.columns])
        .reset_index(drop=True)  # Optional: Reset index if needed
    )
    return final_df


def create_meth_dataframe(df):
    # Step 1: Remove NaN values from SNP column
    data = pd.read_excel(
        "meth_database.xlsx"
    )
    # data_clean = data.dropna(subset=['SNP'])
    data_clean = data
    # Step 2: Filter for common RSID values
    common_rsid = data_clean[data_clean['RSID'].isin(df['rsid'])]

    # Step 3: Merge common_rsid with df on RSID to align corresponding data
    merged_df = pd.merge(common_rsid, df, left_on='RSID', right_on='rsid', how='inner')


    # Step 5: Create the SNP Name and result column using vectorized operations
    merged_df['SNP Name'] = merged_df['Gene'].astype(str) + " " + merged_df['SNP'].astype(str).replace(['nan', 'NaN'], '')
    merged_df['Result'] = merged_df.apply(check_result, axis=1)

    # Step 6: Select the desired columns for the final result
    final_df = merged_df[['rs10306114','RSID', 'SNP Name', 'Risk', 'genotype', 'Result', 'Info', 'Video', 'Tags']]

    # Step 7: Rename columns if needed
    final_df.columns = ['rs10306114','SNP ID', 'SNP Name', 'Risk Allele', 'Your Allele', 'Result', 'Info', 'Video', 'Tags']

    return final_df
    

def create_covid_dataframe(df):
    
    data = pd.read_excel(
        "Database.xlsx"
    )
    # data_clean = data.dropna(subset=["SNP"])
    data_clean = data
    primary_df = data_clean[data_clean["Gene"].isin(gene_references["Primary"])]
    secondary_df = data_clean[data_clean["Gene"].isin(gene_references["Secondary"])]

    common_primary_rsid = data_clean[data_clean["RSID"].isin(primary_df["RSID"])]
    common_primary_rsid = common_primary_rsid.drop_duplicates(subset='RSID', keep='first')

    common_secondary_rsid = data_clean[data_clean["RSID"].isin(secondary_df["RSID"])]
    common_secondary_rsid = common_secondary_rsid.drop_duplicates(subset='RSID', keep='first')


    # Step 4: Merge common RSID with df on RSID for both Primary and Secondary
    merged_primary = pd.merge(
        common_primary_rsid, df, left_on="RSID", right_on="rsid", how="inner"
    )
    merged_secondary = pd.merge(
        common_secondary_rsid, df, left_on="RSID", right_on="rsid", how="inner"
    )

    # Step 6: Apply function and create 'SNP Name' and 'Result' for both DataFrames
    merged_primary["SNP Name"] = (
        merged_primary["Gene"].astype(str) + " " + merged_primary['SNP'].astype(str).replace(['nan', 'NaN'], '')
    )
    merged_primary["Result"] = merged_primary.apply(check_result, axis=1)
    merged_primary["rs10306114"] = "Primary SNPs"  # Label as Primary

    merged_secondary["SNP Name"] = (
        merged_secondary["Gene"].astype(str) + " " + merged_secondary['SNP'].astype(str).replace(['nan', 'NaN'], '')
    )
    merged_secondary["Result"] = merged_secondary.apply(check_result, axis=1)
    merged_secondary["rs10306114"] = "Secondary SNPs"  # Label as Secondary

    # Step 7: Select desired columns
    final_primary_df = merged_primary[
        [
            "RSID",
            "SNP Name",
            "Gene",
            "Risk",
            "genotype",
            "Result",
            "rs10306114",
            "Report Name",
            "Info",
            "Video",
            "Tags",
        ]
    ]
    final_secondary_df = merged_secondary[
        [
            "RSID",
            "SNP Name",
            "Gene",
            "Risk",
            "genotype",
            "Result",
            "rs10306114",
            "Report Name",
            "Info",
            "Video",
            "Tags",
        ]
    ]
    final_primary_df = final_primary_df.sort_values(by='SNP Name', ascending=True)
    final_secondary_df = final_secondary_df.sort_values(by='SNP Name', ascending=True)


    # Step 8: Rename columns
    final_primary_df.columns = [
        "SNP ID",
        "SNP Name",
        "Gene",
        "Risk Allele",
        "Your Allele",
        "Result",
        "rs10306114",
        "Report Name",
        "Info",
        "Video",
        "Tags",
    ]
    final_secondary_df.columns = [
        "SNP ID",
        "SNP Name",
        "Gene",
        "Risk Allele",
        "Your Allele",
        "Result",
        "rs10306114",
        "Report Name",
        "Info",
        "Video",
        "Tags",
    ]

    final_combined_df = pd.concat([final_primary_df, final_secondary_df])

    return final_combined_df




def generate_covid_pdf(content, file_name, folder_name, font_size=11):
    pdf_output = BytesIO()
    
    class bookmark_flowable(Flowable):
    
        def __init__(self, name):
            super().__init__()
            self.name = name
    
        def draw(self):
            # Ensure the canvas has a custom attribute for bookmarks
            if not hasattr(self.canv, 'bookmarks'):
                self.canv.bookmarks = {}  # Initialize an empty dictionary for bookmarks
    
            # Check if bookmark already exists on the current canvas
            if self.name not in self.canv.bookmarks:
                page_number = self.canv.getPageNumber()  # Get current page number
                # Save the bookmark information along with the page number
                self.canv.bookmarks[self.name] = page_number


    class HeaderFooterCanvas(canvas.Canvas):
        def __init__(self, *args, **kwargs):
            canvas.Canvas.__init__(self, *args, **kwargs)
            self.pages = []

        def showPage(self):
            self.pages.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            page_count = len(self.pages)
            for page in self.pages:
                self.__dict__.update(page)
                self.draw_header_footer(page_count)
                canvas.Canvas.showPage(self)
            canvas.Canvas.save(self)

        def draw_header_footer(self, page_count):
            page = f"{self._pageNumber}/{page_count}"

            for key, page_num in self.bookmarks.items():
                if page_num == self._pageNumber:
                    
                    self.bookmarkPage(key)
                    self.addOutlineEntry(key, key)
            
            page_width, page_height = letter

            # Header
            right_margin = 50
            top_margin = 710
            try:
                self.drawImage(
                    "report_logo.png",
                    right_margin,
                    top_margin,
                    width=2 * inch,
                    height=1 * inch,
                    preserveAspectRatio=True,
                )
            except:
                self.rect(right_margin, top_margin, 1 * inch, 1 * inch)
                self.setFont("Times-Roman", 8)
                self.drawString(55, top_margin + 20, "Logo")

            self.setFont("Times-Roman", 16)
            self.setFillColor(colors.black)
            self.drawRightString(550, top_margin + 35, file_name)

            self.setFont("Times-Roman", 12)
            self.setFillColor(colors.gray)
            self.drawRightString(550, top_margin + 20, folder_name)

            self.setStrokeColor(colors.black)
            self.line(50, 720, page_width - 50, 720)

            # Footer
            footer_text_y_position = 40
            self.setFont("Times-Roman", 6)
            self.setFillColor(colors.black)

            footer_text = (
                "This report is intended to translate your results into an easier to understand form. It is not intended to diagnose or treat. For diagnosis or treatment, please present this to your doctor (or find a doctor on MTHFRSupport™ website under 'Find a Practitioner'). Additionally, genetic mutations are flags that something **could** be wrong and not a guarantee that you are having all or any of the associated issues. Other factors like environment, ethnic background, diet, age, personal history, etc all have a factor in whether a mutation starts to present itself or not and when. Copyright all rights reserved MTHFR Support™"
            )

            footer_style = ParagraphStyle(
                "footer_style",
                fontSize=6,
                fontName="Times-Roman",
                alignment=0,
            )
            footer_paragraph = Paragraph(footer_text, footer_style)
            footer_paragraph.wrapOn(self, 400, 20)
            footer_paragraph.drawOn(self, 50, footer_text_y_position)

            self.setFont("Times-Roman", 10)
            self.drawRightString(550, footer_text_y_position + 40, page)

    margin = 50
    doc = SimpleDocTemplate(
        pdf_output,
        pagesize=letter,
        rightMargin=margin,
        leftMargin=margin,
        topMargin=90,
        bottomMargin=120,
    )
    styles = getSampleStyleSheet()

    story = []
    header_style = styles["Heading1"]
    header_style.alignment = TA_CENTER
    header_style.fontName = "Times-Bold"
    header_style.fontSize = 22

    image = Image("report_logo.png", width=240, height=80)
    image.hAlign = "CENTER"

    # Create header
    header = Paragraph("MTHFR Support & Nutrigenomics Wellness", header_style)

    second_header = Paragraph("COVID-19 Genes and SNPs", header_style)
    second_image = Image(
        "gene.png", width=400, height=100
    )
    # Load and center image

    second_header_style = styles["Heading2"]
    second_header_style.fontName = "Times-Bold"
    second_header_style.fontSize = 14
    second_header_style.alignment = TA_LEFT
    intro_header = Paragraph("Introduction", second_header_style)

    paragraph_style = ParagraphStyle(
        name="CustomParagraph",
        fontName="Times-Roman",
        fontSize=14,
        alignment=TA_LEFT,
        leading=22,
    )

    intro_content = """What follows is a collection of genes and SNPs that we have found to be relevant
                                to the current Coronavirus epidemic, COVID-19 (aka SARS-CoV-2), and their
                                implications. This app was created by Sterling Hill of MTHFR Support in
                                conjunction with Cynthia Smith of Nutrigenomics Wellness. <br/><br/>
                                In addition to primary SNPs we have also included some secondary gene SNPs
                                that are related to a downstream cytokine storm that may occur in some folks. The
                                secondary genes may give further insight into individual impairment based on
                                your individual biochemistry to sense COVID-19 virus in your body and address
                                your individualized response to COVID-19. We have also selected relevant genes
                                that are associated with protection of cell wall permeability and may assist with
                                modulation of your immune system.<br/><br/>
                                All of the SNPs mentioned here can be found on our new COVID-19 report
                                available on Sterling’s App.<br/><br/>
                                It is important to note that neither this information nor the COVID-19 report
                                constitutes a medical diagnosis or advice and does not replace medical advice 
                                from your Physician. Rather, our goal is to share info that may be relevant to your
                                personal health.<br/><br/>
                                This information should not be used without the advice of a medical doctor and
                                does not replace medical advice from your physician. We understand that many
                                are concerned about COVID-19 and are working hard to help provide you with
                                information regarding your genetics.<br/><br/>
                                Any information provided herein regarding nutraceuticals should not take the
                                place of medical advice from your Physician. The CDC and Physicians have
                                advised the public to support their immune system via hand washing, etc., and
                                both macro and micronutrients during this COVID-19 outbreak.<br/><br/>
                                Like many things regarding health, genetic knowledge is one data set, that in
                                conjunctions with other data sets and lifestyle information, that can be utilized to
                                optimize your overall health. Genetics can enable you to identify individualize
                                “weak links” in your health “chain”, and then address them.<br/><br/>
                                When using genetic results as a data set, to optimize your health please consult an
                                experienced Practitioner. You may find one near you on our <a href="https://www.mthfrsupport.org/find-a-practitioner" color="blue">Find a Practitioner</a> map.<br/><br/>
                                Here at MTHFR Support we are doing our best to provide you with the most up
                                to date information as you have requested.<br/><br/>"""
    paragraph = Paragraph(intro_content, paragraph_style)

    covid_19 = Paragraph("COVID-19", second_header_style)
    covid_19_content = """NOTE: COVID-19 and SARS-CoV-2 terms are interchangeable.<br/><br/>
                        Some of the research I have cited pertains to original SAR outbreak in 2002-2003
                        (called SARS-CoV), but some of the same principles apply to the immune system
                        domino effect upon SARS-CoV-2 first docking with ACE2 receptors.<br/><br/>
                        COVID-19/SARS-CoV-2 in 2020 is more easily transmitted than SARS-CoV
                        from 2002-2003, but SARS-like impacts with SARS-CoV-2 are lesser.
                        Having said that however, a new FURIN cleavage system in SARS-CoV-2 has
                        made this strain more transmittable. The FURIN cleavage system was not present
                        in coronavirus in original SARS-CoV 2002-2003 version.<br/><br/>
                        I have attempted to list the enzymes/receptor proteins below in the sequential
                        order in which they are impacted, subsequent to the docking of the COVID-19
                        virus onto ACE2 receptors. In some cases however, the enzymes/receptor
                        proteins are working in parallel with the immune system.<br/><br/>
                        Here is a simplified summary of the sequence of events:<br/>
                        Following docking of SARS-CoV-2 onto <b>ACE2</b> receptors (mostly in lungs and
                        GI), and virus-cell membrane fusion via <b>TMPRSS2</b> and <b>FURIN</b>, a cascade of
                        enzymatic steps and subsequent immune system mobilization occurs. Once
                        infected, GI/lung cells are hijacked into making more viruses. The immune
                        system reacts by stepping up its response. This response includes a robust
                        elevation of a pro-inflammatory cytokines including IL-1b, early in the infection
                        process. As described below, <b>NLRP3</b> inflammasomes, <b>CASP1</b>, <b>PYCARD</b>, and
                        <b>HMGB1</b>, play prominent roles in this process.<br/><br/>
                        SARS-CoV-2 infects alveolar endothelial cells (see, ACE2 below) and/or
                        macrophages. Subsequently, the immune system mobilizes a response including
                        generation of various pro-inflammatory cytokines (e.g., IL-1, IL-6, TNF, and
                        IFN-γ).<br/>
                        In some, this immune system mobilization is “overexpressed”, and can result in a
                        severe and highly lethal respiratory disease. This severe respiratory disease is
                        characterized by a prominent pro-inflammatory response (cytokine storm), and is
                        referred to a bilateral pneumonia.<br/>
                        It should be noted that pro-inflammatory cytokines are double-edged swords that
                        not only mobilize human immune system defense but can also drive pathologic
                        inflammation, and therefor can play both anti-viral and pro-viral roles during a
                        SARS-CoV-2 infection.<br/>
                        Postmortem data from fatal cases of the 2002-2003 SARS-CoV outbreak showed 
                        diffuse alveolar damage including collapse and fibrous tissue in alveolar spaces,
                        significant monocyte–macrophage infiltration, and elevated serum cytokines.
                        <a href="https://ajp.amjpathol.org/article/S0002-9440(10)61329-6/fulltext" color="blue">https://ajp.amjpathol.org/article/S0002-9440(10)61329-6/fulltext</a><br/>
                        It was interesting to note that during the 2002-2003 SARS-CoV, AIDS patients
                        with deficient immune system were somewhat resistant to SARS infection,
                        raising a possibility that an excessive immune response is attributable to the
                        lethality of patients who die of SARS. Because death due to SARS may be the
                        result of an overactive immune system response, scientists speculate that HIV
                        patients’ weakened immune systems may put them at a lower risk of developing
                        the disease.<br/>
                        <a href="https://kffhealthnews.org/morning-breakout/dr00017448/" color="blue">https://kffhealthnews.org/morning-breakout/dr00017448/</a><br/>
                        <a href="https://www.amfar.org/Will-HIV-Drugs-Help-Fight-Coronavirus/" color="blue">https://www.amfar.org/Will-HIV-Drugs-Help-Fight-Coronavirus/</a>"""
    covid_19_paragraph = Paragraph(covid_19_content, paragraph_style)
    # Add content to document
    intro_bookmark = bookmark_flowable('Foreword')

    story = [
        intro_bookmark,
        image,
        Spacer(1, 20),
        header,
        Spacer(1, 20),
        second_image,
        Spacer(1, 20),
        second_header,
        Spacer(1, 20),
        intro_header,
        paragraph,
        Spacer(1, 20),
        covid_19,
        covid_19_paragraph,
    ]

    story.append(PageBreak())

    grouped = content.groupby("rs10306114")
    styles = getSampleStyleSheet()
    text_style = ParagraphStyle(
        "tablecellStyle",
        parent=styles["Normal"],
        fontSize=font_size,
        fontName="Times-Roman",
        alignment=1,
    )

    page_width, page_height = letter
    left_margin = 50
    right_margin = 50
    available_table_width = page_width - left_margin - right_margin
    col_widths_proportion = [90, 120, 90, 90, 90]
    total_proportion = sum(col_widths_proportion)
    col_widths = [
        available_table_width * (w / total_proportion) for w in col_widths_proportion
    ]

    tables = []
    for condition, group in grouped:
        table_data = [
            [f"{condition}"],
            ["SNP ID", "SNP Name", "Risk Allele", "Your Allele", "Result"],
        ]

        for _, row in group.iterrows():
            table_data.append(
                [
                    Paragraph(row["SNP ID"], text_style),
                    Paragraph(row["SNP Name"], text_style),
                    Paragraph(row["Risk Allele"], text_style),
                    Paragraph(row["Your Allele"], text_style),
                    Paragraph(row["Result"], text_style),
                ]
            )

        table = Table(table_data, colWidths=col_widths, repeatRows=2)

        style = TableStyle(
            [
                ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                ("SPAN", (0, 0), (-1, 0)),
                ("FONTNAME", (0, 0), (-1, 0), "Times-Roman"),
                ("FONTSIZE", (0, 0), (-1, 0), font_size),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("BACKGROUND", (0, 0), (-1, 0), "#1B80B6"),
                ("ALIGN", (0, 1), (-1, 1), "CENTER"),
                ("FONTNAME", (0, 1), (-1, 1), "Times-Roman"),
                ("FONTSIZE", (0, 1), (-1, 1), font_size),
                ("TEXTCOLOR", (0, 1), (-1, 1), colors.whitesmoke),
                ("BACKGROUND", (0, 1), (-1, 1), "#1B80B6"),
                ("ALIGN", (0, 2), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 2), (-1, -1), "Times-Roman"),
                ("FONTSIZE", (0, 2), (-1, -1), font_size),
                ("TEXTCOLOR", (0, 2), (-1, -1), colors.black),
                ("BACKGROUND", (0, 2), (-1, -1), colors.whitesmoke),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )

        for i in range(2, len(table_data)):
            if i % 2 == 0:
                style.add("BACKGROUND", (0, i), (-1, i), colors.whitesmoke)
            else:
                style.add("BACKGROUND", (0, i), (-1, i), colors.white)

        for i in range(2, len(table_data)):
            style.add(
                "BACKGROUND",
                (4, i),
                (4, i),
                get_result_color(
                    table_data[i][4].text
                    if isinstance(table_data[i][4], Paragraph)
                    else table_data[i][4]
                ),
            )

        table.setStyle(style)
        tables.append(table)
    genes = content["Gene"].unique()
    primary_bookmark = bookmark_flowable('Primary SNPs')
    story.append(primary_bookmark)

    story.append(tables[0])
    story.append(Spacer(1, 12))
    story.append(PageBreak())
    story.append(Paragraph("Primary SNPs", header_style))

    for gene, (header, points, studies) in primary_genes.items():
        if gene in genes:
            create_primary_snps(story, header, points, studies)
            story.append(PageBreak())

    
    secondary_bookmark = bookmark_flowable('Secondary SNPs')
    story.append(secondary_bookmark)
    story.append(tables[1])
    story.append(Spacer(1, 12))
    story.append(PageBreak())
    story.append(Paragraph("Secondary SNPs", header_style))
    for gene, (header, paragraphs) in secondary_genes.items():
        if gene in genes:
            story = create_secondary_snps(story, header, paragraphs)
            story.append(PageBreak())
    doc.build(story, canvasmaker=HeaderFooterCanvas)
    pdf_data = pdf_output.getvalue()
    pdf_output.close()
    
    return pdf_data
