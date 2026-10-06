from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API Integrasi Sistem - Tugas 1")

# Model
class MahasiswaCreate(BaseModel):
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str

class MahasiswaUpdate(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    ipk: Optional[float] = None
    semester: Optional[int] = None
    hobi: Optional[str] = None

# Database simulasi
mahasiswa_db: dict[int, dict] = {}
auto_id: int = 0

# Seed data
auto_id += 1
mahasiswa_db[auto_id] = {
    "id": auto_id,
    "nama": "Muhammad Wafalhana",
    "alamat": "Tingkir Tengah, Salatiga",
    "ipk": 3.9,
    "semester": 5,
    "hobi": "Push Magic Chess",
}

# GET semua
@app.get("/mahasiswa")
async def get_all():
    return list(mahasiswa_db.values())

# GET by ID
@app.get("/mahasiswa/{id}")
async def get_by_id(id: int):
    if id not in mahasiswa_db:
        raise HTTPException(404, "Data tidak ditemukan")
    return mahasiswa_db[id]

# POST
@app.post("/mahasiswa", status_code=201)
async def create(data: MahasiswaCreate):
    global auto_id
    auto_id += 1
    mahasiswa_db[auto_id] = {"id": auto_id, **data.model_dump()}
    return {"message": "Berhasil ditambahkan", "data": mahasiswa_db[auto_id]}

# PUT
@app.put("/mahasiswa/{id}")
async def update(id: int, data: MahasiswaUpdate):
    if id not in mahasiswa_db:
        raise HTTPException(404, "Data tidak ditemukan")
    for key, val in data.model_dump(exclude_none=True).items():
        mahasiswa_db[id][key] = val
    return {"message": "Berhasil diupdate", "data": mahasiswa_db[id]}

# DELETE
@app.delete("/mahasiswa/{id}")
async def delete(id: int):
    if id not in mahasiswa_db:
        raise HTTPException(404, "Data tidak ditemukan")
    deleted = mahasiswa_db.pop(id)
    return {"message": "Berhasil dihapus", "data": deleted}
