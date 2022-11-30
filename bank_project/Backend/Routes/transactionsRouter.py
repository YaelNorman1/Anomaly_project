from fastapi import APIRouter, HTTPException,Depends, Request
from Models.Transactions import Transactions
from auth.JWT_bearer import jwtBearer
from Schemas.Transaction import Transaction
import datetime

router = APIRouter(dependencies=[Depends(jwtBearer())])
model_transactions = Transactions()


@router.get('/balance', status_code=200)
async def get_balance(requset: Request):
    try:
        user_name = requset.headers.get('user')
        res = model_transactions.get_balance(user_name)
        return {"balance":res}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")


@router.get('/breakdown', status_code=200)
async def get_breakdown(requset: Request):
    try:
        user_name = requset.headers.get('user')
        res = model_transactions.get_breakdown(user_name)
        return {"breakdown":res}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")


@router.get('/transactions', status_code=200)
async def get_transactions(requset: Request):
    try:
        user_name = requset.headers.get('user')
        res = model_transactions.get_all(user_name)
        return {"transactions":res}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")



@router.post('/transactions', status_code=201)
async def post_transaction(transaction: Transaction):
    try:
        transaction.set_date(datetime.datetime.now())
        model_transactions.add(transaction)
        return {"result": list(transaction)}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")



@router.delete('/transactions/{id}', status_code=202)
def delete_transaction(id):
    try:
        id=int(id)
        res = model_transactions.delete(id)
        return {"result": "deleted"}
    except:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")
