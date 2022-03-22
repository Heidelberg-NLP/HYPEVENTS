# TimeTravel Data


Original data: 
```
{
  "story_id": "4fd7d150-b080-4fb1-a592-8c27fa6e1fc8",
  "premise": "Andrea wanted a picture of her jumping.",
  "initial": "She set the camera up.",
  "counterfactual": "She asked her friend to draw one.",
  "original_ending": "Then, she jumped in the air. The picture kept coming out wrong. It took twenty tries to get it right.",
  "edited_ending": [
    "Then, she jumped in the air to demonstrate how she wanted it to look.",
    "The picture kept coming out wrong.",
    "It took drawing it several times to get it right."
  ]
}
```

Our setup: 
```
Input : [S] Andrea wanted a picture of her jumping [MASK] The picture kept coming out wrong. It took twenty tries to get it right. [END] Andrea wanted a picture of her jumping. She set the camera up. 
Output: Then, she jumped in the air.

Input : [S] Andrea wanted a picture of her jumping [MASK] The picture kept coming out wrong. It took twenty tries to get it right. [END] Andrea wanted a picture of her jumping. She asked her friend to draw one.
Output: Then, she jumped in the air to demonstrate how she wanted it to look.

```

```
@inproceedings{qin-counterfactual,
    title = "Counterfactual Story Reasoning and Generation",
    author = "Qin, Lianhui and Bosselut, Antoine and Holtzman, Ari and  Bhagavatula, Chandra and  Clark, Elizabeth and Choi, Yejin",
    booktitle = "2019 Conference on Empirical Methods in Natural Language Processing.",
    month = "nov",
    year = "2019",
    address = "Hongkong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/pdf/1909.04076.pdf",
}
```
