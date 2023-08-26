D=False
C='../client/dist'
from flask import Flask,render_template as E
from flask_bcrypt import Bcrypt as F
from flask_cors import CORS
from flask_migrate import Migrate as G
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy as H
from sqlalchemy import MetaData as I
import os
from dotenv import load_dotenv as J
J()
A=Flask(__name__,static_url_path='',static_folder=C,template_folder=C)
A.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URI')
A.config['SQLALCHEMY_TRACK_MODIFICATIONS']=D
A.json.compact=D
A.secret_key=os.environ.get('SESSION_KEY')
K=I(naming_convention={'ix':'ix_%(column_0_label)s','uq':'uq_%(table_name)s_%(column_0_name)s','ck':'ck_%(table_name)s_%(constraint_name)s','fk':'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s','pk':'pk_%(table_name)s'})
B=H(metadata=K)
L=G(A,B)
B.init_app(A)
M=F(A)
@A.route('/',defaults={'path':''})
@A.route('/<path:path>')
def N(path):return E('index.html')
O=Api(A)
CORS(A)