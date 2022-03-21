import sys

sys.path.append("/mnt/storage/apps/software/dias_config")

from dias_dynamic_files import (
    nirvana_genes2transcripts,
    bioinformatic_manifest,
    genepanels_file,
)

assay_name = "CEN" # Core Endo Neuro
assay_version = "v1.0.3"

ref_project_id = "project-Fkb6Gkj433GVVvj73J7x8KbV"

# Single workflow

ss_workflow_id = "{}:workflow-G5gzKx8433GYp8x7FkjV1J2j".format(ref_project_id)

sentieon_stage_id = "stage-Fy6fpk040vZZPPbq96Jb2KfK"

sentieon_R1_input_stage = "{}.reads_fastqgzs".format(sentieon_stage_id)
sentieon_R2_input_stage = "{}.reads2_fastqgzs".format(sentieon_stage_id)
sentieon_sample_input_stage = "{}.sample".format(sentieon_stage_id)
fastqc_fastqs_input_stage = "stage-Fy6fpV840vZZ0v6J8qBQYqZF.fastqs"
ss_beds_inputs = {
    # vcf_qc
    "stage-Fy6fqy040vZV3Gj24vppvJgZ.bed_file ID": "file-Fpz2X0Q433GVK5xxPvzqvVPB",
    "stage-Fy6fqy040vZV3Gj24vppvJgZ.bed_file": "",
    # region coverage
    "stage-G21GzGj433Gky42j42Q5bJkf.input_bed ID": "file-Fpz2X0Q433GVK5xxPvzqvVPB",
    "stage-G21GzGj433Gky42j42Q5bJkf.input_bed": "",
    # mosdepth
    "stage-Fy6fvYQ40vZV1y8p9GYKPYyQ.bed ID": "file-Fpz2X0Q433GVK5xxPvzqvVPB",
    "stage-Fy6fvYQ40vZV1y8p9GYKPYyQ.bed": "",
    # picard
    "stage-Fy6fx2Q40vZbFVxZ283xXGVY.bedfile ID": "file-G5jjzG0433GgkQ093K2p8PxQ",  # CEN Capture Bed
    "stage-Fy6fx2Q40vZbFVxZ283xXGVY.bedfile": ""
}


# Multi workflow

happy_stage_id = "stage-Fq1BPKj433Gx3K4Y8J35j0fv"

happy_stage_prefix = "{}.prefix".format(happy_stage_id)
happy_stage_bed = {
    "{}.panel_bed ID".format(happy_stage_id): "file-G620390433GYGY34Jq6Zq1Xf",
    "{}.panel_bed".format(happy_stage_id): "file-G620390433GYGY34Jq6Zq1Xf"
}

female_threshold = 3
male_threshold = 1

somalier_relate_stage_id = "stage-G5j1jJj433GpFY3v0JZQ2ZZ0"

multi_stage_input_dict = {
    "stage-Fybykxj433GV7vJKFGf3yVkK.SampleSheet": {
        "app": None, "subdir": "", "pattern": "SampleSheet.csv$",
    },
    "{}.query_vcf".format(happy_stage_id): {
        "app": "sentieon-dnaseq", "subdir": "",
        "pattern": "^NA12878-.*-EGG5_markdup_recalibrated_Haplotyper.vcf.gz$",
    },
    "{}.somalier_extract_file".format(somalier_relate_stage_id): {
        "app": "somalier_extract", "subdir": "",
        "pattern": "-E '(.*).somalier$'"
    },
}

ms_workflow_id = "{}:workflow-G5j1j28433GYkv4gPpPG8g11".format(ref_project_id)

# MultiQC

mqc_applet_id = "app-G6FyybQ4f4xqqpFfGqg34y2Y"
mqc_config_file = "{}:file-G82027Q433Gfx69zGvjq7PqQ".format(ref_project_id)

# Reports

xlsx_flanks = 95

exons_nirvana = "{}:file-Fq18Yp0433GjB7172630p9Yv".format(ref_project_id) 

vcf_annotator_stage_id = "stage-G72pJpj46jqgk1y3Kbb1KBxY"
generate_bed_xlsx_stage_id = "stage-G4BJkJQ4JxJvBv5vJq50vJZ8"
vcf2xls_stage_id = "stage-Fyq5ypj433GzxPK360B8Qfg5"
generate_bed_stage_id = "stage-Fyq5yy0433GXxz691bKyvjPJ"
athena_stage_id = "stage-Fyq5z18433GfYZbp3vX1KqjB"

rpt_workflow_id = "{}:workflow-G7PG1k8433GgfJ2fGPkK5J1F".format(ref_project_id)

