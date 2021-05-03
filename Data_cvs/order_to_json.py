import json

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

 

write_order_to_json("Видеокарта",3,500,"Петр","12.12.2021")
