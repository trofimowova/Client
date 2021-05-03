"""import csv
import os
from os import listdir
from os.path import isfile, join
import re

def get_data(road):
  os_prod_list = []
  os_name_list = []
  os_code_list = []
  os_type_list = []
  headers_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]



  list_of_files = os.listdir(road)
  #print(list_of_files)
  for file in list_of_files: # проходим по элементам листа (кроме первого, это какая-то системная папка)
      file = open(road + '/' + file,'r')
      lines = file.readlines()   # file.readlines() надо но для наглядности берем только первую строку
      os_prod = [x for x in lines if x.startswith('Изготовитель системы:')]
        #print(os_name)
      clean_os_prod =  re.findall(r'Изготовитель системы:(.+?)\n', os_prod[0])
      os_prod_list.append(clean_os_prod[0].strip())
        
        
      os_name = [x for x in lines if x.startswith('Название ОС:')]
      clean_os_name =  re.findall(r'Название ОС:(.+?)\n', os_name[0])
      os_name_list.append(clean_os_name[0].strip())


      os_code = [x for x in lines if x.startswith('Код продукта:')]
      clean_os_code =  re.findall(r'Код продукта:(.+?)\n', os_code[0])
      os_code_list.append(clean_os_code[0].strip())

      os_type = [x for x in lines if x.startswith('Тип системы:')]
      clean_os_type =  re.findall(r'Тип системы:(.+?)\n', os_type[0])
      os_type_list.append(clean_os_type[0].strip())
      

      file.close()

      
      main_data=[headers_data,os_prod_list,os_name_list,os_code_list,os_type_list]
 
  return (main_data)



def write_to_csv(tab):
  with open ('write_file_road.csv', 'w') as f_n:
    f_n_writer =csv.writer(f_n,quoting=csv.QUOTE_NONNUMERIC)
    f_n_writer.writerows(get_data(tab))




path_csv = './info'


if __name__ =='__main__':
  write_to_csv(path_csv)"""



"""import json

orders = {"orders": []}
def get_dict(a,b,c,d,e):

  key_list =["item","quantity","price","buyer","data"]
#value_list=[(input(i))for i in range(5)]
  value_list = [a,b,c,d,e]
  dict_t=dict(zip(key_list, value_list))
  orders['orders']=[dict_t]
  return orders



def write_order_to_json(a,b,c,d,e):
  get_dict(a,b,c,d,e,)
  with open ('orders.json','w') as f_n:
    json.dump(orders,f_n,indent=4,ensure_ascii=False)

 

write_order_to_json("Видеокарта",3,500,"Петр","12.12.2021")"""



import yaml

data_yaml= {"first€":[], "second€":2,"third€":{}}

with open('file.yaml', 'w') as f_n:
  yaml.dump(data_yaml, f_n,default_flow_style=False)
