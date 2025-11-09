from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db
from ..utils.imagekit_client import upload_file_to_imagekit

router = APIRouter(prefix="/api/v1/mil-symbols", tags=["mil-symbols"])

@router.get("/", response_model=List[schemas.MilSymbol])
def list_symbols(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_symbols(db, skip=skip, limit=limit)

@router.get("/{symbol_id}", response_model=schemas.MilSymbol)
def get_symbol(symbol_id: str, db: Session = Depends(get_db)):
    symbol = crud.get_symbol(db, symbol_id)
    if not symbol:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Symbol not found")
    return symbol

@router.post("/", response_model=schemas.MilSymbol, status_code=status.HTTP_201_CREATED)
def create_symbol(
    name: str = Form(...),
    code: str = Form(...),
    type: str | None = Form(None),
    description: str | None = Form(None),
    file: UploadFile | None = File(None),
    db: Session = Depends(get_db),
):
    icon_url = None
    if file:
        file_bytes = file.file.read()
        upload_resp = upload_file_to_imagekit(file_bytes, file.filename, folder="mil-symbols")
        icon_url = upload_resp.get('url')

    symbol_in = schemas.MilSymbolCreate(name=name, code=code, type=type, icon_url=icon_url, description=description)
    return crud.create_symbol(db, symbol_in)

@router.put("/{symbol_id}", response_model=schemas.MilSymbol)
def update_symbol(
    symbol_id: str,
    payload: schemas.MilSymbolUpdate,
    db: Session = Depends(get_db),
):
    return crud.update_symbol(db, symbol_id, payload)

@router.delete("/{symbol_id}")
def delete_symbol(symbol_id: str, db: Session = Depends(get_db)):
    return crud.delete_symbol(db, symbol_id)