# ETL Pipeline Project

## Deskripsi
Proyek ini merupakan implementasi ETL (Extract, Transform, Load) menggunakan Apache Airflow untuk mengekstrak data dari dua sumber berbeda: `sales_data.csv` dan `customers_data.json`. Proyek ini bertujuan untuk memberikan pemahaman praktis tentang bagaimana menggunakan Airflow untuk mengelola alur kerja ETL dan menyimpan hasilnya dalam database SQLite.

## Teknologi yang Digunakan
- Python
- SQL
- Apache Airflow
- SQLite
- DBeaver (untuk mengelola database SQLite)

## Cara Menjalankan Proyek
1. **Persyaratan Sistem:**
   - Pastikan Anda memiliki Docker dan Docker Compose terinstal.
   - Kloning repositori ini ke mesin lokal Anda.

2. **Instalasi:**
   - Navigasikan ke direktori proyek Anda.
   - Jalankan perintah berikut untuk memulai Airflow:
     ```bash
     docker-compose up -d
     ```
   - Tunggu hingga semua kontainer siap.

3. **Menjalankan DAG:**
   - Akses antarmuka Airflow melalui browser di `http://localhost:8080`.
   - Trigger DAG untuk file CSV dengan konfigurasi:
     ```json
     {
         "source_type": "csv"
     }
     ```
   - Trigger DAG untuk file JSON dengan konfigurasi:
     ```json
     {
         "source_type": "json"
     }
     ```

## Contoh Penggunaan
Setelah menjalankan DAG untuk kedua file, Anda dapat melihat hasilnya di database SQLite menggunakan DBeaver. Screenshot berikut menunjukkan hasil dari proses ekstraksi:

1. ![Screenshot Pengaturan DAG](images/1_Screenshot_Pengaturan_DAG.png)
   - Menunjukkan semua konfigurasi yang terkait dengan DAG, termasuk nama DAG dan parameter lainnya.

2. ![Screenshot Parameter Konfigurasi untuk CSV](images/2_Screenshot_Parameter_Konfigurasi_untuk_CSV.png)
   - Menampilkan pengaturan parameter untuk ekstraksi file `sales_data.csv`.

3. ![Screenshot DAG Run untuk CSV](images/3_Screenshot_DAG_Run_untuk_CSV.png)
   - Status run DAG saat menjalankan file CSV.

4. ![Screenshot Graf DAG untuk CSV](images/4_Screenshot_Graf_DAG_untuk_CSV.png)
   - Visualisasi dari alur kerja DAG untuk file CSV.

5. ![Screenshot Hasil di SQLite Setelah CSV](images/5_Screenshot_Hasil_di_SQLite_Setelah_CSV.png)
   - Hasil ekstraksi data dari `sales_data.csv` di database SQLite.

6. ![Screenshot Parameter Konfigurasi untuk JSON](images/6_Screenshot_Parameter_Konfigurasi_untuk_JSON.png)
   - Menampilkan pengaturan parameter untuk ekstraksi file `customers_data.json`.

7. ![Screenshot DAG Run untuk JSON](images/7_Screenshot_DAG_Run_untuk_JSON.png)
   - Status run DAG saat menjalankan file JSON.

8. ![Screenshot Graf DAG untuk JSON](images/8_Screenshot_Graf_DAG_untuk_JSON.png)
   - Visualisasi dari alur kerja DAG untuk file JSON.

9. ![Screenshot Hasil di SQLite Setelah JSON](images/9_Screenshot_Hasil_di_SQLite_Setelah_JSON.png)
   - Hasil ekstraksi data dari `customers_data.json` di database SQLite.

## Kesimpulan
Proyek ini menunjukkan bagaimana Airflow dapat digunakan untuk mengotomatiskan proses ETL dari berbagai sumber data. Dengan mengonfigurasi DAG dan menggunakan parameter, Anda dapat dengan mudah mengekstrak, mentransformasi, dan memuat data ke dalam database, yang merupakan keterampilan penting dalam pengembangan data engineering.
