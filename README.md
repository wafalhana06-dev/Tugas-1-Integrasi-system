# 📚 Tugas 1 - Integrasi Sistem

## API CRUD Data Mahasiswa

API RESTful yang dibuat menggunakan **FastAPI** (Python) untuk mengelola data mahasiswa dengan operasi CRUD lengkap. Dokumentasi API otomatis tersedia melalui **Swagger UI**.

**Author:** Muhammad Wafalhana

---

## 📦 Data Object

| Field      | Tipe     | Keterangan              |
|------------|----------|-------------------------|
| `nama`     | string   | Nama lengkap mahasiswa  |
| `alamat`   | string   | Alamat tempat tinggal   |
| `ipk`      | float    | IPK (0.0 - 4.0)        |
| `semester` | integer  | Semester (1 - 14)       |
| `hobi`     | string   | Hobi mahasiswa          |

---

## 🔗 Endpoints

| Method   | Endpoint                 | Keterangan                         |
|----------|--------------------------|------------------------------------|
| `GET`    | `/`                      | Halaman utama API                  |
| `GET`    | `/mahasiswa`             | Ambil semua data mahasiswa         |
| `GET`    | `/mahasiswa/{id}`        | Ambil data mahasiswa berdasarkan ID|
| `POST`   | `/mahasiswa`             | Tambah data mahasiswa baru         |
| `PUT`    | `/mahasiswa/{id}`        | Update data mahasiswa              |
| `DELETE` | `/mahasiswa/{id}`        | Hapus data mahasiswa               |

---

## 🚀 Cara Menjalankan

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Jalankan Server

```bash
uvicorn main:app --reload
```

### 3. Buka Swagger UI

Setelah server berjalan, buka browser dan akses:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📝 Contoh Request

### POST - Tambah Mahasiswa

```json
{
  "nama": "Muhammad Wafalhana",
  "alamat": "Tingkir Tengah, Salatiga",
  "ipk": 3.9,
  "semester": 5,
  "hobi": "Push Magic Chess"
}
```

### PUT - Update Mahasiswa

```json
{
  "nama": "Muhammad Wafalhana",
  "ipk": 4.0
}
```

---

## 🛠 Tech Stack

- **Python 3.10+**
- **FastAPI** — Framework API modern dan cepat
- **Pydantic** — Validasi data otomatis
- **Uvicorn** — ASGI server
- **Swagger UI** — Dokumentasi API interaktif (bawaan FastAPI)
