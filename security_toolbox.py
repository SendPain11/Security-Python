import argparse
import hashlib
import socket
import re
import os
from datetime import datetime

# --- CONFIGURATION ---
MIN_LENGTH = 8
REQUIRES_UPPER = True
REQUIRES_LOWER = True
REQUIRES_NUMBER = True
REQUIRES_SYMBOL = True
SYMBOL_REGEX = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
# --- END CONFIGURATION ---

# ==============================================================================
# 1. PASSWORD STRENGTH CHECKER
# ==============================================================================

def check_password_strength(password):
    """Menganalisis dan menilai kekuatan kata sandi."""
    score = 0
    feedback = []

    # 1. Panjang
    if len(password) >= MIN_LENGTH:
        score += 1
    else:
        feedback.append(f"[-] Panjang harus minimal {MIN_LENGTH} karakter.")

    # 2. Huruf Besar
    if REQUIRES_UPPER and any(c.isupper() for c in password):
        score += 1
    elif REQUIRES_UPPER:
        feedback.append("[-] Harus mengandung huruf kapital.")

    # 3. Huruf Kecil
    if REQUIRES_LOWER and any(c.islower() for c in password):
        score += 1
    elif REQUIRES_LOWER:
        feedback.append("[-] Harus mengandung huruf kecil.")

    # 4. Angka
    if REQUIRES_NUMBER and any(c.isdigit() for c in password):
        score += 1
    elif REQUIRES_NUMBER:
        feedback.append("[-] Harus mengandung angka.")

    # 5. Simbol
    if REQUIRES_SYMBOL and SYMBOL_REGEX.search(password):
        score += 1
    elif REQUIRES_SYMBOL:
        feedback.append("[-] Harus mengandung simbol.")

    max_score = 5 
    
    if score == max_score:
        print("\n[+] Hasil: Kuat (Strong).")
        return True
    
    print(f"\n[!] Hasil: Lemah/Sedang. Skor: {score}/{max_score}")
    print("Rekomendasi:")
    for item in feedback:
        print(item)
    return False

# ==============================================================================
# 2. SIMPLE PORT SCANNER
# ==============================================================================

def scan_port(host, port):
    """Mencoba koneksi ke port tertentu."""
    try:
        # Membuat socket baru (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Timeout 1 detik
        
        # Mencoba koneksi
        result = s.connect_ex((host, port))
        
        if result == 0:
            print(f"[+] Port {port} Terbuka (Open)")
        s.close()
    except socket.gaierror:
        print("[-] Hostname tidak bisa diselesaikan.")
    except socket.error:
        print("[-] Server tidak merespons.")

def run_port_scanner(host, start_port, end_port):
    """Menjalankan pemindaian port dalam rentang tertentu."""
    print(f"\n[*] Memindai {host} dari port {start_port} hingga {end_port}...")
    
    if start_port > end_port:
        start_port, end_port = end_port, start_port # Tukar jika rentang terbalik
        
    for port in range(start_port, end_port + 1):
        scan_port(host, port)
        
    print("[*] Pemindaian Selesai.")

# ==============================================================================
# 3. FILE INTEGRITY CHECKER
# ==============================================================================

HASH_FILE = "integrity_hashes.txt"

def calculate_file_hash(filepath):
    """Menghitung hash SHA256 dari sebuah file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Baca file per chunk agar efisien untuk file besar
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[-] Error: File '{filepath}' tidak ditemukan.")
        return None

def manage_integrity(filepath, mode):
    """Mengelola (menghitung atau memverifikasi) integritas file."""
    current_hash = calculate_file_hash(filepath)
    if not current_hash:
        return

    if mode == 'calculate':
        # Mode CALCULATE: Simpan hash baru
        with open(HASH_FILE, "a") as hf:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            hf.write(f"{filepath} | {timestamp} | {current_hash}\n")
        print(f"[+] Hash SHA256 untuk '{filepath}' berhasil disimpan ke {HASH_FILE}.")
        print(f"    Hash: {current_hash}")
        
    elif mode == 'verify':
        # Mode VERIFY: Verifikasi hash
        if not os.path.exists(HASH_FILE):
            print(f"[-] Error: File referensi hash '{HASH_FILE}' tidak ditemukan. Hitung hash terlebih dahulu.")
            return

        reference_hash = None
        with open(HASH_FILE, "r") as hf:
            for line in hf:
                if filepath in line:
                    parts = line.strip().split(' | ')
                    if len(parts) >= 3:
                        reference_hash = parts[2]
        
        if not reference_hash:
            print(f"[!] Peringatan: Hash referensi untuk '{filepath}' tidak ditemukan.")
            return

        print(f"[*] Hash Referensi: {reference_hash}")
        print(f"[*] Hash Saat Ini:  {current_hash}")
        
        if current_hash == reference_hash:
            print("\n[+] Integritas TERJAGA. File TIDAK diubah.")
        else:
            print("\n[!] PERINGATAN! Integritas TERKOMPROMI. File MUNGKIN telah diubah.")

# ==============================================================================
# MAIN PARSER (Antarmuka Command-Line)
# ==============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Cyber-Tools Essentials: Kumpulan Alat Keamanan Dasar (Python).",
        epilog="Gunakan -h atau --help pada setiap subcommand untuk detail lebih lanjut."
    )
    subparsers = parser.add_subparsers(dest="command")

    # --- Subparser 1: Password Strength ---
    parser_pass = subparsers.add_parser("password", help="Menilai kekuatan kata sandi.")
    parser_pass.add_argument("password", type=str, nargs='?', help="Kata sandi yang akan dinilai. Jika tidak diisi, akan meminta input.")

    # --- Subparser 2: Port Scanner ---
    parser_scan = subparsers.add_parser("scan", help="Memindai port terbuka pada host.")
    parser_scan.add_argument("--host", required=True, help="Target Hostname atau IP (e.g., 127.0.0.1)")
    parser_scan.add_argument("--start", type=int, default=1, help="Port awal untuk pemindaian (default: 1)")
    parser_scan.add_argument("--end", type=int, required=True, help="Port akhir untuk pemindaian.")

    # --- Subparser 3: Integrity Checker ---
    parser_integrity = subparsers.add_parser("integrity", help="Mengelola dan memverifikasi integritas file (SHA256).")
    parser_integrity.add_argument("--file", required=True, help="Jalur file yang akan diolah.")
    parser_integrity.add_argument("--mode", choices=['calculate', 'verify'], required=True, help="Mode operasi: 'calculate' (simpan hash) atau 'verify' (bandingkan hash).")

    args = parser.parse_args()

    if args.command == "password":
        pwd = args.password
        if not pwd:
            import getpass
            pwd = getpass.getpass("Masukkan Kata Sandi: ")
        check_password_strength(pwd)
        
    elif args.command == "scan":
        run_port_scanner(args.host, args.start, args.end)

    elif args.command == "integrity":
        manage_integrity(args.file, args.mode)
    
    elif not args.command:
        parser.print_help()