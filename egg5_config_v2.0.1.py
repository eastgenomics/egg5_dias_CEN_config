assay_name = "CEN" # Core Endo Neuro
assay_version = "v2.0.1"

ref_project_id = "project-Fkb6Gkj433GVVvj73J7x8KbV"

### Dynamic files:

## for generate_bed
# genepanels 230602
genepanels_file = "{}:file-GVx0vkQ433Gvq63k1Kj4Y562".format(ref_project_id)
# g2t 230421
genes2transcripts = "{}:file-GV4P970433Gj6812zGVBZvB4".format(ref_project_id)
# GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0.tsv
exons_nirvana = "{}:file-GF611Z8433Gk7gZ47gypK7ZZ".format(ref_project_id)

# for generate_bed_for_VEP
vep_bed_flank = 495

## for eggd_Athena
# GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0.tsv
exons_file = "{}:file-GF611Z8433Gf99pBPbJkV7bq".format(ref_project_id)

## for eggd_VEP
# VEP config file for SNV reports v1.1.2
vep_config = "{}:file-GVgfXJ04Qg8BF8z5QK0kVjq6".format(ref_project_id)
# VEP config file for CNV reports v1.1.0
cnv_vep_config =  "{}:file-GQGJ3Z84xyx0jp1q65K1Q1jY".format(ref_project_id)

# additional regions TSV for CNV reports v1.0.1
additional_regions = "{}:file-GJZQvg0433GkyFZg13K6VV6p".format(ref_project_id)


### Apps and workflows:

# GATKgCNV_call
# v1.0.1
cnvcall_app_id = "app-GJZVB2840KK0kxX998QjgXF0"

cnvcalling_fixed_inputs = {
    # GATK Docker image tar v4.2.5.0
    "gatk_docker": "{}:file-GBBP9JQ433GxV97xBpQkzYZx".format(ref_project_id),
    # CEN intervals for CNV calling and its annotation v1.1.0
    "interval_list": "{}:file-GFPxzKj4V50pJX3F4vV58yyg".format(ref_project_id),
    "annotation_tsv": "{}:file-GFPxzPQ4V50z4pv230p82G0q".format(ref_project_id),
}

cnvcalling_input_dict = {
    "app": "sentieon-dnaseq",
    "patterns": ["-E '(.*).bam$'", "-E '(.*).bai$'"]
}


# dias_reports
# v2.0.4
rpt_workflow_id = "{}:workflow-GBQ985Q433GYJjv0379PJqqg".format(ref_project_id)

generate_bed_vep_stage_id = "stage-G9P8p104vyJJGy6y86FQBxkv"
vep_stage_id = "stage-G9Q0jzQ4vyJ3x37X4KBKXZ5v"
generate_workbook_stage_id = "stage-G9P8VQj4vyJBJ0kg50vzVPxY"
generate_bed_athena_stage_id = "stage-Fyq5yy0433GXxz691bKyvjPJ"
athena_stage_id = "stage-Fyq5z18433GfYZbp3vX1KqjB"

