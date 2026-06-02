# debug_vcf.py
import sys
from vcf_parser import parse_vcf
from gene_rules import construct_diplotypes, get_phenotype
from drug_rules import evaluate_drug_risk

def main(vcf_path, drugs_csv="CODEINE"):
    variants = parse_vcf(vcf_path)
    if isinstance(variants, dict) and "error" in variants:
        print("VCF parse error:", variants["error"])
        return

    print("=== Parsed Variants ===")
    for v in variants:
        print(v)

    diplotypes = construct_diplotypes(variants)
    print("\n=== Diplotypes ===")
    for g, d in diplotypes.items():
        print(g, "=>", d)

    phenotypes = {}
    for gene, diplotype in diplotypes.items():
        phenotypes[gene] = get_phenotype(gene, diplotype)

    print("\n=== Phenotypes ===")
    for g, p in phenotypes.items():
        print(g, "=>", p)

    drugs = [d.strip().upper() for d in drugs_csv.split(",")]
    print("\n=== Drug Evaluations ===")
    for drug in drugs:
        risk_label, severity, confidence, gene = evaluate_drug_risk(drug, phenotypes)
        print(f"{drug} => gene:{gene} phenotype:{phenotypes.get(gene)} risk:{risk_label} severity:{severity} conf:{confidence}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python debug_vcf.py path/to/test.vcf [CODEINE,WARFARIN]")
    else:
        vcf = sys.argv[1]
        drugs = sys.argv[2] if len(sys.argv) > 2 else "CODEINE"
        main(vcf, drugs)