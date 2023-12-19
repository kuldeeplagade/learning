from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp,make_playground_handler
from graphene import Schema,ObjectType,String,Int,List,Field,Mutation
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, URL,Column,Integer,String as saString,ForeignKey
from datetime import datetime,timedelta
import jwt
from graphql import GraphQLError

SECRET_KEY="Theater!"
ALGORITHM="HS256"
TOKEN_EXPIRATION_TIME_MINITES =15

url = URL.create(
    drivername="postgresql", 
    username='postgres',
    password='kuldeep',
    host='localhost',
    database='theater',
    port=5432
)

engine = create_engine(url) 
Base =declarative_base()

#models,Schema
class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True,autoincrement=True)
    username=Column(saString)
    password=Column(saString)
    

class Token(Base):
    __tablename__ = "user_sesssion"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    token = Column(saString)
    
        
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)


#Types
class UserObject(ObjectType):
   id=Int() 
   username=String()
   password=String() 
   
#queries 
class Query(ObjectType):
    users=List(UserObject)
    user =Field(UserObject, id=Int(required=True))
    @staticmethod
    def resolve_users(root,info):
        return  Session().query(User).all()
       
#mutation Add User
class AddUser(Mutation):
    class Arguments:
        #id=Int(required=True) 
        username=String(required=True)
        password=String(required=True)
        
    user =Field(lambda:UserObject)    
    
    @staticmethod
    def mutate(root,info,username,password):
        session=Session()
        user=User(username=username,password=password)
        session=Session()
        session.add(user)
        session.commit()
        session.refresh(user)
        return AddUser(user=user) 


#Genrate Token
def generate_token(password):
    #now+token lifespan
    expiration_time =datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_TIME_MINITES)
    
    payload={
        "sub":password,
        "exp":expiration_time
    }
    
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return token 


#varify password
def varify_password(pwd_hash,pwd):
    if pwd_hash == pwd:
        return "password matched !"
    else:
        raise GraphQLError("Invalid Password")

#login user
class LoginUser(Mutation):
    class Arguments:
        username=String(required=True)
        password=String(required=True)
    
    token=String()
    
    @staticmethod
    def mutate(root,info,username,password):
        session=Session()
        user=session.query(User).filter(User.username==username).first()
        
        if not user:
            raise GraphQLError("A username does not Exit")
          
        if varify_password(user.password,password):
            token=generate_token(username)
            
        # store this token to database
        
       
       
        return LoginUser(token=token)
    
# access_hope_page
class Homepage:
    class Arguments:
        user_name = String
        token = Int
    
class Mutation(ObjectType):
    add_user=AddUser.Field()
    login_user=LoginUser.Field()

schema=Schema(query=Query,mutation=Mutation)

app=FastAPI()
app.mount("/graphql--", GraphQLApp(
    schema=schema,
    on_get=make_playground_handler()
))


