# heart-stroke-prediction documentation!

## Description

What demographic and health-related factors significantly predict the occurrence of a stroke in patients?

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `az storage blob upload-batch -d` to recursively sync files in `data/` up to `kubernetes/data/`.
* `make sync_data_down` will use `az storage blob upload-batch -d` to recursively sync files from `kubernetes/data/` to `data/`.


