CYP2D6_RULES = {
    "*1/*1": "NM",
    "*1/*2": "NM",
    "*2/*1": "NM",
    "*2/*2": "NM",
    "*1/*4": "IM",
    "*4/*1": "IM",
    "*4/*4": "PM"
}

CYP2C19_RULES = {
    "*1/*1": "NM",
    "*1/*2": "IM",
    "*2/*1": "IM",
    "*2/*2": "PM"
}

CYP2C9_RULES = {
    "*1/*1": "NM",
    "*1/*2": "IM",
    "*2/*1": "IM",
    "*2/*2": "PM",
    "*3/*3": "PM"
}

SLCO1B1_RULES = {
    "*1/*1": "NM",
    "*1/*5": "IM",
    "*5/*5": "PM"
}

TPMT_RULES = {
    "*1/*1": "NM",
    "*1/*3A": "IM",
    "*3A/*3A": "PM"
}

DPYD_RULES = {
    "*1/*1": "NM",
    "*1/*2A": "IM",
    "*2A/*2A": "PM"
}


def get_phenotype(gene, diplotype):
    if gene == "CYP2D6":
        return CYP2D6_RULES.get(diplotype, "Unknown")

    if gene == "CYP2C19":
        return CYP2C19_RULES.get(diplotype, "Unknown")
    if gene == "CYP2C9":
        return CYP2C9_RULES.get(diplotype, "Unknown")

    if gene == "SLCO1B1":
        return SLCO1B1_RULES.get(diplotype, "Unknown")

    if gene == "TPMT":
        return TPMT_RULES.get(diplotype, "Unknown")

    if gene == "DPYD":
        return DPYD_RULES.get(diplotype, "Unknown")


    return "Unknown"


SUPPORTED_GENES = [
    "CYP2D6",
    "CYP2C19",
    "CYP2C9",
    "SLCO1B1",
    "TPMT",
    "DPYD"
]
# gene_rules.py (only snippet to replace construct_diplotypes)

SUPPORTED_GENES = [
    "CYP2D6",
    "CYP2C19",
    "CYP2C9",
    "SLCO1B1",
    "TPMT",
    "DPYD"
]

def construct_diplotypes(variants):
    """
    Build diplotypes per supported gene using allele counts.
    variants: output of parse_vcf() where each entry may appear multiple times if allele_count > 1
    Returns dict: { gene: "*1/*1" or "*1/*X" or "*X/*Y" }
    """
    gene_stars = {}

    for v in variants:
        gene = v.get("gene")
        star = v.get("star")
        count = v.get("allele_count", 1)

        if not gene:
            continue

        if gene not in gene_stars:
            gene_stars[gene] = []

        # if STAR is missing (None) we skip adding; later we'll assign *1
        if star:
            for _ in range(count):
                gene_stars[gene].append(star)

    diplotypes = {}
    for gene in SUPPORTED_GENES:
        stars = gene_stars.get(gene, [])
        if len(stars) == 0:
            diplotypes[gene] = "*1/*1"
        elif len(stars) == 1:
            diplotypes[gene] = f"*1/{stars[0]}"
        else:
            # if more than 2 alleles present, take first two (simplification)
            diplotypes[gene] = f"{stars[0]}/{stars[1]}"

    return diplotypes


