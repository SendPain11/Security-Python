<!-- # Security-Python
This is my fundamental script code python for security reason to minimize risk in device -->

# 🔐 Security Toolbox

Sebuah toolkit keamanan Python yang berisi tiga alat keamanan praktis dalam satu skrip terpadu.

## 📋 Fitur

1. **Password Strength Checker** - Menganalisis kekuatan password
2. **Simple Port Scanner** - Memindai port pada host target
3. **File Integrity Checker** - Memverifikasi integritas file menggunakan hashing

## 🚀 Instalasi

Pastikan Python 3.x sudah terinstall di sistem Anda.

```bash
git clone https://github.com/username/security-toolbox.git
cd security-toolbox
```

## 📖 Penggunaan

### 1. Password Strength Checker

Menganalisis string password yang diberikan dan memberikan evaluasi kekuatannya.

#### Opsi 1: Dengan Argumen Langsung
```bash
python security_toolbox.py password "MyP@ssw0rd123"
```

#### Opsi 2: Dengan Input Tersembunyi (Disarankan)
Jalankan tanpa argumen untuk meminta input password tersembunyi, yang lebih aman di lingkungan terminal.

```bash
python security_toolbox.py password
```

---

### 2. Simple Port Scanner

Alat ini digunakan untuk memindai port tertentu pada host yang ditentukan untuk melihat apakah port tersebut terbuka.

#### Argumen:
| Argumen | Deskripsi | Wajib |
|---------|-----------|--------|
| `--host` | Alamat IP atau nama host target (misalnya, 127.0.0.1) | Ya |
| `--start` | Nomor port awal untuk dipindai | Ya |
| `--end` | Nomor port akhir untuk dipindai | Ya |

#### Contoh Penggunaan:
Memindai port 20 hingga 80 di localhost:

```bash
python security_toolbox.py scan --host 127.0.0.1 --start 20 --end 80
```

---

### 3. File Integrity Checker

Alat ini menggunakan fungsi hashing untuk memverifikasi apakah sebuah file telah diubah sejak hash awalnya dihitung dan disimpan.

#### Argumen:
| Argumen | Deskripsi | Wajib |
|---------|-----------|--------|
| `--file` | Nama path file yang akan diperiksa | Ya |
| `--mode` | `calculate` untuk membuat hash, atau `verify` untuk membandingkannya | Ya |

#### Langkah 1: Hitung dan Simpan Hash Awal
Ini akan membuat hash file dan menyimpannya (biasanya di file terpisah).

```bash
python security_toolbox.py integrity --file my_secret_file.txt --mode calculate
```

#### Langkah 2: Verifikasi Integritas
Ini akan menghitung hash file saat ini dan membandingkannya dengan hash yang disimpan.

```bash
python security_toolbox.py integrity --file my_secret_file.txt --mode verify
```

## 📝 Struktur Proyek

```
security-toolbox/
├── security_toolbox.py    # Skrip utama
├── README.md              # Dokumentasi ini
├── requirements.txt       # Dependensi (jika ada)
└── examples/              # Contoh file untuk testing
```

## 🛠️ Teknologi

- **Python 3.x** - Bahasa pemrograman utama
- **Socket** - Untuk port scanning
- **Hashlib** - Untuk fungsi hashing SHA-256
- **Getpass** - Untuk input password yang aman

## ⚠️ Catatan Keamanan

1. Alat ini ditujukan untuk **tujuan edukasi dan pengujian sah** saja
2. Dapatkan izin tertulis sebelum memindai sistem yang bukan milik Anda
3. Port scanner hanya cocok untuk penggunaan lokal atau jaringan pribadi
4. Simpan hash file dengan aman untuk memastikan integritas

## 🤝 Kontribusi

Kontribusi dipersilakan! Silakan buat pull request atau buka issue untuk fitur baru atau perbaikan bug.

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

## 🌟 Kesimpulan

Dengan satu skrip yang menangani tiga fungsi keamanan inti, Anda telah menunjukkan keahlian pemrograman Python dan pemahaman yang kuat tentang konsep keamanan!

Berkontribusi pada proyek ini akan membantu Anda mengembangkan keterampilan keamanan siber praktis sambil membangun portofolio yang mengesankan.