import tkinter as tk

def tampilkan_prediksi():
    label_luaran.config(text="Hasil Prediksi: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x550") 

label_judul = tk.Label(root, text="Aplikasi prediksi Prodi Pilihan", font=("Arial", 14, "bold"))
label_judul.pack(pady=15)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

entries = []
for i in range(1, 11):
    label_mapel = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i}:")
    label_mapel.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    entry_mapel = tk.Entry(frame_input, width=20)
    entry_mapel.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry_mapel)

btn_prediksi = tk.Button(root, text="Hasil Prediksi", command=tampilkan_prediksi)
btn_prediksi.pack(pady=20)
