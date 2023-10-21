import pandas as pd

class ExcelParser:
    def Parse(self, excel_path):
        # Load the xlsx file
        excel_data = pd.read_excel(excel_path)

        # Read the values of the file in the dataframe
        data = pd.DataFrame(excel_data, columns=['Шифр направления', 'Предыдущее место обучения', 'Любимые книги', 'Деятельность', 'Интересы', 'Сообщества и подписки'])

        # Print the content
        return data