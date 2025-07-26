from constants.helper import create_link, create_link_text

ace_header = "Angiotensin-converting enzyme 2 (ACE2)"
ace_points = [
    {"point": """ACE2 gene encodes the angiotensin-converting enzyme-2"""},
    {
        "point": """ACE2 acts as a cell surface receptor for Human coronavirus. Normally, the
ACE2 receptor plays an important role in regulating the body’s blood
pressure and fluid balance."""
    },
    {
        "point": """The surface expression of the ACE2 protein occurs on lung alveolar
epithelial cells and enterocytes of the small intestine. As such, ACE2 is
abundantly present in humans in the epithelia of the lung and small intestine.
The coronavirus gains entry into a cell via exploiting ACE2 and type II
transmembrane serine proteases (TMPRSS2) see below."""
    },
    {
        "point": """Basically, the coronavirus S (spike) protein of COVID-19 binds to ACE2
with high affinity."""
    },
    {
        "point": """Binding of the coronavirus S protein to ACE2 triggers a conformational
change in the S protein of the coronavirus, allowing for proteolytic digestion
by host cell proteases (TMPRSS2), thereby facilitating COVID-19 virus to
human cell membrane fusions, and subsequent inflammatory immune system
response (IL-6, and IL1B)<i>see below.</i>"""
    },
    {
        "point": """NOTE: Although ACE inhibitors and ARBs are useful drugs in the treatment
of high blood pressure, CAD and diabetes, (used to reduce blood pressure,
decrease risk of progressive kidney disease, and decrease risk of dying if one
is at high cardiovascular risk), there are ongoing questions as to whether
taking ACE inhibitors or ARBs increase or decrease ones susceptibility to
the more severe symptoms of COVID-19."""
    },
    {
        "point": """A March 2020 article in the Lancet, entitled, Are patients with hypertension
and diabetes mellitus at increased risk for COVID-19 infection?, suggested
that because the expression of ACE2 is substantially increased in patients
with diabetes, heart disease, etc., who are treated with ACE inhibitors and
angiotensin II type-I receptor blockers (ARBs),<i> “…they are at higher risk for
severe COVID-19 infection and, therefore, should be monitored for ACE2-
modulating medications, such as ACE inhibitors or ARBs”</i>"""
    },
    {"point": """ACE2 has binding sites for Zinc and Chloride"""},
]
ace_studies = [
    create_link(url="http://www.nephjc.com/news/covidace2"),
    create_link(url="https://onlinelibrary.wiley.com/doi/full/10.1002/path.1570"),
    create_link(
        url="https://www.thelancet.com/pdfs/journals/lanres/PIIS2213-2600(20)30116-8.pdf"
    ),
]

furin_header = "Furin (FURIN)"
furin_points = [
    {
        "point": """Furin is an enzyme encoded by the FURIN gene. Furin is a proprotein
convertase and acts to cleave sections of inactive proteins, in order to
activate them. The Furin enzyme is highly expressed in lungs.""",
        "subpoint": [
            """NOTE: Proprotein convertases are a family of nine serine secretory
proteases proteins that activate other proteins. Many proteins are
inactive when they are first synthesized, because they contain chains of
amino acids that block their activity. Proprotein convertases remove
those chains and activate the protein.""",
            """The proprotein convertase family is responsible for the activation of a
wide variety of precursor proteins, such as growth factors, hormones,
receptors and adhesion molecules, as well as cell surface glycoproteins
of infectious viruses""",
        ],
    },
    {
        "point": """In addition to processing cellular precursor proteins, Furin is also utilized by
a number of pathogens. For example, the envelope proteins of viruses
influenza, HIV, SARS-CoV-2 and several filoviruses including Ebola
Marburg virus must be cleaved by furin or furin-like proteases to become
fully functional and active."""
    },
    {
        "point": """As previously discussed, the spikes “crowning” the SARS-CoV-2 must
attach (AGT2), fuse (TMPRSS2) and gain entry to cells."""
    },
    {
        "point": """David Veesler, senior author of the report referenced below and assistant
professor of biochemistry at the UW School of Medicine, said that <i>“The
spike is the business part as far as viral entry. It is in charge not only of
attachment at the host cell surface, but also of fusing the viral and host cell
membranes to allow the infection to start.”</i>"""
    },
    {
        "point": """He goes on to say that, <i>“…unlike SARS-CoV, SARS-CoV-2 includes a furin cleavage site at a boundary between two subunits of the spike protein. It is
not yet known if this difference is expanding the kinds of cells the SARSCoV-2 could infect or enhancing its transmissibility, in a way that might be
similar to that of highly pathogenic avian flu viruses.”</i>"""
    },
    {
        "point": create_link(
            url="https://newsroom.uw.edu/news-releases/covid-19-coronavirus-spike-holds-infectivity-details"
        )
    },
    {
        "point": """Thus, when SARS-CoV-2 attaches to ACE2 cell surface receptors in the
respiratory tract, it may then successfully exploit this Furin enzyme to
activate its own surface glycoprotein to gain entry to respiratory tract cells.
This makes SARS-CoV-2 a very easily transmittable virus. This was not the
case with 2002-2003 SARS-CoV."""
    },
    {"point": """Binds 3 calcium ions per subunit"""},
    {"point": """Optimum pH is 6.0"""},
]

