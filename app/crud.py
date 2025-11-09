from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def _ensure_icon_url_is_str(data: dict):
    """
    Convert any HttpUrl or non-str icon_url value to string, if present.
    Modifies dict in-place and returns it.
    """
    if "icon_url" in data and data["icon_url"] is not None:
        try:
            data["icon_url"] = str(data["icon_url"])
        except Exception:
            data["icon_url"] = None
    return data


def get_symbol(db: Session, symbol_id: str):
    return db.query(models.MilSymbol).filter(models.MilSymbol.id == symbol_id).first()


def get_symbol_by_code(db: Session, code: str):
    return db.query(models.MilSymbol).filter(models.MilSymbol.code == code).first()


def get_symbols(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MilSymbol).offset(skip).limit(limit).all()


def create_symbol(db: Session, symbol: schemas.MilSymbolCreate):
    payload = symbol.model_dump()
    _ensure_icon_url_is_str(payload)

    db_symbol = models.MilSymbol(**payload)
    try:
        db.add(db_symbol)
        db.commit()
        db.refresh(db_symbol)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Symbol code must be unique")
    return db_symbol


def update_symbol(db: Session, symbol_id: str, symbol_update: schemas.MilSymbolUpdate):
    db_symbol = get_symbol(db, symbol_id)
    if not db_symbol:
        raise HTTPException(status_code=404, detail="Symbol not found")

    update_data = symbol_update.model_dump(exclude_unset=True)
    _ensure_icon_url_is_str(update_data)

    for key, value in update_data.items():
        setattr(db_symbol, key, value)

    try:
        db.add(db_symbol)
        db.commit()
        db.refresh(db_symbol)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Symbol code must be unique")
    return db_symbol


def delete_symbol(db: Session, symbol_id: str):
    db_symbol = get_symbol(db, symbol_id)
    if not db_symbol:
        raise HTTPException(status_code=404, detail="Symbol not found")
    db.delete(db_symbol)
    db.commit()
    return {"detail": "Symbol deleted"}