rpt_stage_input_dict = {
    # vcf2xls
    "{}.dest_vcf".format(vcf_annotator_stage_id): {
        "app": "nirvana2vcf", "subdir": "",
        "pattern": "-E '{}(.*).annotated.vcf$'"
    },
    "{}.raw_vcf".format(vcf2xls_stage_id): {
        # pattern excludes "g" because g.vcf are in the same folder
        "app": "sentieon-dnaseq", "subdir": "",
        "pattern": "-E '{}(.*)[^g].vcf.gz$'"
    },
    "{}.sample_coverage_file".format(vcf2xls_stage_id): {
        "app": "region_coverage", "subdir": "",
        "pattern": "-E '{}(.*)5bp.gz$'",
    },
    "{}.sample_coverage_index".format(vcf2xls_stage_id): {
        "app": "region_coverage", "subdir": "",
        "pattern": "-E '{}(.*)5bp.gz.tbi$'",
    },
    "{}.flagstat_file".format(vcf2xls_stage_id): {
        "app": "flagstat", "subdir": "", "pattern": "-E '{}(.*)flagstat$'"
    },
    # generate_bed
    "{}.sample_file".format(generate_bed_stage_id): {
        "app": "mosdepth", "subdir": "",
        "pattern": "-E '{}(.*).per-base.bed.gz.csi$'"
    },
    "{}.sample_file".format(generate_bed_xlsx_stage_id): {
        "app": "mosdepth", "subdir": "",
        "pattern": "-E '{}(.*).per-base.bed.gz.csi$'"
    },
    # athena
    "{}.mosdepth_files".format(athena_stage_id): {
        "app": "mosdepth", "subdir": "",
        # athena requires both per-base files and reference files
        "pattern": "-E '{}(.*)(per-base.bed.gz$|reference)'"
    },
}

rpt_dynamic_files = {
    "{}.genepanels_file ID".format(vcf2xls_stage_id): genepanels_file,
    "{}.genepanels_file".format(vcf2xls_stage_id): "",
    "{}.bioinformatic_manifest ID".format(vcf2xls_stage_id): bioinformatic_manifest,
    "{}.bioinformatic_manifest".format(vcf2xls_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(vcf2xls_stage_id): nirvana_genes2transcripts,
    "{}.nirvana_genes2transcripts".format(vcf2xls_stage_id): "",
    "{}.exons_nirvana ID".format(generate_bed_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(generate_bed_stage_id): "",
    "{}.exons_nirvana ID".format(generate_bed_xlsx_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(generate_bed_xlsx_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_stage_id): nirvana_genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_xlsx_stage_id): nirvana_genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_xlsx_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_xlsx_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_xlsx_stage_id): "",
    "{}.manifest ID".format(generate_bed_stage_id): bioinformatic_manifest,
    "{}.manifest".format(generate_bed_stage_id): "",
    "{}.manifest ID".format(generate_bed_xlsx_stage_id): bioinformatic_manifest,
    "{}.manifest".format(generate_bed_xlsx_stage_id): "",
    "{}.exons_nirvana ID".format(athena_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(athena_stage_id): ""
}

# reanalysis

rea_stage_input_dict = {
    # vcf2xls
    "{}.dest_vcf".format(vcf_annotator_stage_id): {
        "app": "nirvana2vcf", "subdir": "",
        "pattern": "-E '{}(.*).annotated.vcf$'"
    },
    "{}.raw_vcf".format(vcf2xls_stage_id): {
        # pattern excludes "g" because g.vcf are in the same folder
        "app": "sentieon-dnaseq", "subdir": "",
        "pattern": "-E '{}(.*)[^g].vcf.gz$'"
    },
    "{}.sample_coverage_file".format(vcf2xls_stage_id): {
        "app": "region_coverage", "subdir": "",
        "pattern": "-E '{}(.*)5bp.gz$'",
    },
    "{}.sample_coverage_index".format(vcf2xls_stage_id): {
        "app": "region_coverage", "subdir": "",
        "pattern": "-E '{}(.*)5bp.gz.tbi$'",
    },
    "{}.flagstat_file".format(vcf2xls_stage_id): {
        "app": "flagstat", "subdir": "", "pattern": "-E '{}(.*)flagstat$'"
    },
    # athena
    "{}.mosdepth_files".format(athena_stage_id): {
        "app": "mosdepth", "subdir": "",
        # athena requires both per-base files and reference files
        "pattern": "-E '{}(.*)(per-base.bed.gz$|reference)'"
    },
}

rea_dynamic_files = {
    "{}.genepanels_file ID".format(vcf2xls_stage_id): genepanels_file,
    "{}.genepanels_file".format(vcf2xls_stage_id): "",
    "{}.bioinformatic_manifest ID".format(vcf2xls_stage_id): bioinformatic_manifest,
    "{}.bioinformatic_manifest".format(vcf2xls_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(vcf2xls_stage_id): nirvana_genes2transcripts,
    "{}.nirvana_genes2transcripts".format(vcf2xls_stage_id): "",
    "{}.exons_nirvana ID".format(generate_bed_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(generate_bed_stage_id): "",
    "{}.exons_nirvana ID".format(generate_bed_xlsx_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(generate_bed_xlsx_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_stage_id): nirvana_genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_xlsx_stage_id): nirvana_genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_xlsx_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_xlsx_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_xlsx_stage_id): "",
    "{}.exons_nirvana ID".format(athena_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(athena_stage_id): ""
}
