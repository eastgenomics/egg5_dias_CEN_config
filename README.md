# dias_CEN_config_GRCh37_v3.1.0.json

This repo contains a JSON config file which is used with eggd_dias_batch to specify inputs for running the Dias pipeline for CEN data.

## What does the config do?
eggd_dias_batch ([https://github.com/eastgenomics/eggd_dias_batch](https://github.com/eastgenomics/eggd_dias_batch)) is a DNAnexus app that runs the Dias pipeline for germline sequence data analysis. The egg5_dias_CEN_config repo contains the dias_CEN_config file that specifies the executables and their input files to be used in the Dias pipeline for analysing CEN data on build GRCh37.

New versions of apps and app inputs for use in the Dias pipeline can be updated in the config without needing to update the pipeline itself.

## Parts of the config
The config specifies app IDs and workflow IDs at the top, followed by a `reference_files` dict for inputs common to multiple running modes.
The `modes` section specifies inputs specific to a running mode:
* cnv_call
    * specifies inputs for CNV calling.
* snv_reports
    * specifies inputs for dias_reports.
* cnv_reports
    * specifies inputs for dias_cnvreports.
* mosaic_reports
    * specifies inputs for dias_reports for mosaic reports.
* artemis
    * specifies inputs for [artemis](https://github.com/eastgenomics/eggd_artemis)


## Versions of workflows, apps, and dynamic files in the config
Workflows:
* Dias reports: **dias_reports_v2.2.0**
    * DNAnexus workflow ID: `workflow-Gg9Yvj04z4VvPFF3fygp63jy`
* Dias CNV reports: **dias_cnvreports_v1.2.0**
    * DNAnexus workflow ID: `workflow-Gg9Ybq841Ky1xfYgQ2qjqG3F`

Apps:
* CNV calling app: **eggd_GATKgCNV_call**
    * v1.0.2
    * DNAnexus app ID: `app-GZ4pXxj4xG062Bj5zjgP1Bb0`
* Artemis app: **eggd_artemis**
    * v1.4.0
    * DNAnexus app ID `app-GfKV5204ZF35Z47z31Qzqx90`

Dynamic files:
| File      | File name | DNAnexus file ID |
| --------- | --------- | ---------------- |
| genepanels | **240213_genepanels.tsv** | `file-GgBG75Q433Gk4pY5qpxbgVyz` |
| exons_nirvana | **GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gk7gZ47gypK7ZZ` |
| genes2transcripts | **240213_g2t.tsv** | `file-GgBG6p8433Gg7XK69fG7P9j7` |
| exons_file for eggd_athena | **GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gf99pBPbJkV7bq` |
| cen_vep_config for SNV/mosaic reports | **cen_vep_config_v1.1.12.json** | `file-GgFbqP84z6jB1870G2Zg450k` |
| cen_vep_config for CNV reports | **cen-cnv_config_v1.1.0.json** | `file-GQGJ3Z84xyx0jp1q65K1Q1jY` |
| panel_dump for eggd_optimised_filtering | **240202_panelapp_dump.json** | `file-Gg35Vf845B5bV08VqJ0qGV5V` |
| additional_regions for CNVs | **CEN_CNV_additional_regions_b37_v1.0.1.tsv** | `file-GJZQvg0433GkyFZg13K6VV6p` |
| gatk_docker | **GATK_v4.2.5.0.tar.gz** | `file-GBBP9JQ433GxV97xBpQkzYZx` |
| interval_list for CNV calling | **CEN_CNV_targets_v1.1.0_sorted.interval_list** | `file-GFPxzKj4V50pJX3F4vV58yyg` |
| annotation of interval_list for CNV calling | **CEN_CNV_targets_v1.1.0_sorted_annotation.tsv**| `file-GFPxzPQ4V50z4pv230p82G0q` |
| capture_bed for artemis | **CEN_CNV_targets_b37_v1.1.0.bed** | `file-GFPxpJj4GVV0Pfzv4VGYf1pq` |