furin_studies = [
    create_link(
        url="https://www.sciencedirect.com/science/article/pii/S0166354220300528"
    ),
    create_link(url="https://en.wikipedia.org/wiki/Furin"),
]

hmgb1_header = "High mobility group protein B1 (HMGB1)"
hmgb1_points = [
    {
        "point": """HMGB1 is a multifunctional redox sensitive protein with various roles in
different cellular compartments."""
    },
    {
        "point": """HMGB1 is also released passively by necrotic cells, and actively by
macrophages/monocytes in response to exogenous and endogenous
inflammatory stimuli."""
    },
    {
        "point": """It activates macrophages/monocytes to express proinflammatory cytokines,
chemokines, and adhesion molecules."""
    },
    {
        "point": """A caspase activation-dependent cytokines, regulated by the release of
inflammasomes (NLRP3, see above)""",
        "subpoint": [
            "Activation of the NLRP3 inflammasome is required for HMGB1 secretion."
        ],
    },
    {
        "point": """The active cytokines and HMGB1 stimulate inflammatory responses.
Inflammasomes can also induce pyroptosis, an inflammatory form of
programmed cell death."""
    },
]
hmgb1_studies = [
    create_link(url="https://www.uniprot.org/citations/22801494"),
    create_link(url="https://www.ncbi.nlm.nih.gov/pubmed/22801494"),
]


