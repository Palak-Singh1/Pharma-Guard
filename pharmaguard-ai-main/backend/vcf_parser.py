import re

def parse_vcf(file_path):
    variants = []
    header_cols = None
    sample_col_idx = None

    try:
        with open(file_path, "r") as fh:
            for line in fh:
                line = line.strip()

                if not line:
                    continue

                if line.startswith("##"):
                    continue

                if line.startswith("#CHROM"):
                    header_cols = line.split("\t")
                    # sample column = last column
                    sample_col_idx = len(header_cols) - 1
                    continue

                if not header_cols:
                    continue

                parts = line.split("\t")

                # Ensure enough columns
                if len(parts) <= sample_col_idx:
                    continue

                try:
                    info_field = parts[7]
                    format_field = parts[8]
                    sample_field = parts[sample_col_idx]
                except IndexError:
                    continue

                # Parse INFO safely
                info = {}
                for kv in info_field.split(";"):
                    if "=" in kv:
                        k, v = kv.split("=", 1)
                        info[k] = v

                gene = info.get("GENE")
                star = info.get("STAR")
                rsid = info.get("RS")

                # Parse genotype
                format_keys = format_field.split(":")
                sample_values = sample_field.split(":")

                if "GT" not in format_keys:
                    continue

                gt_idx = format_keys.index("GT")

                if gt_idx >= len(sample_values):
                    continue

                genotype = sample_values[gt_idx].replace("|", "/")

                if genotype in (".", "./.", ".|."):
                    continue

                alleles = re.split(r"[\/]", genotype)

                allele_count = 0
                for a in alleles:
                    if a.isdigit() and int(a) > 0:
                        allele_count += 1

                if allele_count == 0:
                    continue

                variants.append({
                    "gene": gene,
                    "star": star,
                    "rsid": rsid,
                    "allele_count": allele_count
                })

        return variants

    except Exception as e:
        return {"error": str(e)}