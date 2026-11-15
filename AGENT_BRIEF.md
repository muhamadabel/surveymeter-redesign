# AGENT_BRIEF.md: SurveyMETER Web Redesign

> Dokumen handoff dan instruksi arsitektur untuk Claude Code / Claude Desktop.
> Lead Orchestrator: Hermes Agent (review, quality gate, git push, deployment).
> Frontend Builder: Claude Code (deep coding, typography, micro-interactions, layout polish).

---

## 1. TUJUAN PROYEK & PEMBAGIAN PERAN

- **Proyek**: Redesain menyeluruh situs lembaga penelitian SurveyMETER (`https://surveymeter.org/id/node/11`).
- **Masalah Utama Web Eksisting**:
  - Berjalan di Drupal 8.5 (EOL 2021) dan PHP 7.2 (EOL 2020) di shared hosting Hostinger.
  - Sering mengalami White/Black Screen of Death (WSOD): *"Situs web mengalami kesalahan tak terduga"*.
  - Memakai tema sisa yayasan amal (`yg_charity`) dengan kode rusak dan inline style berantakan.
  - Layout mobile cacat: tombol hamburger ditaruh di tengah layar di bawah logo.
- **Misi**: Membangun antarmuka landing page berstandar institusi riset kelas dunia (setara Brookings, SMERU, RAND, CSIS) dengan gaya visual minimalis modern yang terinspirasi oleh **Osome Singapore** (`https://osome.com/sg/`).
- **Pembagian Tugas**:
  - **Claude Code**: Bertanggung jawab penuh atas implementasi frontend, pemilihan framework/bundler, penataan tipografi, spacing lapang, dan interaksi yang rapi.
  - **Hermes Agent**: Melakukan pre-commit review, memverifikasi ketiadaan AI slop dan em-dash, menjalankan uji responsivitas browser, serta melakukan commit, push ke Git remote, dan deploy ke Vercel/Cloudflare.

---

## 2. ATURAN KERJA & STANDAR NON-NEGOSIABEL (ANTI-SLOP)

Abel memiliki aturan spesifik yang wajib dipatuhi:

1. **Dilarang Keras Menggunakan Tanda Pisah Em-Dash**:
   - Jangan gunakan karakter em-dash di seluruh teks, copy, komentar kode, maupun dokumen ini.
   - Gunakan tanda pisah biasa (`-`), tanda kurung `(...)`, titik dua, atau struktur kalimat langsung.
2. **Anti AI-Slop (No Fluff, No Buzzwords)**:
   - Buang kata-kata klise AI (*delve, harness, seamless, cutting-edge, komprehensif, terdepan, mutakhir*).
   - Tulis copy yang pendek, padat, dan faktual.
   - Hindari tumpukan badge/chip berlebihan di atas kartu atau judul section.
   - Hindari kartu yang dipenuhi checklist centang (`✓`) seragam ala template landing page SaaS.
3. **Landing Page Minimalis**:
   - Sedikit section (maksimal 4-5 section utama), whitespace lapang, headline tajam.
   - "Makin AI" = terlalu banyak copy, teks deskripsi panjang, section pengisi template.
   - Berikan ruang bernapas yang lega antar section (`padding: 96px 0` atau lebih).
4. **Dilarang Menggunakan Emoji**:
   - Nol emoji pada UI, tombol, chip, maupun teks konten.
5. **Clean Light Mode Permanen**:
   - Kanvas utama: Warm ecru / parchment (`#FAF8F5` atau `#FAF7F2`).
   - Kartu / kontainer: Putih bersih (`#FFFFFF`) dengan border halus (`#E6E1D8`).
   - Teks utama: Charcoal gelap pekat (`#141A17` atau `#1A211E`), bukan abu-abu tipis.
   - Aksen resmi: Hijau botani SurveyMETER (`#0E5E3A` / hover `#09472B`) dipadu sage/mint lembut (`#EBF7EE`).

---

## 3. REFERENSI DESAIN: OSOME SINGAPORE (`https://osome.com/sg/`)

