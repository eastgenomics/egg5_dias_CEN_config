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
* dias_reports **2.1.0**
    * DNAnexus workflow ID: `workflow-GXzkfYj4QPQp9z4Jz4BF09y6`
* dias_cnvreports **1.1.0**
    * DNAnexus workflow ID: `workflow-GXzvJq84XZB1fJk9fBfG88XJ`

Dynamic files:
* genepanels **230602**
    * DNAnexus file ID: `file-GVx0vkQ433Gvq63k1Kj4Y562`
* genes2transcripts **230421**
    * DNAnexus file ID: `file-GV4P970433Gj6812zGVBZvB4`
* exons_nirvana **GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0**
    * DNAnexus file ID `file-GF611Z8433Gk7gZ47gypK7ZZ`
* exons_file for eggd_athena **GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0**
    * DNAnexus file ID: `file-GF611Z8433Gf99pBPbJkV7bq`
* cen_vep_config for SNV reports **1.1.6**
    * DNAnexus file ID `file-GYX83Kj4z6jFbKy9fVj44BYK`
* cen_vep_config for CNV reports **1.1.0**
    * DNAnexus file ID `file-GQGJ3Z84xyx0jp1q65K1Q1jY`
* additional_regions for CNVs **1.0.1**
    * DNAnexus file ID `file-GJZQvg0433GkyFZg13K6VV6p`