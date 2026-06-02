DRUG_RULES = {
    "CODEINE": {
        "gene": "CYP2D6",
        "rules": {
            "PM": ("Ineffective", "moderate", 0.95),
            "IM": ("Adjust Dosage", "low", 0.85),
            "NM": ("Safe", "none", 0.90),
            "URM": ("Toxic", "high", 0.95)
        }
    },

    "WARFARIN": {
        "gene": "CYP2C9",
        "rules": {
            "PM": ("Toxic", "high", 0.95),
            "IM": ("Adjust Dosage", "moderate", 0.85),
            "NM": ("Safe", "none", 0.90)
        }
    },

    "CLOPIDOGREL": {
        "gene": "CYP2C19",
        "rules": {
            "PM": ("Ineffective", "high", 0.95),
            "IM": ("Adjust Dosage", "moderate", 0.85),
            "NM": ("Safe", "none", 0.90)
        }
    },

    "SIMVASTATIN": {
        "gene": "SLCO1B1",
        "rules": {
            "PM": ("Toxic", "high", 0.95),
            "IM": ("Adjust Dosage", "moderate", 0.85),
            "NM": ("Safe", "none", 0.90)
        }
    },

    "AZATHIOPRINE": {
        "gene": "TPMT",
        "rules": {
            "PM": ("Toxic", "critical", 0.99),
            "IM": ("Adjust Dosage", "high", 0.90),
            "NM": ("Safe", "none", 0.90)
        }
    },

    "FLUOROURACIL": {
        "gene": "DPYD",
        "rules": {
            "PM": ("Toxic", "critical", 0.99),
            "IM": ("Adjust Dosage", "high", 0.90),
            "NM": ("Safe", "none", 0.90)
        }
    }
}


def evaluate_drug_risk(drug, phenotypes):
    drug = drug.upper()

    if drug not in DRUG_RULES:
        return "Unknown", "low", 0.50, None

    gene = DRUG_RULES[drug]["gene"]
    phenotype = phenotypes.get(gene, "Unknown")

    if phenotype in DRUG_RULES[drug]["rules"]:
        risk_label, severity, confidence = DRUG_RULES[drug]["rules"][phenotype]
        return risk_label, severity, confidence, gene

    return "Unknown", "low", 0.50, gene