Elemen visual Osome yang harus diadopsi:
- **Tipografi Hybrid**: Perpaduan sans-serif geometris modern (Inter / Plus Jakarta Sans / Geist) untuk teks teknis dan UI, dipadu dengan font serif editorial (Newsreader / Instrument Serif / Georgia italic) untuk kata kunci penekanan pada headline.
- **Pill Geometry**: Sudut membulat penuh (`border-radius: 9999px`) pada tombol utama, tag klasifikasi, toggle bahasa, dan search input.
- **Top Announcement Strip**: Bar notifikasi ringkas di paling atas layar dengan latar hijau kontras tinggi untuk pengumuman rilis data terbaru.
- **Whitespace & Breathing Room**: Elemen tidak dijejali teks panjang. Biarkan ruang kosong menegaskan wibawa akademik lembaga.
- **Kartu Produk / Dataset Terstruktur**: Layout data yang rapi dengan spesifikasi format (STATA, SPSS), cakupan sampel, tahun rilis, dan tombol aksi langsung.

---

## 4. DATA RIIL & FAKTA SURVEYMETER (SUMBER KEBENARAN)

Gunakan hanya data terverifikasi berikut (jangan mengarang data baru):

### A. Profil Lembaga & Sejarah
- **Nama Resmi**: PT SurveyMETER (sebelumnya Yayasan SurveyMETER didirikan 20 Februari 2002 di Yogyakarta).
- **Kepanjangan**: *Survey, Measurement, Training, and Research*.
- **Akar Sejarah**: Berasal dari tim peneliti lapangan yang berpengalaman lebih dari 15 tahun mengelola pengumpulan data *Indonesia Family Life Survey* (IFLS) bersama RAND Corporation.
- **Tonggak Penting**:
  - 2002: Pendirian lembaga di Yogyakarta.
  - 2011: Penguatan fokus sebagai Lembaga Penelitian dan Advokasi Kebijakan Publik.
  - 2020: Transformasi menjadi PT SurveyMETER untuk memperluas kemitraan riset internasional.
- **Kepemimpinan**:
  - Bondan S. Sikoki (Direktur Eksekutif 2002-2012)
  - Dr. Ir. Ni Wayan Suriastini, M.Phil (Direktur Eksekutif 2012-2024)
  - Dr. Cecep Sukria Sumantri (Direktur Eksekutif sejak 20 Februari 2024)

### B. Mitra Strategis Internasional & Nasional
- **Lembaga Donor & Multilateral**: The World Bank, Asian Development Bank (ADB), UNICEF, UNDP, AUSAID / PROSPERA.
- **Institusi Riset & Universitas Global**: RAND Corporation, Abdul Latif Jameel Poverty Action Lab (J-PAL), Innovations for Poverty Action (IPA), Duke University, Australian National University (ANU), University of Melbourne, University of Sydney, UCLA, Hitotsubashi University.
- **Kementerian & Lembaga Pemerintah**: Bappenas RI, TNP2K, Kementerian Kesehatan RI, BNPB, Kementerian Pendidikan RI, Pemerintah Daerah D.I. Yogyakarta.

### C. Dataset Publik Utama
1. **IFLS East (Survei Aspek Kehidupan Rumah Tangga Indonesia Timur)**:
   - Survei panel multi-topik kondisi kehidupan rumah tangga dan komunitas di 7 provinsi Indonesia Timur.
   - Format: STATA (.dta), SPSS, Codebook PDF.
   - Status: Akses terbuka dengan registrasi peneliti.
2. **ILAS 2023 (Indonesia Longitudinal Aging Survey)**:
   - Studi longitudinal penuaan penduduk, kesehatan fisik dan mental, jejaring keluarga, serta kesiapan ekonomi lansia di Indonesia bekerja sama dengan Asian Development Bank (ADB).
   - Format: Dataset mikro, kuesioner, modul pengasuh.
   - Status: Rilis 2024.
3. **Studi Pemulihan Pasca Tsunami Aceh (STAR / Longitudinal Panel)**:
   - Pemantauan jangka panjang pemulihan ekonomi, relokasi perumahan, dan ketahanan sosial pasca tsunami bersama Duke University dan World Bank.
   - Format: Data panel multi-putaran.

