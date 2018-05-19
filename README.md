# Persian_NER
Persian Name Entity Recognition tool based on ArmanPersoNERCorpus
```
مهدی : B-pers
طارمی : I-pers
با : O
تیم : B-org
الغرافه : I-org
قطر : I-org
به : O
توافق : O
رسید : O
. : O
```

## Training
Based on [ArmanPersoNERCorpus](https://github.com/HaniehP/PersianNER) , I've trained a model and it's ready to use.
The training tool is developed by Python and using Tensorflow.
I've customized [guillaumegenthial](https://github.com/guillaumegenthial/sequence_tagging) source codes for this purpose.

## Using

First of all, you should download [this file](https://drive.google.com/open?id=1aWEkPNRxbDgFiaY8JBOYrhHGCMSIjbzv) and extract it to the main folder. It will create a folder named **results** .
You can find a file in **data** folder called **input.txt** . Put your text there and call **Python evaluate.py** . Your desired results will be written in **data/result.txt** . 

If you want to train your own model, follow instructions in https://github.com/guillaumegenthial/sequence_tagging.


## Citation

    Hanieh Poostchi, Ehsan Zare Borzeshi, and Massimo Piccardi, "BiLSTM-CRF for Persian Named-Entity Recognition; ArmanPersoNERCorpus: the First Entity-Annotated Persian Dataset," The 11th Edition of the Language Resources and Evaluation Conference (LREC), Miyazaki, Japan, 7-12 May 2018, ISLRN 399-379-640-828-6, ISLRN 921-509-141-609-6.
