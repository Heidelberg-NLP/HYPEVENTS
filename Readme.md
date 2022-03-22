# Generating Hypothetical Events for Abductive Inference
![](https://img.shields.io/github/last-commit/Heidelberg-NLP/HYPEVENTS?color=blue) 

This directory contains the following parts of the 'Generating Hypothetical Events for Abductive Inference' experiment. 

Along with our code we include the relevant datasets used in the paper. The TIMETRAVEL dataset are taken from website: https://drive.google.com/file/d/150jP5FEHqJD3TmTO_8VGdgqBftTDKn4w/view 

We train GPT-2 model to generate a possible event that could happen next, given some counterfactual scenarios for a given story. 
We used the following script to prepare our training : 
```create_counterfactual_data.py```

Preprocessed data can be found in ```data/counterfactual```