### D. Publikasi Terpilih (Aset Cover Tersedia Lokal di Repo)
- `pub_repro.jpg`: *Studi Kualitatif Persepsi Pendidikan Seks & Kesehatan Reproduksi Remaja di Yogyakarta* (14 Okt 2024) - Peneliti: Sikoki, Larastiti, Suriastini, Pujiastuti.
- `pub_irsa.jpg`: *COVID-19 Disruption and Regional Development in Small Island Economies* (17 Jul 2024) - IRSA Conference 2024.
- `pub_adb_aging.jpg`: *Aging Well in Asia: Asian Development Policy Report 2024* (15 Mei 2024) - Kolaborasi bersama Asian Development Bank.
- `pub_nbs.jpg`: *Mengangkat Kerja Layak bagi Lanjut Usia yang Menekuni Solusi Berbasis Alam di Indonesia* (31 Mei 2024).
- `pub_aceh.jpg`: *Mengukur Pemulihan Bencana: Pelajaran Tahap Awal Wilayah Pasca Tsunami Aceh* (Desember 2023) - Jurnal Sustainability.

### E. Alamat & Kontak Resmi Kantor
- **Kantor Utama**: Jl. Jenengan Raya No. 109, Maguwoharjo, Depok, Sleman, D.I. Yogyakarta 55282.
- **Telepon**: +62 274 4477-464
- **Fax**: +62 274 4477-004
- **Email**: `sm@surveymeter.org`
- **Sosial Media**: Twitter/X `@SurveyMETER_Id`, Facebook `Surveymeter`.

---

## 5. STRUKTUR & BLUEPRINT HALAMAN (MAKSIMAL 5 SECTION)

Buat struktur halaman yang ramping dan langsung ke inti:

1. **Top Ribbon & Sticky Navbar (Tinggi 68-72px)**:
   - Ribbon: *"Dataset Longitudinal Penuaan Penduduk (ILAS 2023) telah dirilis. Akses Repositori Data ->"*
   - Navbar: Logo vektor SurveyMETER di kiri, 4 menu navigasi di tengah (`Fokus Riset`, `Data Publik`, `Publikasi`, `Tentang Lembaga`), switch bahasa `[ ID | EN ]` dan tombol aksi pill *"Permohonan Data"*.
2. **Hero Section (Editorial Authority & Proof Strip)**:
   - Headline: *"Riset Kebijakan Berbasis Bukti untuk [Pembangunan Berkelanjutan]"* (kata kedua memakai font serif miring).
   - Subheadline (maksimal 2 kalimat): Menjelaskan kiprah SurveyMETER dalam pengumpulan data longitudinal dan evaluasi kebijakan publik sejak 2002.
   - Dua CTA: *"Jelajahi Data Publik ->"* (primary solid) dan *"Katalog Publikasi"* (secondary subtle outline).
   - Proof Strip (4 kolom angka tegas tanpa kotak berat):
     - `22+ Tahun` Dedikasi Riset Lapangan
     - `35+ Mitra` Lembaga Internasional & Kementerian
     - `100+ Survei` Longitudinal & Rumah Tangga
     - `100% Data Primer` Terverifikasi
3. **Mitra Kebijakan & Akademik (Dignified Partner Ledger)**:
   - Baris logo / nama institusi monokrom elegan: World Bank, ADB, Bappenas, RAND, J-PAL, UNICEF, TNP2K, Kemenkes, ANU, UGM.
4. **Portal Data Publik (Fitur Utama)**:
   - Input pencarian dataset instan.
   - Kartu katalog 3 dataset riil (IFLS East, ILAS 2023, Aceh Recovery Panel) dengan metadata rapi (Cakupan, Format STATA/SPSS, Tombol Unduh Metadata, Tombol Minta Akses).
   - Mengklik *"Minta Akses"* membuka modal bersih untuk mengisi nama, instansi, email, dan tujuan riset.
5. **Publikasi & Policy Briefs Pilihan**:
   - Tab filter topik ringkas (Semua, Penuaan, Kesehatan, Ekonomi).
   - Grid kartu dengan cover buku asli, tanggal publikasi, nama peneliti/jurnal, dan tautan unduh ringkasan.
6. **Footer Resmi & Footer Ledger**:
   - Alamat lengkap Sleman/Yogyakarta, kontak telepon, email, legalitas Kemenkumham, serta tautan arsip.

---

## 6. INVENTARIS ASET DI DIREKTORI INI