rpt_dynamic_files = {
    # inputs for generate bed for vep
    "{}.exons_nirvana ID".format(generate_bed_vep_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(generate_bed_vep_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_vep_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_vep_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_vep_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_vep_stage_id): "",
    # input for eggd_vep
    "{}.config_file ID".format(vep_stage_id): vep_config,
    "{}.config_file".format(vep_stage_id): "",
    # inputs for generate bed for athena
    "{}.exons_nirvana ID".format(generate_bed_athena_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(generate_bed_athena_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_athena_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_athena_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_athena_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_athena_stage_id): "",
    # inputs for athena
    "{}.exons_file ID".format(athena_stage_id): exons_file,
    "{}.exons_file".format(athena_stage_id): ""
}

# Sample-specific input files and their search patterns
rpt_stage_input_dict = {
    # eggd_vep
    "{}.vcf".format(vep_stage_id): {
        "app": "sentieon-dnaseq", "subdir": "",
        "pattern": "-E '{}(.*)[^g].vcf.gz$'"
    },
    # eggd_athena
    "{}.mosdepth_files".format(athena_stage_id): {
        "app": "mosdepth", "subdir": "",
        # athena requires both per-base files and reference files
        "pattern": "-E '{}(.*)(per-base.bed.gz$|reference)'"
    },
}


# dias_cnvreports
# v1.0.2
cnv_rpt_workflow_id =  "{}:workflow-GJk5VXQ433GbPgPY4gGY262z".format(ref_project_id)

cnv_generate_bed_excluded_stage_id = "stage-GFZQB7Q4qq8X6yjKG2pFQ58x"
cnv_annotate_excluded_regions_stage_id = "stage-GG1qYz84qq8yKzF1J2X48q62"
cnv_generate_bed_vep_stage_id = "stage-GG39Gq04qq8ZkfgV31yQy93v"
cnv_vep_stage_id = "stage-GFYvJF04qq8VKgq34j30pZZ3"
cnv_generate_workbook_stage_id = "stage-GFfYY9j4qq8ZxpFpP8zKG7G0"


cnv_rpt_dynamic_files = {
    # inputs for generate bed for vep
    "{}.exons_nirvana ID".format(cnv_generate_bed_vep_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(cnv_generate_bed_vep_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(cnv_generate_bed_vep_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(cnv_generate_bed_vep_stage_id): "",
    "{}.gene_panels ID".format(cnv_generate_bed_vep_stage_id): genepanels_file,
    "{}.gene_panels".format(cnv_generate_bed_vep_stage_id): "",
    "{}.additional_regions ID".format(cnv_generate_bed_vep_stage_id): additional_regions,
    "{}.additional_regions".format(cnv_generate_bed_vep_stage_id): "",
    # input for eggd_vep
    "{}.config_file ID".format(cnv_vep_stage_id): cnv_vep_config,
    "{}.config_file".format(cnv_vep_stage_id): "",
    # inputs for generate bed for excluded app
    "{}.exons_nirvana ID".format(cnv_generate_bed_excluded_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(cnv_generate_bed_excluded_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(cnv_generate_bed_excluded_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(cnv_generate_bed_excluded_stage_id): "",
    "{}.gene_panels ID".format(cnv_generate_bed_excluded_stage_id): genepanels_file,
    "{}.gene_panels".format(cnv_generate_bed_excluded_stage_id): "",
    "{}.additional_regions ID".format(cnv_generate_bed_excluded_stage_id): additional_regions,
    "{}.additional_regions".format(cnv_generate_bed_excluded_stage_id): "",
    # inputs for excluded app
    "{}.cds_hgnc ID".format(cnv_annotate_excluded_regions_stage_id): exons_nirvana,
    "{}.cds_hgnc".format(cnv_annotate_excluded_regions_stage_id): "",
    "{}.cds_gene ID".format(cnv_annotate_excluded_regions_stage_id): exons_file,
    "{}.cds_gene".format(cnv_annotate_excluded_regions_stage_id): "",
    "{}.additional_regions ID".format(cnv_annotate_excluded_regions_stage_id): additional_regions,
    "{}.additional_regions".format(cnv_annotate_excluded_regions_stage_id): ""
}

# Sample-specific input files and their search patterns
# subdirectories always require trailing forward slash
cnv_rpt_stage_input_dict = {
    # eggd_vep
    "{}.vcf".format(cnv_vep_stage_id): {
        "app": "eggd_GATKgCNV_call", "subdir": "CNV_vcfs/",
        "pattern": "-E '{}(.*)_segments.vcf$'"
    },
    # excluded_annotate
    "{}.excluded_regions".format(cnv_annotate_excluded_regions_stage_id): {
        "app": "eggd_GATKgCNV_call", "subdir": "CNV_summary/",
        "pattern": "-E '(.*)_excluded_intervals.bed$'"
    },
}
