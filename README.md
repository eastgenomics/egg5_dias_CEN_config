# egg5_dias_CEN_config

This repo contains a JSON config files for GRCh37 and GRCh38 which are used with eggd_dias_batch to specify inputs for running the Dias pipeline for CEN data.

## What does the config do?
eggd_dias_batch ([https://github.com/eastgenomics/eggd_dias_batch](https://github.com/eastgenomics/eggd_dias_batch)) is a DNAnexus app that runs the Dias pipeline for germline sequence data analysis. The egg5_dias_CEN_config repo contains the dias_CEN_config file that specifies the executables and their input files to be used in the Dias pipeline for analysing CEN data on build GRCh37/GRCh38.

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

# Versions of apps, files, and docker images in the config
The following table lists the versions of apps, files, and docker images used in the config for both GRCh38 and GRCh37. The DNAnexus file IDs are provided for each file.

| Type | File Description | GRCh38 File Name | GRCh38 DNAnexus File ID | GRCh37 File Name | GRCh37 DNAnexus File ID |
|------|------------------|------------------|--------------------------|------------------|--------------------------|
| workflow | dias_reports | **dias_reports_v2.2.3** | `workflow-J2j7GzQ432PYvJ9P270bfj88` | **dias_reports_v2.2.3** | `workflow-J2j7GzQ432PYvJ9P270bfj88` |
| workflow | dias_cnvreports | **dias_cnvreports_v1.3.0** | `workflow-J2j7XYj432PQ6YBBX341bQJk` | **dias_cnvreports_v1.3.0** | `workflow-J2j7XYj432PQ6YBBX341bQJk` |
| app | eggd_GATKgCNV_call | **eggd_GATKgCNV_call_v2.0.0** | `app-GvZB5p846Vg69fBg0Fq10938` | **eggd_GATKgCNV_call_v2.0.0** | `app-GvZB5p846Vg69fBg0Fq10938` |
| app | eggd_artemis | **eggd_artemis_v1.7.1** | `app-J2pjgJQ4Qg0gk1pQJqqQ6KPz` | **eggd_artemis_v1.5.0** | `app-GkbJ7p0463bjk9VKv3x8G5F8` |
| file | genepanels | **250711_genepanels.tsv** | `file-J1jXFZj4XG7Qvj0PGZGg96Pg` | **241024_genepanels.tsv** | `file-GvJ5fbQ4qQYq73gjGyP57zFB` |
| file | exons | **GCF_000001405.39_GRCh38.p13_genomic_20211119.exon_5bp.tsv** | `file-GyFfgpQ4fJPv132574bFQfV5` | **GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gk7gZ47gypK7ZZ` |
| file | genes2transcripts | **g2t_grch38_v2.1.0.tsv** | `file-J1q297j4J0b3V741GxbX0Q14` | **240402_g2t.tsv** | `file-Gj770X8433Gb506pjq1PxXG9` |
| file | exons_with_symbols for eggd_athena | **GCF_000001405.39_GRCh38.p13_genomic_20211119.symbols.exon_5bp.tsv** | `file-Gyb29P84fJPqZJ37pfjz1vZB` | **GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gf99pBPbJkV7bq` |
| config | cen_vep_config for SNV/mosaic reports | **cen_vep_config_GRCh38_v1.1.4.json** | `file-J2Xpy6j4z6jPXXV9YYVykXbg` | **cen_vep_config_v1.2.1.json** | `file-J04Kfv04z6j02Jz1Zj9VvK7k` |
| config | cen_vep_config for CNV reports | **cen-cnv_config_GRCh38_v1.0.0.json** | `file-GyXyyp04Q8Xpj5fJ8v45by9k` | **cen-cnv_config_v1.1.0.json** | `file-GQGJ3Z84xyx0jp1q65K1Q1jY` |
| file | panel_dump for eggd_optimised_filtering | **250530_panelapp_dump.json** | `file-J0yk3V04VVYxJ9bz3QPPzxPg` | **241030_panelapp_dump.json** | `file-GvVg3qj4Y54jBF8bgX62gkfQ` |
| file | additional_regions for CNVs | **CEN_CNV_additional_regions_b38_v1.0.0.tsv** | `file-GfKb08j4679f4jbfxf8XP7JZ` | **CEN_CNV_additional_regions_b37_v1.0.1.tsv** | `file-GJZQvg0433GkyFZg13K6VV6p` |
| file | additional_regions for SNVs | **CEN_SNV_additional_regions_GRCh38_v1.0.0.tsv** | `file-J0zJ06Q4Pp80Q73204yZkzvz` | **CEN_SNV_additional_regions_b37_v1.0.0.tsv** | `file-Gpy96q04PKYjjg9kbQy692bF` |
| docker | gatk_docker | **GATK_v4.6.0.0.tar.gz** | `file-GpZz87Q4ZbZkxJJGx9b02gyV` | **GATK_v4.6.0.0.tar.gz** | `file-GpZz87Q4ZbZkxJJGx9b02gyV` |
| file | interval_list for CNV calling | **CEN_CNV_targets_b38_v1.0.0.interval_list** | `file-GfFGFP04z704bp38ykFvgX03` | **CEN_CNV_targets_v1.1.0_sorted.interval_list** | `file-GFPxzKj4V50pJX3F4vV58yyg` |
| file | annotation of interval_list for CNV calling | **CEN_CNV_targets_b38_v1.0.0_annotation.tsv** | `file-GfFGFPQ4z70JG5VPQP28V1PV` | **CEN_CNV_targets_v1.1.0_sorted_annotation.tsv** | `file-GFPxzPQ4V50z4pv230p82G0q` |
| file | capture bed for artemis | **CEN_CNV_targets_b38_v1.0.0.bed** | `file-Gf0gX1Q4XGyqKzj4yFJyy0XV` | **CEN_CNV_targets_b37_v1.1.0.bed** | `file-GFPxpJj4GVV0Pfzv4VGYf1pq` |

## Cmd to check the config file ids (not comprehensive)
```bash
config_file="dias_CEN_config_GRCh38_v4.4.0.json"
jq -r '.. | objects | .id? // empty' "${config_file}" | while read -r file_id; do
   dx describe "$file_id" --json | jq -r '"\(.id) \(.name)"';
done
```
