
from argparse import *
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-a","--adress",help="Shows server",default="adress")
parser.add_argument("-p","--port",help="Shows port",default="port")

args=parser.parse_args()



print(args)