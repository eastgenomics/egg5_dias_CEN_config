# dias_CEN_config_GRCh37_v3.2.3.json

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
* Dias reports: **dias_reports_v2.2.2**
    * DNAnexus workflow ID: `workflow-GkbJY284FpfgqF8ggz57fVY2`
* Dias CNV reports: **dias_cnvreports_v1.2.0**
    * DNAnexus workflow ID: `workflow-Gj77F9041Ky3Vp045gpKx0B4`

Apps:
* CNV calling app: **eggd_GATKgCNV_call**
    * v1.0.2
    * DNAnexus app ID: `app-GZ4pXxj4xG062Bj5zjgP1Bb0`
* Artemis app: **eggd_artemis**
    * v1.6.0
    * DNAnexus app ID `app-GxVK0bQ4KzQzXkJ3Xg53ypXv`

Dynamic files:
| File      | File name | DNAnexus file ID |
| --------- | --------- | ---------------- |
| genepanels | **241024_genepanels.tsv** | `file-GvJ5fbQ4qQYq73gjGyP57zFB` |
| exons | **GCF_000001405.39_GRCh38.p13_genomic_20211119.exon_5bp.tsv** | `file-GyFfgpQ4fJPv132574bFQfV5` |
| genes2transcripts | **g2t_grch38_v2.0.0.tsv** | `file-Gyy99kj4zqZJ7Qp4145PXv9F` |
| exons_with_symbols for eggd_athena | **GCF_000001405.39_GRCh38.p13_genomic_20211119.symbols.exon_5bp.tsv** | `file-Gyb29P84fJPqZJ37pfjz1vZB` |
| cen_vep_config for SNV/mosaic reports | **cen_vep_config_GRCh38_v1.0.0.json** | `file-GyXF5304z6jF9JVxZjQ1Pk2P` |
| cen_vep_config for CNV reports | **cen-cnv_config_GRCh38_v1.0.0.json** | `file-GyXyyp04Q8Xpj5fJ8v45by9k` |
| panel_dump for eggd_optimised_filtering | **241030_panelapp_dump.json** | `file-GvVg3qj4Y54jBF8bgX62gkfQ` |
| additional_regions for CNVs | **CEN_CNV_additional_regions_b38_v1.0.0.tsv** | `file-GfKb08j4679f4jbfxf8XP7JZ` |
| additional_regions for SNVs | **CEN_SNV_additional_regions_GRCh38_v1.0.0.tsv** | `file-Gz4gg184Pp8FbPxp42VBzF52` |
| gatk_docker | **GATK_v4.6.0.0.tar.gz** | `file-GpZz87Q4ZbZkxJJGx9b02gyV` |
| interval_list for CNV calling | **CEN_CNV_targets_b38_v1.0.0.interval_list** | `file-GfFGFP04z704bp38ykFvgX03` |
| annotation of interval_list for CNV calling | **CEN_CNV_targets_b38_v1.0.0_annotation.tsv**| `file-GfFGFPQ4z70JG5VPQP28V1PV` |
| capture_bed for artemis | **CEN_CNV_targets_b38_v1.0.0.bed** | `file-Gf0gX1Q4XGyqKzj4yFJyy0XV` |


## Cmd to check the config file ids
```bash
config_file="dias_CEN_config_GRCh38_v4.0.0.json"
jq -r '.. | objects | .id? // empty' "${config_file}" | while read -r file_id; do
   dx describe "$file_id" --json | jq -r '"\(.id) \(.name)"';
done
```