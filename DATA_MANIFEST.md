# Data Manifest

This document provides a structured overview of the data assets, code, and analytical outputs involved in the project, as well as their storage locations and preservation status.  
Its purpose is to support transparency, traceability, and long-term preservation within the data life cycle framework.

---

## 1. Overview of preserved assets

The project distinguishes between different types of assets, each preserved according to its role within the data life cycle:

- Raw data (bronze layer)
- Processed data (silver and gold layers)
- Code and utilities
- Analytical results
- Documentation and metadata

---

## 2. Raw data (Bronze layer)

**Description**  
Raw datasets are obtained directly from the original data providers without manual modification.

**Content**
- GDP data from the World Bank (CSV format)
- Air traffic data from EUROCONTROL performance datasets (CSV format, annual files)

**Storage location**
- Google Drive (shared project workspace)

**Preservation strategy**
- Raw files are preserved in their original structure
- Multiple versions are retained when new data are downloaded
- Files are not overwritten

**Update frequency**
- Periodic updates through re-execution of the ingestion pipeline

---

## 3. Processed data (Silver layer)

**Description**  
Silver datasets result from cleaning, filtering, and standardisation of the raw data.

**Content**
- Harmonised air traffic dataset
- Harmonised GDP dataset

**Storage location**
- Google Drive

**Preservation strategy**
- Derived datasets are regenerated programmatically
- No manual editing is applied
- Versions correspond to pipeline executions

---

## 4. Analytical data (Gold layer)

**Description**  
The gold dataset represents the final analytical table used for statistical analysis.

**Content**
- Country–year level dataset
- Variables include total number of flights and GDP

**Storage location**
- Google Drive

**Preservation strategy**
- The dataset is fully reproducible from the silver layer
- Each pipeline execution produces an updated analytical snapshot

---

## 5. Code and utilities

**Description**  
All code required to reproduce the data pipeline is preserved.

**Content**
- Jupyter notebooks implementing the bronze–silver–gold workflow
- Reusable utility functions (`utils.py`)

**Storage location**
- GitHub repository

**Preservation strategy**
- Version control using Git
- Complete history of changes preserved
- Code released under the MIT License

---

## 6. Analytical outputs

**Description**  
Final analytical results are preserved in a non-executable, human-readable format.

**Content**
- Rendered HTML file containing analysis, visualisations, and conclusions

**Storage location**
- GitHub repository (`analysis/` directory)

**Preservation strategy**
- HTML format selected to minimise dependency on specific software environments
- Outputs represent a snapshot of the analysis at a given pipeline execution

---

## 7. Documentation and metadata

**Description**  
Project documentation and metadata provide context necessary for reuse and interpretation.

**Content**
- Project README
- Data manifest
- Analytical and technical decisions (`DECISIONS.md`)

**Storage location**
- GitHub repository

**Preservation strategy**
- Documentation is versioned alongside the code
- Changes are tracked through Git history

---

## 8. Excluded assets

The following assets are intentionally not preserved in the GitHub repository:
- Raw and processed datasets (CSV files)
- Intermediate large data files

These assets are stored in Google Drive to avoid duplication and unnecessary data transfer.

---

## 9. Summary

This data manifest reflects a preservation strategy that separates data storage from code and documentation, supports periodic updates, and ensures full reproducibility of the analytical workflow while maintaining clarity and long-term accessibility.