Semua aset lokal ada di `assets/img/`:
- `surveymeter-logo.png`: Logo resmi RGBA asli (336x62).
- `ilas-wide.jpg`: Potongan lebar foto dari sampul laporan ILAS (`slai_adb.png`, 682x226), dipakai di beranda.
- `photo-*.jpg`: foto kegiatan dari slider situs lama (APRC 2024, tim, pelatihan 2022 dan 2024).
- `arsip/`: 798 gambar artikel hasil migrasi (lihat bagian 8).
- `pub_repro.jpg`, `pub_irsa.jpg`, `pub_adb_aging.jpg`, `pub_nbs.jpg`, `pub_aceh.jpg`: File gambar cover publikasi asli.
- `slai_adb.png`, `peta.png`: Dokumentasi dan peta survei IFLS East.

---

## 7. CHECKLIST ACCEPTANCE CRITERIA (QUALITY GATE)

Sebelum Claude Code menyatakan tugas selesai untuk direview Hermes:
- [x] Nol karakter tanda pisah em-dash di seluruh kode HTML, CSS, JS, dan copy.
- [x] Nol emoji pada antarmuka aplikasi.
- [x] Tidak ada tumpukan badge/chip berlebihan dan tidak ada daftar centang (`✓`) seragam.
- [x] Teks deskripsi pendek, padat, to-the-point, dan bebas dari kata-kata AI generik.
- [x] Menggunakan palet warm ecru (`#FAF8F5`), putih bersih, dan hijau botani (`#0E5E3A`).
- [x] Tipografi menggunakan perpaduan sans-serif bersih dan aksen serif miring editorial.
- [x] Seluruh tombol dan kontrol interaktif (modal permohonan data, filter pencarian) berfungsi normal.
- [x] Tata letak responsif mulus dari layar ponsel (375px) hingga desktop lebar (1440px).
- [x] File deliverable siap diuji langsung di browser lokal.

---

## 8. STATUS IMPLEMENTASI (Claude Code, 15 Nov 2026, migrasi penuh situs lama)

Branch: `feat/landing-page`. Situs statis multi-halaman (ID + EN), dibangun oleh generator Python tanpa dependensi. Hasil build ikut di-commit, jadi Vercel/Cloudflare cukup menyajikan folder repo apa adanya (`vercel.json`: `outputDirectory: "."`, `cleanUrls: true`).

Atas permintaan pihak SurveyMETER, situs baru memuat informasi selengkap surveymeter.org lama: semua menu, semua daftar, dan isi setiap artikel. Batas "maksimal 5 section" di bagian 5 tidak berlaku lagi. Versi landing satu halaman sebelumnya disimpan di `legacy/v1-bento/`, `legacy/v2-portal/`, `legacy/v3-profil/`.

### Cara kerja
- Sumber yang diedit:
  - `content/site.json`: konten hasil migrasi.
  - `content/images.json`: peta URL gambar lama ke file lokal.
  - `content/home_en.json`: teks beranda versi EN.
  - `templates/home.html`: isi beranda.
  - `styles.css`, `main.js`.
  - `tools/build.py`: menu, label UI, halaman khusus.
- Build: `python3 tools/build.py`. Cek link internal: `python3 tools/check_links.py` (harus 0 rusak).
- Jangan edit file HTML hasil build langsung (`index.html`, `en/`, `baca/`, `tentang/`, dst.), karena akan tertimpa saat build berikutnya.
- Setiap ubah CSS/JS, naikkan `ASSET_V` di `tools/build.py` (cache busting).
- Generator otomatis mengganti em-dash dan en-dash di konten lama dengan tanda hubung biasa.

