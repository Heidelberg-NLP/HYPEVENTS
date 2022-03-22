# Generating Hypothetical Events for Abductive Inference
![](https://img.shields.io/github/last-commit/Heidelberg-NLP/HYPEVENTS?color=blue) 

This directory contains the following parts of the 'Generating Hypothetical Events for Abductive Inference' experiment. 

Along with our code we include the relevant datasets used in the paper. The TIMETRAVEL dataset are taken from website: https://drive.google.com/file/d/150jP5FEHqJD3TmTO_8VGdgqBftTDKn4w/view 

We train GPT-2 model to generate a possible event that could happen next, given some counterfactual scenarios for a given story. 
We used the following script to prepare our training : 
```create_counterfactual_data.py```

Preprocessed data can be found in ```data/counterfactual```

## Unsupervised Setting

We used BERT score to evaluate our hypothesis that the generated possible next event observation (O^{2}_{H_{j}}) given the more plausible hypothesis H_{j}
should be more similar to observation {O_2}.

```pip install bert-score```

run: ```get_bert_score.py generated_file test_file label_file``` 


### Citation

```
@inproceedings{paul-frank-2021-generating,
    title = "Generating Hypothetical Events for Abductive Inference",
    author = "Paul, Debjit  and
      Frank, Anette",
    booktitle = "Proceedings of *SEM 2021: The Tenth Joint Conference on Lexical and Computational Semantics",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.starsem-1.6",
    doi = "10.18653/v1/2021.starsem-1.6",
    pages = "67--77"
    }
```