il6_header = "Interleukin-6 receptor subunit alpha (IL-6)"
il6_points = [
    {
        "point": """Interleukin 6 is encoded by the IL6 gene
IL6 is a pleotropic cytokine produced in response to tissue damage and/or
infections."""
    },
    {
        "point": """IL6 IL-6 stimulates the inflammatory and auto-immune processes in many
diseases"""
    },
    {
        "point": """IL-6 is a cytokine with a wide variety of biological functions. It is a potent
inducer of the acute phase response. It plays an essential role in the final
differentiation of B-cells into Ig-secreting cells Involved in lymphocyte and
monocyte differentiation. It acts on B-cells, T-cells, hepatocytes,
hematopoietic progenitor cells and cells of the CNS. It is required for the
generation of T(H)17 cells. In some cases, it also acts as an antiinflammatory myokine. It is discharged into the bloodstream after muscle
contraction and acts to increase the breakdown of fats and to improve insulin
resistance. It induces myeloma and plasmacytoma growth and induces nerve
cells differentiation."""
    },
    {
        "point": """It is worth noting that,<i> “While several studies show the essential role of IL-6
to mount a proper immune response during some viral infections, others link
this cytokine with exacerbation of viral disease. These latter findings lend
support to the hypothesis that up-regulation of IL-6 during certain viral
infections may promote virus survival and/or exacerbation of clinical
disease.”</i>"""
    },
    {
        "point": """<i>“The clinical picture of severe acute respiratory syndrome (SARS) is
characterized by an over-exuberant immune response with lung
lymphomononuclear cell infiltration and proliferation that may account for
tissue damage more than the direct effect of viral replication.”</i>"""
    },
]
il6_studies = [
    create_link(url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6524401/"),
    create_link(
        url="https://www.sciencedirect.com/science/article/pii/S0168170207000470"
    ),
    create_link(
        url="https://www.frontiersin.org/articles/10.3389/fmicb.2019.01057/full"
    ),
]


nlr_header = """NACHT, LRR and PYD domains-containing protein 3 (NLRP3 aka
CIAS1, Cryopyrin, NALP3, and Pypaf1)"""
nlr_points = [
    {"point": "NLRP3 is a protein encoded by the NLRP3 gene."},
    {
        "point": "As the sensor component of the NLRP3 inflammasome, NLRP3 plays a crucial role in innate immunity (first line of immune defense against non-self pathogens such as SARS-CoV-2), and inflammation."
    },
    {
        "point": "NLRP3 regulates the secretion of pro-inflammatory cytokines interleukin 1 beta (IL-1β) and IL-18."
    },
    {
        "point": """In response to pathogens and other damage-associated signals, NLRP3
initiates the formation of the inflammasome polymeric complex, made of
NLRP3, PYCARD see, below and CASP1, see below.""",
        "subpoint": [
            """Recruitment of proCASP1 to the inflammasome promotes its activation,
and CASP1-catalyzed IL1B and IL18 maturation and secretion in the
extracellular milieu."""
        ],
    },
    {
        "point": """NLRP3 activation stimuli include extracellular ATP, reactive oxygen
species, K+ efflux, etc., crystals of monosodium urate or cholesterol,
amyloid-beta fibers, cytosolic dsRNA, etc.""",
        "subpoint": [
            f"""NOTE: Coronaviruses are positive-sense RNA viruses that generate
double-stranded RNA (dsRNA) intermediates during replication, yet
evade detection by host innate immune sensors.
{create_link(url='https://www.pnas.org/content/pnas/early/2017/05/02/1618310114.full.pdf')}"""
        ],
    },
    {
        "point": """NLRP3 activation further occurs in the presence of cytosolic dsRNA and is
mediated by ATP-dependent RNA helicase (aka DHX33)""",
        "subpoint": [
            """DHX33 Independently of inflammasome activation, regulates the
differentiation of T helper 2 (Th2) cells.""",
            create_link(url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6678949/"),
            create_link(url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7025476/"),
        ],
    },
    {
        "point": """<i>“…melatonin has been evidenced to significantly inhibit airway
inflammation, and suppress TLR3/4-mediated inflammation in liver injury.
Most notably, NLRP3 is a novel molecular target for melatonin in murine
model of septic response, liver injury and acute lung injury…”</i>"""
    },
    {
        "point": """Melatonin exhibits immunomodulatory properties.""",
        "subpoint": [
            create_link(url="https://www.ncbi.nlm.nih.gov/pubmed/24720799"),
            create_link(url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4163918/"),
            create_link(url="https://www.ncbi.nlm.nih.gov/pubmed/15582288"),
        ],
    },
    {
        "point": """There is evidence that melatonin levels are disrupted (decreased) by
electromagnetic fields such as those associated with high frequency
electromagnetic fields (EMFs), particularly those associated with 4G and 5G
technology.""",
        "subpoint": [
            """Melatonin is a natural hormone produced by pineal gland activity in the
brain that regulates the body’s sleep-wake cycle.""",
            """The pineal gland is likely to sense EMFs as light but, as a consequence,
may decrease the melatonin production.""",
            """High melatonin folks include children and women in 3rd trimester of
pregnancy. Elders have lower melatonin levels.""",
        ],
        "nestpoint": [
            """Melatonin peaks in early childhood (130 pg/ml)""",
            """Melatonin begins slow decline at puberty""",
            "20 yrs old — 80 pg/ml",
            "40 yrs old — 35 pg/ml",
            "50 yrs old — 20 pg/ml",
            "60 yrs old — 5 pg/ml",
            "70 yrs old – negligible",
        ],
    },
]
nlr_studies = [
    create_link(url="https://www.ncbi.nlm.nih.gov/pubmed/23051584"),
    create_link(
        url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1855314/#!po=9.61538"
    ),
]


pycard_header = (
    "Apoptosis-associated speck-like protein containing a CARD(PYCARD aka ASC)"
)
pycard_points = [
    {
        "point": """PYCARD is a protein that functions as key mediator in apoptosis
(programmed cell death) and inflammation."""
    },
    {
        "point": """The PYCARD protein is involved in macrophage pyroptosis, (a caspase-1-
dependent inflammatory form of cell death) and is the major constituent of
the ASC pyroptosome which forms upon potassium depletion and rapidly
recruits and activates caspase-1.""",
        "subpoint": [
            """NOTE: ASC can be either apoptosis-associated speck protein containing
a CAR, or Caspase activation and recruitment domain).""",
            """NOTE: Pyroptosis is highly inflammatory form of programmed cell
death that occurs most frequently upon infection with intracellular
pathogens.""",
            """NOTE: Pyroptosis pyroptosis requires the function of the enzyme
Caspase-1""",
        ],
    },
    {
        "point": """In innate immune response (first line of immuhne defense against non-self
pathogen such as SARS-CoV-2), the PYCARD protein is believed to act as
an integral adapter in the assembly of inflammasome which activates
caspase-1, thereby leading to processing and secretion of pro-inflammatory
cytokines."""
    },
]
pycard_studies = [
    create_link(url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4400844/")
]

cas_header = "Caspase-1 (CASP1)"
cas_points = [
    {"point": """CASP1 gene encodes the protease (enzyme) caspase-1"""},
    {
        "point": """CASP1 is an organosulfur-based protease that cleaves Interleukin-1 beta,
thereby releasing the mature cytokines which are involved in a variety of
inflammatory processes. Important for defense against pathogens."""
    },
    {
        "point": """Upon inflammasome activation, during DNA virus infection but not RNA
virus challenge, CASP1 controls antiviral immunity through the cleavage of
Cyclic GMP-AMP synthase, rendering it inactive.""",
        "subpoint": [
            """NOTE: Cyclic GMP-AMP synthase is a component of the innate
immune system which detects the presence of cystolic DNA and, in
response, trigger expression of inflammatory genes that can lead to cell
death or to the activation of defense mechanisms.""",
            """DNA is normally only found in the nucleus of the cell.""",
            """Localization of DNA to the cytosol is associated with tumorigenesis, a
viral infection or an invasion by some intracellular bacteria. The cGAS –
STING pathway, including Cyclic GMP-AMP synthase, acts to detect
cytosolic DNA and induce an immune response.""",
        ],
    },
]
cas_studies = [create_link(url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4163918/")]

ilb_header = "Interleukin-1 beta (IL1B aka IL-1β)"
ilb_points = [
    {
        "point": """Interleukin-1 beta is a cytokine protein that is encoded by the IL1B gene"""
    },
    {
        "point": """As a caspase activation-dependent cytokine, regulated by the release of
inflammasomes (NLRP3, <i>see above</i>)"""
    },
    {
        "point": """IL1B is Potent proinflammatory cytokine, and induces prostaglandin
synthesis, neutrophil influx and activation, T-cell activation and cytokine
production, B-cell activation and antibody production, and fibroblast
proliferation and collagen production."""
    },
    {
        "point": """The IL1B production occurs in 2 steps, each being controlled by different
stimuli.""",
        "subpoint": [
            """First, inflammatory signals, such as LPS, stimulate the synthesis and
promote the accumulation of cytosolic stores of pro-IL1B (priming).""",
            """Second, additional signals are required for inflammasome assembly,
leading to CASP1 activation, pro-IL1B processing and eventually
secretion of the active cytokine. IL1B processing and secretion are
temporarily associated.""",
        ],
    },
    {
        "point": """NOTE: Blocking the activity of IL-1 beta has entered the clinical arena of
treating autoimmune diseases""",
        "subpoint": [create_link(url="https://www.ncbi.nlm.nih.gov/pubmed/15192144")],
    },
]
ilb_studies = [
    create_link(url="https://www.uniprot.org/citations/22801494"),
    create_link(url="https://www.ncbi.nlm.nih.gov/pubmed/22801494"),
]

n_oxide_header = (
    "Nitric oxide synthase 3 [endothelial] (NOS3 aka eNOS, Constitutive NOS)"
)
n_oxide_points = [
    {
        "point": """There are three types of NOS; NOS1 (Nitric oxide synthase 1, neuronal),
NOS2 (Nitric oxide synthase, inducible; aka iNOS), NOS3 (Nitric oxide
synthase, endothelial; aka eNOS)""",
        "subpoint": [
            """NOS2 enhances the synthesis of pro-inflammatory mediators such as
IL6 and IL8"""
        ],
    },
    {
        "point": """NOS3 produces nitric oxide (NO) that is implicated in vascular smooth
muscle relaxation through a cGMP-mediated signal transduction pathway.
NO mediates vascular endothelial growth factor (VEGF)-induced
angiogenesis in coronary vessels and promotes blood clotting through the
activation of platelets."""
    },
    {
        "point": """eNOS is primarily responsible for the generation of NO in the vascular
endothelium, a monolayer of flat cells lining the interior surface of blood
vessels, at the interface between circulating blood in the lumen and the
remainder of the vessel wall. NO produced by eNOS in the vascular
endothelium plays crucial roles in regulating vascular tone, cellular
proliferation, leukocyte adhesion, and platelet aggregation. Therefore, a
functional eNOS is essential for a healthy cardiovascular system."""
    },
    {
        "point": "Catalytic activity:",
        "subpoint": [
            "2 L-arginine + 3 NADPH + 4 O2 = 2 L-citrulline + 2 nitric oxide + 3NADP+ + 4 H2O"
        ],
    },
    {"point": "Cofactors: Heme, FAD, FMN, 5,6,7,8-tetrahydrobiopterin"},
    {
        "point": """Encouraging Nitric Oxide production inhibits the replication cycle of Severe Acute Respiratory symptoms of SARS-CoV-2 <br/><i> “Our results demonstrated that NO specifically inhibits the replication cycle of
SARS CoV, most probably during the early steps of infection.”</i>""",
        "subpoint": [create_link(url="https://jvi.asm.org/content/79/3/1966")],
    },
]
n_oxide_studies = [
    create_link(url="https://www.ncbi.nlm.nih.gov/pubmed/16416260"),
    create_link(url="https://www.ncbi.nlm.nih.gov/pubmed/12379270"),
    create_link(url="https://www.ncbi.nlm.nih.gov/pubmed/16585403"),
]

ifnari_header = "Interferon-alpha/beta receptor 1 (IFNAR1)"
ifnari_points = [
    {
        "point": """Interferon-alpha/beta receptor 1 alpha chain is a protein that in humans is
encoded by the IFNAR1 gene."""
    },
    {
        "point": """IFNAR1 is a type of interferon that helps regulate the immune system."""
    },
    {
        "point": """All type 1 interferons bind to IFN-α receptors that consist of IFNAR1 and IFNAR2 chains."""
    },
    {
        "point": """IFNAR1 is a component of the receptor for type I interferons.""",
        "subpoint": [
            create_link_text(
                url="https://pubmed.ncbi.nlm.nih.gov/2153461/",
                text="""Genetic transfer of a functional human interferon alpha receptor into
mouse cells: cloning and expression of its cDNA""",
            ),
            create_link_text(
                url="https://pubmed.ncbi.nlm.nih.gov/10049744/",
                text="""Formation of a uniquely stable type I interferon receptor complex by
interferon beta is dependent upon particular interactions between
interferon beta and its receptor and independent of tyrosine
phosphorylation""",
            ),
            create_link_text(
                url="https://pubmed.ncbi.nlm.nih.gov/21854986/",
                text="""Structural linkage between ligand discrimination and receptor activation
by type I interferons""",
            ),
        ],
    },
    {
        "point": """A B cell auto-immune phenocopy of inborn errors of type I IFN immunity
underlies life-threatening COVID-19 pneumonia in at least 2.6% of women
and 12.5% of men.""",
        "subpoint": [
            create_link_text(
                url="https://www.science.org/doi/10.1126/science.abd4585",
                text="""
Auto-antibodies against type I IFNs in patients with life-threatening
COVID-19""",
            )
        ],
    },
]
ifnari_studies = []


ifh1_header = "IFIH1 (HLA)"
ifh1_points = [
    {
        "point": """innate immune receptor which acts as a cytoplasmic sensor of viral nucleic
acids and plays a major role in sensing viral infection and in the activation of
a cascade of antiviral responses including the induction of type I interferons
and proinflammatory cytokines.""",
        "subpoint": [
            """<a href="https://www.uniprot.org/uniprotkb/Q9BYX4" color="blue"><u>IFIH1 – Interferon-induced helicase C domain-containing protein</u></a>"""
        ],
    },
    {
        "point": """The severe acute respiratory syndrome coronavirus-2 (SARS-CoV-2) is
responsible for the current COVID-19 pandemic. An unbalanced immune
response, characterized by a weak production of type I interferons (IFN-Is)
and an exacerbated release of proinflammatory cytokines, contributes to the
severe forms of the disease""",
        "subpoint": [
            '<a href="https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1008737" color="blue"><u>Interplay between SARS-CoV-2 and the type I interferon response</u></a>'
        ],
    },
    {
        "point": "Further Resources",
        "subpoint": [
            """Analyses suggest that African-Americans and Chinese with low Tmaf of
rs1990760 are more vulnerable to SARS-COV2 infection, apart from
other genetic factors or socioeconomic conditions in these population.
Taken together, an IFN-beta supplement might aid in preventing
COVID-19 infection and help in development of herd immunity –
<a href='https://pubmed.ncbi.nlm.nih.gov/32737579/' color="blue"><u>PubMed</u></a>"""
        ],
    },
]
