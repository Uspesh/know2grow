from fastapi import UploadFile
import os


class FileWork:

    def create_file(self, file: UploadFile, filename: str = ''):
        if not filename:
            file_path = f'./media/{file.filename}'
        else:
            file_path = f'./media/{filename}'

        with open(file_path, 'wb') as f:
            f.write(file.file.read())

        return 200

    def get_file(self, filename):
        file_path = f'./media/{filename}'
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                file = f.read()
            return file
        else:
            return 'Такого файла нет.'

    def delete_file(self, filename):
        file_path = f'./media/{filename}'
        if os.path.isfile(file_path):
            os.remove(file_path)
            return 200
        else:
            return 'Такого файла нет.'