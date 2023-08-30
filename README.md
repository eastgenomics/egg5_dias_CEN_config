# egg5_dias_CEN_config

This repo contains a Python config file which is used with dias_batch_running to specify inputs for running the Dias pipeline for CEN data.

## What does the config do?
dias_batch_running ([https://github.com/eastgenomics/dias_batch_running](https://github.com/eastgenomics/dias_batch_running)) is a Python module that runs the Dias pipeline for germline sequence data analysis on DNAnexus. The egg5_dias_CEN_config specifies the executables and their input files to be used in the Dias pipeline for analysing CEN data.

New versions of apps and app inputs for use in the Dias pipeline can be updated in the config without needing to update the pipeline itself

## Parts of the config
* GATKgCNV_call
    * specifies the app ID and inputs for CNV calling
* dias_reports
    * specifies the workflow ID, stage IDs (matching those in the workflow), and dynamic files for dias_reports.
* dias_cnvreports
    * specifies the workflow ID, stage IDs (matching those in the workflow), and dynamic files for dias_cnvreports.

## Versions of workflows and dynamic files in the config
Workflows:
* Dias reports: **dias_reports_v2.1.0**
    * DNAnexus workflow ID: `workflow-GXzkfYj4QPQp9z4Jz4BF09y6`
* Dias CNV reports: **dias_cnvreports_v1.1.0**
    * DNAnexus workflow ID: `workflow-GXzvJq84XZB1fJk9fBfG88XJ`

Apps:
* CNV calling app: **eggd_GATKgCNV_call**
    * v1.0.1 
    * DNAnexus app ID: `app-GJZVB2840KK0kxX998QjgXF0`

Dynamic files:
| File      | File name | DNAnexus file ID |
| --------- | --------- | ---------------- |
| genepanels | **230602_genepanels.tsv** | `file-GVx0vkQ433Gvq63k1Kj4Y562` |
| genes2transcripts | **230421_g2t.tsv** | `file-GV4P970433Gj6812zGVBZvB4` |
| exons_nirvana | **GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gk7gZ47gypK7ZZ` |
| exons_file for eggd_athena | **GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gf99pBPbJkV7bq` |
| cen_vep_config for SNV reports | **cen_vep_config_v1.1.6.json** | `file-GYX83Kj4z6jFbKy9fVj44BYK` |
| cen_vep_config for CNV reports | **cen-cnv_config_v1.1.0.json** | `file-GQGJ3Z84xyx0jp1q65K1Q1jY` |
| additional_regions for CNVs | **CEN_CNV_additional_regions_b37_v1.0.1.tsv** | `file-GJZQvg0433GkyFZg13K6VV6p` |
| gatk_docker | **GATK_v4.2.5.0.tar.gz** | `file-GBBP9JQ433GxV97xBpQkzYZx` |
| interval_list for CNV calling | **CEN_CNV_targets_v1.1.0_sorted.interval_list** | `file-GFPxzKj4V50pJX3F4vV58yyg` |
| annotation of interval_list for CNV calling | **CEN_CNV_targets_v1.1.0_sorted_annotation.tsv**| `file-GFPxzPQ4V50z4pv230p82G0q` |