### Struktur URL (ID di `/`, EN di `/en/`)
- Tentang: `tentang/sasaran`, `tentang/mitra`, `tentang/profil`, `tentang/struktur`, `tentang/visi-misi`, `tentang/kemampuan`.
- Kegiatan: `kegiatan/evaluasi-dampak`, `kegiatan/studi-kebijakan`, `kegiatan/pendampingan`, `kegiatan/pelatihan`, `kegiatan/pengelolaan-pengetahuan`, `kegiatan/penelitian-ilmiah`, `kegiatan/kajian`.
- Publikasi: `publikasi` (semua, berhalaman), `publikasi/working-paper`, `publikasi/policy-brief`, `publikasi/buku`, `publikasi/artikel`, `publikasi/laporan-penelitian`, `publikasi/laporan-tahunan`.
- Data publik: `data/ifls-east`, `data/star`, `data/ilas`.
- Kelompok kerja: `kelompok-kerja/lansia/{survei,pendampingan,publikasi}`, `kelompok-kerja/stunting/{survei,publikasi}`, `kelompok-kerja/silani`, `kelompok-kerja/ltc`.
- Karir per tahun: `karir/2019` sampai `karir/2024`.
- Lainnya: `berita` (berhalaman, 18 per halaman), `kontak`, `cari` (pencarian di browser dari `search-index-{id,en}.json`).
- Artikel: `baca/<slug>` (ID) dan `en/read/<slug>` (EN).
- `sitemap.xml` dan `404.html` dibuat otomatis.

### Hasil migrasi (diambil 15 Nov 2026)
- 472 artikel ID dan 428 artikel EN, masing-masing lengkap dengan tanggal, tipe, penulis, kata kunci, lokasi, dan isi.
- 439 berita ID, 22 buku dengan link unduh Google Drive, dan semua daftar kegiatan, publikasi, kelompok kerja, serta karir.
- Halaman "Sasaran dan Lingkup" dan "Kemampuan dan Pengalaman" di situs lama hanya berupa gambar. Isinya ditulis ulang sebagai HTML: fokus isu per periode dan linimasa perjalanan.
- Daftar karir EN 2020-2024 kosong di situs lama, jadi diisi dengan versi ID. Halaman STAR versi ID error, jadi memakai versi EN.
- Sekitar 46 artikel tidak bisa diambil karena server lama selalu mengembalikan HTTP 500 untuk halaman itu. Item-nya disembunyikan dari daftar supaya tidak ada link mati. Daftar lengkapnya ada di log crawl.
- "Semua publikasi" dibangun dari gabungan semua kategori publikasi, karena beberapa halaman paginasi di situs lama juga selalu error.
- Gambar: 798 file diunduh dari situs lama atas izin Abel, dikecilkan menjadi JPEG maksimal 1000 px di `assets/img/arsip/` (sekitar 91 MB). Gambar di folder `/uploads/` lama sudah 404 di situs lama sendiri, jadi dihapus dari isi artikel.
- File dokumen (PDF di `sites/default/files`, `media/*/download`) dan halaman data ILAS (`surveymeter.org/ilas/`) masih ditautkan ke server lama.

### Penting sebelum ganti domain
- Unduhan PDF dan portal data ILAS masih di server Drupal lama. Sebelum surveymeter.org dipindah ke situs baru, server lama harus tetap hidup di subdomain (misalnya `arsip.surveymeter.org`), atau file-file itu dipindah dan link-nya diganti di `content/site.json`.
- Siapkan redirect dari URL lama (`/id/read/...`, `/id/post/...`, `/en/...`) ke URL baru. Generator sudah punya pemetaannya (`post_path`, `OLD_SECTION`), tinggal diekspor ke `vercel.json` kalau dibutuhkan.

### Desain
- Tema terang: putih + krem `#F6F4EF`, hijau `#0E5E3A`, blok `#0A3322`, aksen lime `#C6E57A`. Font Plus Jakarta Sans.
- Mega menu desktop meniru struktur menu lama (Tentang, Kegiatan, Publikasi, Kelompok kerja, Karir), lalu Berita dan Cari. Di bawah 1100 px berubah jadi menu akordeon.
- Halaman daftar memakai kartu bergambar dan sidebar "Di bagian ini" + "Berita terbaru". Daftar publikasi memakai sampul tegak.
- Semua tombol dan link minimal 44 x 44 px. Tanpa geser horizontal di 360 px. Kontras teks lolos 4.5:1.

### Belum ada (butuh data dari SurveyMETER)
- Foto pengurus (struktur organisasi sekarang memakai inisial).
- Logo resmi mitra, nomor SK Kemenkumham.
- Terjemahan EN untuk artikel yang hanya ada dalam bahasa Indonesia (sekarang ditautkan ke versi ID).
