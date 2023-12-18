> [!CAUTION]
> This repo contains a JSON file (compatible with new eggd_dias_batch - planned to go live in Jan 2024) and a Python script (compatible with old dias_batch - currently being used)
>
> The readme.md describes the JSON not the python script
>
> When new eggd_dias_batch goes live the python script will be deleted

# dias_CEN_config_GRCh37_v3.0.0.json

This repo contains a JSON config file which is used with eggd_dias_batch to specify inputs for running the Dias pipeline for CEN data.

## What does the config do?
eggd_dias_batch  ([https://github.com/eastgenomics/dias_batch_running](https://github.com/eastgenomics/dias_batch_running)) is a DNAnexus app that runs the Dias pipeline for germline sequence data analysis. The egg5_dias_CEN_config repo contains the dias_CEN_config file that specifies the executables and their input files to be used in the Dias pipeline for analysing CEN data on build GRCh37.

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
* Dias reports: **dias_reports_v2.1.0**
    * DNAnexus workflow ID: `workflow-GXzkfYj4QPQp9z4Jz4BF09y6`
* Dias CNV reports: **dias_cnvreports_v1.1.0**
    * DNAnexus workflow ID: `workflow-GXzvJq84XZB1fJk9fBfG88XJ`

Apps:
* CNV calling app: **eggd_GATKgCNV_call**
    * v1.0.2
    * DNAnexus app ID: `app-GZ4pXxj4xG062Bj5zjgP1Bb0`
* Artemis app: **eggd_artemis**
    * v1.3.0
    * DNAnexus app ID `app-GZ1X5zj4K5ZxyfYPPq4YgGv3`

Dynamic files:
| File      | File name | DNAnexus file ID |
| --------- | --------- | ---------------- |
| genepanels | **230602_genepanels.tsv** | `file-GVx0vkQ433Gvq63k1Kj4Y562` |
| genes2transcripts | **230421_g2t.tsv** | `file-GV4P970433Gj6812zGVBZvB4` |
| exons_nirvana | **GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gk7gZ47gypK7ZZ` |
| exons_file for eggd_athena | **GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gf99pBPbJkV7bq` |
| cen_vep_config for SNV/mosaic reports | **cen_vep_config_v1.1.9.json** | `file-GbPYpkQ4z6jBQxkqYBF32821` |
| cen_vep_config for CNV reports | **cen-cnv_config_v1.1.0.json** | `file-GQGJ3Z84xyx0jp1q65K1Q1jY` |
| additional_regions for CNVs | **CEN_CNV_additional_regions_b37_v1.0.1.tsv** | `file-GJZQvg0433GkyFZg13K6VV6p` |
| gatk_docker | **GATK_v4.2.5.0.tar.gz** | `file-GBBP9JQ433GxV97xBpQkzYZx` |
| interval_list for CNV calling | **CEN_CNV_targets_v1.1.0_sorted.interval_list** | `file-GFPxzKj4V50pJX3F4vV58yyg` |
| annotation of interval_list for CNV calling | **CEN_CNV_targets_v1.1.0_sorted_annotation.tsv**| `file-GFPxzPQ4V50z4pv230p82G0q` |
| capture_bed for artemis | **CEN_CNV_targets_b37_v1.1.0.bed** | `file-GFPxpJj4GVV0Pfzv4VGYf1pq` |