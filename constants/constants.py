from constants.primary_snp_data import *
from constants.secondary_snp_data import *

gene_references = {
    'Primary' : ['ACE2', 'IFNAR1', 'IL12A-AS1', 'IL12B', 'CIITA', 'ABCG2', 'IFNG', 'B9D2','TGFB1', 'B9D2/TGFB1', 'IFNGR1', 'MRC1', 'BAHD1', 'TNF', 'FAS', 'IL6', 'NLRP3', 'FURIN', 'TMPRSS2', 'NOS3', 'PYCARD', 'CASP1', 'IL1B', 'HMGB1'],
    'Secondary': ['FUT2', 'SOD3', 'HFE', 'IFIH1', 'NOD2', 'G6PD', 'PTGS2', 'COX2', 'PTGS2/COX2'] #sec
}

# Define mappings for Primary and Secondary genes
primary_genes = {
    "ACE2": (ace_header, ace_points, ace_studies),
    "FURIN": (furin_header, furin_points, furin_studies),
    "NLRP3": (nlr_header, nlr_points, nlr_studies),
    "PYCARD": (pycard_header, pycard_points, pycard_studies),
    "CASP1": (cas_header, cas_points, cas_studies),
    "IL1B": (ilb_header, ilb_points, ilb_studies),
    "IL6": (il6_header, il6_points, il6_studies),
    "NOX": (n_oxide_header, n_oxide_points, n_oxide_studies),
    "IFIH1": (ifh1_header, ifh1_points, []),
    "IFNAR1": (ifnari_header, ifnari_points, []),
}

secondary_genes = {
    "FUT2": (fut2_header, fut2_paragraphs),
    "SOD3": (sod_header, sod_paragraphs),
    "HFE": (hema, hema_paragraphs),
    "NOD2": (nod_header, nod_paragraphs),
    "G6PD": (g6_header, g6_paragraphs),
    "PTGS2/COX2": (pt_header, pt_paragraphs),
}
