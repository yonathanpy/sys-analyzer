# sys-analyzer

Lightweight system telemetry collector and anomaly detection engine designed for continuous host-level monitoring.

## Overview

`sys-analyzer` is a modular monitoring tool that collects system metrics (CPU, memory, disk usage, process activity) and performs real-time heuristic analysis to identify abnormal behavior patterns.

The project is designed with separation of concerns:

* data collection
* state aggregation
* statistical analysis
* alert generation

It is intended for defensive security use cases such as:

* baseline behavior profiling
* anomaly detection
* resource abuse detection
* early signal identification in compromised environments

## Architecture

The system operates as two concurrent loops:

1. **Collection Loop**

   * Samples system metrics at fixed intervals
   * Normalizes and pushes data into a bounded history buffer

2. **Analysis Loop**

   * Consumes historical snapshots
   * Computes rolling averages
   * Detects spikes and threshold violations
   * Emits alerts

### Data Flow

collector → stats buffer → analyzer → alerts

## Components

### main.py

Entry point. Initializes engine, starts concurrent loops, handles lifecycle.

### collector.py

Responsible for gathering telemetry:

* CPU utilization
* memory usage
* disk usage
* process count

Uses `psutil` for cross-platform metric access.

### stats.py

Maintains a bounded in-memory time series using a deque.
Supports snapshot extraction for analysis.

### analyzer.py

Implements heuristic-based detection:

* rolling average threshold checks
* sudden spike detection between intervals
* configurable limits

### config.py

Handles configuration loading, defaults, and validation.

### cli.py

Supports runtime overrides and configuration export.

### utils.py

Utility helpers (time formatting, averages, formatting).

## Installation

```bash
git clone https://github.com/yourname/sys-analyzer.git
cd sys-analyzer
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Optional parameters:

```bash
python main.py --interval 1 --analysis-interval 3
```

## Configuration

Default configuration:

```json
{
  "interval": 2,
  "analysis_interval": 5,
  "cpu_threshold": 85,
  "memory_threshold": 80,
  "history_size": 50
}
```

You can override values via CLI or by supplying a config file.

## Detection Strategy

The analyzer uses simple but effective heuristics:

* Mean resource utilization over sliding window
* Delta-based spike detection between consecutive samples
* Configurable thresholds to adapt to environment baselines

This avoids overfitting and keeps runtime overhead minimal.

## Performance Characteristics

* Low CPU overhead (<1–2% on idle systems)
* Memory usage bounded by history size
* No external services required
* Fully local execution


