import argparse
import os
import sys
import random
import ast
import math
from random import randint
import codecs
import json
import pickle
import bert_score
from bert_score import score
from rouge_score import rouge_scorer
import rouge 
import ast 
import nltk
import spacy

nlp = spacy.load("en_core_web_sm")

def main(): 

      parser = argparse.ArgumentParser()
      parser.add_argument("picklefile",nargs='?')
      parser.add_argument("txtfile",nargs='?')
      parser.add_argument("labelfile",nargs='?')
      args = parser.parse_args()
      make_data(args.txtfile,args.picklefile, args.labelfile)
      
def make_data(data, test_pickle, label):

      labels = []
      with open(label,'r') as f:
           for line in f: 
               line = line.replace('\n','')
               line = line.split('\t')
               labels.append(line)
      numbers = []
            
      with open(test_pickle,'r') as f:
            for line in f:
               line = ast.literal_eval(line)
               s = line["beams"][1]  
               numbers.append(s)
      
      count = 0  
      count_s = 0  
      obs = ''     
      correct = []
      wrong = []
      pred = {}
      orig = {}
      refs = []
      obs1 = []

      obs2 = []
      with open(data,'r') as f:
          for line in f: 
              line = json.loads(line)
              line["obs1"] = line["obs1"].replace("\n","")
              line["obs2"] = line["obs2"].replace("\n","")
              orig[str(line["obs1"]+line["obs2"])] = []
              pred[str(line["obs1"]+line["obs2"])] = []

      with open(data,'r') as f:
           for line in f:
                line = json.loads(line) 
                line["obs1"] = line["obs1"].replace("\n","")
                line["obs2"] = line["obs2"].replace("\n","")
                if line["label"]=='1':
                    correct.append(str(numbers[count_s].replace('["eos"]', '')))
                    pred[str(line["obs1"]+line["obs2"])]=[str(numbers[count_s].replace('["eos"]', ''))]   
                    obs1.append(str(line["obs1"].replace("\n","")))
                    obs2.append(str(line["obs2"].replace("\n","")))
                    refs.append(str(line["hyp1"].replace("\n","")))
                    orig[str(line["obs1"].replace("\n","")) + str(line["obs2"].replace("\n",""))].append(str(line["hyp1"].replace("\n","").lower()))

                elif line["label"]=='2':   
                    correct.append(str(numbers[count_s].replace('["eos"]', ''))) 
                    pred[str(line["obs1"].replace('\n','')+line["obs2"].replace('\n',''))] = [str(numbers[count_s].replace('["eos"]', ''))]  
                    obs1.append(str(line["obs1"].replace("\n","")))
                    obs2.append(str(line["obs2"].replace("\n","")))
                    refs.append(str(line["hyp2"].replace("\n","")))    
                    orig[str(line["obs1"].replace("\n","")) + str(line["obs2"].replace("\n",""))].append(str(line["hyp2"].replace("\n","").lower()))

                count_s = count_s+1
                
      P_cor, R_cor, F_cor = score(correct, refs, lang="en", model_type="bert-base-uncased", verbose=True)
      cor = F_cor.tolist()
      print(F_cor.mean())
      
      return	           

if __name__ =='__main__':
    main()
