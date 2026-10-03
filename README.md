# Persiapan LKSN AI
Belajar untuk persiapan LKSN-AI SMKN 1 Jakarta.

# Starter Guide
## Step 1: Download materi
- Klik disini untuk [Download ZIP](https://codeload.github.com/huzaifi18/LKS-AI/zip/master), atau
- Bagi yang familiar dengan git, boleh menggunakan clone
    ```
    git clone https://github.com/huzaifi/LKS-AI.git
    ```

## Step 2: Instalasi Miniconda
### **Windows user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Windows 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Windows-x86_64.exe)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya.

- Install miniconda
    - Ketika ada pilihan `install for`, pilih `Just Me (recommended)`
    - Untuk `Advanced Options`, silahkan centang `Register Anaconda as my default Python 3.7`
    - Tunggu hingga instalasi selesai

- Jalankan `Anaconda Prompt`

### **Mac user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Mac OS X 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-MacOSX-x86_64.pkg)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya

- Install miniconda
    - Install tanpa mengubah opsi apapun
    - Tunggu hingga instalasi selesai

- Jalankan terminal

### **Linux user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-x86_64.sh)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya.
    
- Install miniconda
    - jalankan terminal
    - Install miniconda menggunakan command berikut
        ```
        bash Miniconda3-py39_23.3.1-0-Linux-x86_64.sh
        ```
    - Ketik `yes` untuk agree dengan license nya, kemudian `yes` lagi untuk `prepend miniconda install location to PATH`
    - Tunggu hingga instalasi selesai
    
- hanya untuk memastikan, tutup dan buka terminal lagi

## Step 3: Instalasi Jupyter 
- Kita akan install 2 hal di base environment
    ```
    conda install -n base -c conda-forge jupyter nb_conda_kernels "notebook<6.0" 
    ```

## Step 4: Instalasi Environment
- Change directory `cd` ke folder kerja ini
    ```
    cd LKS-AI/
    ```
- Jalankan command ini untuk menginstall environment `LKS-AI`
    ```
    conda env create -f env_LKS-AI.yml
    ```

## Step 5: Memastikan environment terinstall dengan baik
- Jalankan command berikut untuk mengecek instalasi dan ikuti instruksi yang dihasilkan
    ```
    python check_installation.py
    ```
- Jika sudah aman, maka akan muncul keterangan berikut, dan kita bisa mulai belajar. Semangat!
    ```
    ✓ jupyter telah terinstall dengan baik
    ✓ nb_conda_kernels telah terinstall dengan baik
    ✓ Environment LKS-AI terdeteksi
    ✓ Package telah terinstall dengan baik di dalam environment jcopml
    ✓ Instalasi berjalan dengan baik. Selamat belajar!
    ```