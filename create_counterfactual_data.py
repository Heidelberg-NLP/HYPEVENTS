import argparse
import os
import sys
import random
import ast
import math
from random import randint
import codecs
import json
import spacy
nlp = spacy.load("en_core_web_sm")
#sentencizer = nlp.create_pipe("sentencizer")
from tqdm import tqdm


def main(): 

      parser = argparse.ArgumentParser()
      parser.add_argument("txtfile",nargs='?')
      parser.add_argument("types",nargs='?')
      args = parser.parse_args()
      make_data(args.txtfile, args.types)		

def make_data(data, types):   
      count = 0 
      length = 0
      if types=='train':
          f1=open('train100k.txt','w')
          f1.close()
      elif types=='dev':
          f1 = open('dev1.txt', 'w')
          f1.close()
      else: 
          f1 = open('test.txt','w')
          f1.close()
      num_lines = sum(1 for line in open(data,'r'))     
      with open(data,'r') as f:
           for line in tqdm(f, total=num_lines):    
               line = json.loads(line)
               count+=1	
               flag = False
               initial = line["initial"].strip('\n')
               counterfactual = line["counterfactual"].strip('\n')
               if types =='dev' or types == 'test':
                   counter_third_line = line["edited_endings"][0][0]
               else: 
                   counter_third_line = line["edited_ending"][0]
               
               
               original = nlp(line["original_ending"])
               original_sent = []
               discourse = ['however','nevertheless','on the other hand', 'on the contrary', 'while', 'in contrast', 'otherwise', 'conversely', 'whereas', 'beside', 'despite', 'whereas', 'but', 'all of a sudden'] 	
               
               for sent in original.sents:
                      original_sent.append(sent.text)
               #for i in discourse: 
               #    for j in original_sents:
               #        if i in j:
               #             flag = True  
               #             break
               
               if types!='train':
                   s = '["SOS"] '+ str(line["premise"]) +' ["MASK"] '+ str(original_sent[-1]) +' ["EOS"] '+ '["SOS"] '+str(line["premise"]) +' ["SEP"] ' + str(counterfactual) + ' ["SEP"]'+ '\t' + line["edited_endings"][0][0] +' ["EOS"]'+'\t' + str(1) +'\n'
                   p = '["SOS"] '+ str(line["premise"])+' ["MASK"] '+ str(original_sent[-1]) +' ["EOS"] '+ '["SOS"] '+str(line["premise"]) +' ["SEP"] ' + str(initial) + ' ["SEP"]'+ '\t' + str(original_sent[0]) + ' ["EOS"]'+ '\t' + str(1) +'\n'
                   if types=="dev":
                       f1 = open('dev1.txt','a')
                   else: 
                       f1 = open('test.txt', 'a')
                   f1.write(s)
                   f1.write(p)
                   f1.close()
               else: 
                   p = str(line["premise"])+' ["MASK"] '+ str(original_sent[-1]) +' ["EOS"] '+ '["SOS"] '+str(line["premise"]) +' ["SEP"] ' + str(initial) + ' ["SEP"]'+ '\t' + str(line["edited_ending"][0]) + ' ["EOS"]'+'\n'
                   s = str(line["premise"])+' ["MASK"] '+ str(original_sent[-1]) +' ["EOS"] '+ '["SOS"] '+str(line["premise"]) +' ["SEP"] ' + str(initial) + ' ["SEP"]'+ '\t' + str(original_sent[0]) + ' ["EOS"]'+'\n'
                   f1 = open('train100k.txt','a')
                   f1.write(s)
                   f1.write(p)
                   f1.close()
            
      return	           

if __name__ =='__main__':
    main()	
