
import yaml

data_yaml= {"first€":[], "second€":2,"third€":{}}

with open('file.yaml', 'w') as f_n:
  yaml.dump(data_yaml, f_n,default_flow_style=False)



