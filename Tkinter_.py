import tkinter as tk

def tampilkan_prediksi():
    label_luaran.config(text="Hasil Prediksi: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x550") 

label_judul = tk.Label(root, text="Aplikasi prediksi Prodi Pilihan", font=("Arial", 14, "bold"))
label_judul.pack(pady=15)
