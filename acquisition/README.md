# Telemetry Acquisition

This directory contains the telemetry acquisition component used in the research.

The public script:

    poll_epmp_public.sh

retrieves operational metrics from Cambium ePMP equipment through SSH and
stores the results in daily CSV files.

The acquisition includes:

- MCS DL and UL
- SNR DL and UL
- RSSI Chain 0
- RSSI Chain 1
- Physical Downlink Rate
- Link RSSI

The original experimental implementation was scheduled approximately once per
minute using cron.

Authentication credentials are not included in this repository.
