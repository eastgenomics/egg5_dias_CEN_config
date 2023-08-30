# egg5_dias_CEN_config

This repo contains a Python config file which is used with dias_batch_running, to specify inputs for running the Dias pipeline for CEN data.

## What does the config do?
dias_batch_running ([https://github.com/eastgenomics/dias_batch_running](https://github.com/eastgenomics/dias_batch_running)) is a Python module that runs the Dias pipeline for germline sequence data analysis. This config specifies the executables and their input files to be used in the Dias pipeline for analysing CEN data.

New versions of apps and app inputs for use in the Dias pipeline can be updated in the config without needing to update the pipeline itself

## Parts of the config
* GATKgCNV_call
    * specifies the app ID and inputs for CNV calling
* dias_reports
    * specifies the workflow ID, stage IDs (matching those in the workflow), and dynamic files for dias_reports.
* dias_cnvreports
    * specifies the workflow ID, stage IDs (matching those in the workflow), and dynamic files for dias_cnvreports.

