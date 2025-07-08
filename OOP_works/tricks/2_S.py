# У вас есть класс Report, который:
# - хранит данные отчета,
# - генерирует его в PDF,
# - сохраняет на диск.
# Разделите этот класс на части, каждая из которых будет отвечать только за одну ответственность.
# class Report:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#     def generate_pdf(self):
#         print("PDF generated")
#     def save_to_file(self, filename):
#         print(f"Saved {filename}")


class StoreData:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class GeneratePDF:
    def generate_pdf(self):
        print("PDF generated")


class SaveToFile:        
    def save_to_file(self, filename):
        print(f"Saved {filename}")
