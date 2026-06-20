# Confidence Scoring Framework

Confidence measures the strength of evidence supporting an explanation.

Confidence is not the same as risk.

A region may have a high risk score but low confidence if the available evidence is limited.

## Low Confidence

Characteristics:

* Single source of evidence
* No supporting contextual information
* No temporal data

Example:

NDVI = 0.22

Available Information:

* NDVI only

Possible Explanations:

* Vegetation stress
* Urbanization
* Seasonal effects

Because multiple explanations are plausible, confidence remains low.

## Medium Confidence

Characteristics:

* Multiple supporting observations
* Limited contextual evidence

Example:

NDVI = 0.22

Distance to Water = 4 km

Evidence:

* Low vegetation health
* Limited proximity to water

Possible Interpretation:

Water stress becomes more plausible.

Confidence:

Medium

## High Confidence

Characteristics:

* Multiple independent evidence sources
* Supporting temporal patterns
* Limited contradictory evidence

Example:

NDVI decline observed for three consecutive years.

Distance to water remains high.

Rainfall deficit observed.

Land use remains unchanged.

Multiple indicators support vegetation stress.

Confidence:

High

## Factors Increasing Confidence

* Temporal consistency
* Multiple independent signals
* Supporting environmental context
* Limited contradictory evidence

## Factors Reducing Confidence

* Single observation
* Conflicting evidence
* Missing contextual information
* Lack of historical comparison

## Recommended Communication Style

Instead of:

"The cause is water stress."

Use:

"The available evidence moderately supports a water stress hypothesis, although alternative explanations remain possible."

Confidence-aware explanations help prevent overconfident conclusions and improve trust in Earth Intelligence systems.
