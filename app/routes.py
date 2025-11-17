from fastapi import APIRouter, HTTPException
from typing import Dict
from .models import Entry, ModifyEntry
from .glossary import glossary

router = APIRouter()

# Получение списка всех терминов.
@router.get("/", response_model=Dict[str, Entry])
async def all_entries():
    return glossary

# Получение информации о конкретном термине по ключевому слову.
@router.get("/entry/{key}", response_model=Entry)
async def get_entry(key: str):
    entry = glossary.get(key)
    if not entry:
        raise HTTPException(status_code=404, detail=f"'{key}' не обнаружен в базе")
    return entry

# Добавление нового термина с описанием.
@router.post("/entry/{key}", response_model=Entry)
async def post_entry(key: str, entry: Entry):
    if key in glossary:
        raise HTTPException(status_code=400, detail=f"'{key}' уже есть в словаре")
    glossary[key] = entry
    return glossary[key]

# Обновление существующего термина.
@router.put("/entry/{key}", response_model=Entry)
async def modify_entry(key: str, entry: ModifyEntry):
    if key not in glossary:
        raise HTTPException(status_code=404, detail=f"'{key}' не обнаружен в базе")
    if entry.description is not None:
        glossary[key].description = entry.description
    if entry.reference is not None:
        glossary[key].reference = entry.reference
    return glossary[key]

# Удаление термина из глоссария.
@router.delete("/entry/{key}", response_model=Entry)
async def delete_entry(key: str):
    if key not in glossary:
        raise HTTPException(status_code=404, detail=f"'{key}' не обнаружен в базе")
    return glossary.pop(key)