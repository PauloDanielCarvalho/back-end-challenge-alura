
import os
import datetime
from fastapi import FastAPI,File,UploadFile,HTTPException,status
import csv
import shutil
from schemas.schemas import  TransacoesInput,ImportacaoRealizadasInput
from repository.trasacao_repository import TransacaoRepository
from router.user import user_router
from typing import List

app= FastAPI()
app.include_router(user_router, prefix='/user')

@app.post("/files_csv/")
async def create_file(id:int,file_csv: UploadFile = File(...)):
    read_file=await file_csv.read()
    with open(file_csv.filename,"wb") as new_file:
        new_file.write(read_file)
        new_file.close()
    shutil.move(file_csv.filename,"./static")
    with open(f'./static/{file_csv.filename}','r') as file:
        read_csv=csv.reader(file, delimiter=',')
        try:
            first_index = None
            for i in read_csv:
                if not(first_index):
                    first_index=i[7][:10]

                if first_index==i[7][:10] and '' not in i:
                    valor=float(i[6])
                    data_hora=datetime.datetime(int(i[7][:4]),int(i[7][5:7]),int(i[7][8:10]),int(i[7][11:13]),int(i[7][14:16]),int(i[7][17:]))
                    transacao=TransacoesInput(banco_origem=i[0],agencia_origem=int(i[1]),conta_origem=i[2],banco_destino=i[3],agencia_destino=int(i[4]),conta_destino=i[5],valor_transação=valor,data_hora=data_hora)
                    transacao=await TransacaoRepository().save_transacao(transacao)
                    await TransacaoRepository().date_transacao(ImportacaoRealizadasInput(data_transacao=data_hora,data_importacao=datetime.datetime.today(),id_user=id,id_transaçoes=transacao.id))
    
        except Exception as erroo:
            os.remove(f'./static/{file_csv.filename}') 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(erroo))
             
        os.remove(f'./static/{file_csv.filename}')          
    return file_csv.filename

@app.get('/get_dates_transacoes',response_model=List[ImportacaoRealizadasInput])
async def get_dates_transacoes():
    return await TransacaoRepository().get_date_transacao()

@app.post('/teste/')
async def teste(id:str,file_csv: UploadFile = File(...)):
    print(id)
    test=await file_csv.read()
    return test