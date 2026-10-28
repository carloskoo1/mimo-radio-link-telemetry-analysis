# IEEE Access manuscript V21 — documentary verification log

Date: 2026-10-27. This note is an editorial and provenance record, **not a new experiment**.

## Primary bibliographic correction
Two existing Zenodo/DataCite DOIs are associated with the **software project**, not with two distinct publications:
- `10.5281/zenodo.21844766`: *Temporal Analysis of Signal Imbalance in a 5.8 GHz MIMO Radio Link*, software, version **v2.0.1**. Frozen analysis-code commit: `e91214bb9931131ef971c930a76c46419076525a`.
- `10.5281/zenodo.23551370`: another version of the same software record (related to **v2.0.2**). **It is not an identifier for the undergraduate thesis.**

The UNC undergraduate thesis is cited in the article independently as an institutional thesis manuscript. No independent published thesis DOI was established during this check.

## Literature correction
Reference [8] uses DOI `10.32911/as.2023.v16.n1.1012`. Crossref metadata gives the original Spanish title:
“Radio enlace autónomo para transmisión de datos para sensores en alta montaña: Quebrada Cojup, Huaraz - Perú.”
The previous English reference title mentioning Laguna Palcacocha was not faithful to that registered article title. Reference updated accordingly.
The arXiv DOI `10.48550/arXiv.2501.01344` resolves via DataCite, rather than Crossref.

## Template and editorial checks
The current official IEEE Access Microsoft Word template was downloaded from
https://ieeeaccess.ieee.org/authors/submission-guidelines/
and inspected. The V21 Word manuscript was reflowed with the official page dimensions and margin/column geometry, then visually inspected and rendered to an eight-page PDF. The cover letter was revised to a one-page document. Six author biographies are present. The manuscript names Carlos Jesús Koo Labrín as first and corresponding author and has Jhon Cristhian Torres Hoyos last, following team approval.

The corresponding author's public ORCID record `0000-0002-0323-2961` responds, but actual IEEE Author Portal connection must be confirmed in the submitter's account.

## Reproducibility and scope
The publicly documented V19 analysis reproduces a Spearman association of `0.4925851782879838` from 1,989 complete hourly records. The original hourly panel has SHA-256
`977d95ec7328edc5bc881c0ebd944ced044d2724a5ede8c5f8be7e43a65a981b`.
Raw telemetry and CLI records are **not** distributed publicly. Supplementary Material S1 V21 contains only field descriptions, aggregate results, a read-only script, the input hash, and a bibliographic clarification.

Cambium documents downlink received power at the SM and uplink received power at the AP, but the firmware-specific semantics of the historic AP `show rssi` chain fields remain incompletely verified. The article treats the association with `connectedSTADLRateMbps` as **descriptive**, without assigning a causal, same-direction link mechanism.

## References
- https://ieeeaccess.ieee.org/authors/preparing-your-article/
- https://ieeeaccess.ieee.org/authors/submission-guidelines/
- https://zenodo.org/records/21844766
- https://zenodo.org/records/23551370
- https://community.cambiumnetworks.com/t/epmp-how-to-view-a-radio-s-wireless-interface/59109

**This file does not publish any raw telemetry or secret credentials.**
