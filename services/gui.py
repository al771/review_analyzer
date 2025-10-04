import tkinter as tk
from tkinter import filedialog, messagebox
from services.ninja_service import NinjaService
from services.twinword_service import TwinwordService
from services.comparison_service import compare_results


class SentimentGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Анализ тональности")
        self.root.geometry("600x500")

        self.service1 = NinjaService()
        self.service2 = TwinwordService()

        # Заголовок
        tk.Label(self.root, text="Анализ отзыва о фильме",
                 font=("Arial", 16)).pack(pady=20)

        # Поле ввода
        tk.Label(self.root, text="Введите отзыв:").pack()
        self.text_input = tk.Text(self.root, height=6, width=60)
        self.text_input.pack(pady=10)

        # Кнопки
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Анализировать",
                  command=self.analyze).pack(side=tk.LEFT, padx=5)

        tk.Button(button_frame, text="Загрузить файл",
                  command=self.load_file).pack(side=tk.LEFT, padx=5)

        # Результаты
        tk.Label(self.root, text="Результаты:",
                 font=("Arial", 12, "bold")).pack(pady=10)

        self.result1 = tk.Label(self.root, text="Анализатор 1: —",
                                font=("Arial", 10))
        self.result1.pack(pady=5)

        self.result2 = tk.Label(self.root, text="Анализатор 2: —",
                                font=("Arial", 10))
        self.result2.pack(pady=5)

        self.final_result = tk.Label(self.root, text="Итог: —",
                                     font=("Arial", 12, "bold"), fg="white")
        self.final_result.pack(pady=15)

    def analyze(self):
        text = self.text_input.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Ошибка", "Введите текст!")
            return

        try:
            # Анализируем
            result1 = self.service1.analyze_sentiment(text)
            result2 = self.service2.analyze_sentiment(text)
            comparison = compare_results(result1, result2)

            # Выводим результат 1
            if result1["success"]:
                text1 = f"Анализатор 1: {result1['sentiment'].upper()} (уверенность: {result1['score']:.2f})"
            else:
                text1 = f"Анализатор 1: Ошибка - {result1['error']}"
            self.result1.config(text=text1)

            # Выводим результат 2
            if result2["success"]:
                text2 = f"Анализатор 2: {result2['sentiment'].upper()} (уверенность: {result2['score']:.2f})"
            else:
                text2 = f"Анализатор 2: Ошибка - {result2['error']}"
            self.result2.config(text=text2)

            # Итог
            final_text = f"Итог: {comparison['final_sentiment'].upper()}"
            if comparison.get('conclusion_text'):
                final_text += f"\n{comparison['conclusion_text']}"
            self.final_result.config(text=final_text)

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if not file_path:
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()

            if content:
                self.text_input.delete("1.0", tk.END)
                self.text_input.insert("1.0", content)
                messagebox.showinfo("Успех", "Файл загружен!")
            else:
                messagebox.showwarning("Ошибка", "Файл пуст!")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")

    def run(self):
        self.root.mainloop()