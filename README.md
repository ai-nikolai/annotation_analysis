BRR
# Annotation Analysis
## Package to analyse inter-annotator agreement.
Simple package to compute Interannotation Agreement with a simple interface.

## Getting Started
Install package:
```bash
pip3 install annotation_analysis
```


## Documentation
### function krippendorf_alpha(annotations:List[List],labels:Optional[List], ignore=Optional[List])
```python
"""
Arguments:
    - annotations:
        - The list of annotations, assumed to be one "row" per annotator (i.e. annotations[0] is annotator #1).
        - Number of Columns represents the number of datapoints.
        - Important: at this stage only hashable values are allowed.
        - E.g. with labels ["A","B"], and three datapoints and 2 annotators the following would be the valid structure:
        - [["A","B","A"],["A","B","B"]],
            - Annotator #1 (index=0) -> ["A","B","A"]
            - Annotator #2 (index=1) -> ["A","B","B"]

    - labels:
        - Represents the optional list of valid labels.
        - Important: at this stage only hashable values are allowed.

    - ignore:
        - Represents a list of optional labels that should be ignored
        - I.e. If this is non-empty then for any datapoint, if any of the annotators has the ignored label, the data point with all annotators is ignored

Return:
    - Krippendorff Alpha score for all annotators.
"""
```

### function fleiss_kappa(annotations:List[List],labels:Optional[List], ignore=Optional[List])
```python
"""
Arguments:
    - annotations:
        - The list of annotations, assumed to be one "row" per annotator (i.e. annotations[0] is annotator #1).
        - Number of Columns represents the number of datapoints.
        - Important: at this stage only hashable values are allowed.
        - E.g. with labels ["A","B"], and three datapoints and 2 annotators the following would be the valid structure:
        - [["A","B","A"],["A","B","B"]],
            - Annotator #1 (index=0) -> ["A","B","A"]
            - Annotator #2 (index=1) -> ["A","B","B"]

    - labels:
        - Represents the optional list of valid labels.
        - Important: at this stage only hashable values are allowed.

    - ignore:
        - Represents a list of optional labels that should be ignored
        - I.e. If this is non-empty then for any datapoint, if any of the annotators has the ignored label, the data point with all annotators is ignored

Return:
    - Fleiss Kappa score for all annotators.
"""
```


#### (C) - Nikolai Rozanov 2022
