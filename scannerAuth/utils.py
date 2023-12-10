from pyzbar.pyzbar import decode
from time import sleep 
from cryptography.fernet import Fernet
import json
import qrcode
from PIL import Image
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment

class Util:
    @staticmethod
    def generate_qr_code(data, file_name='qrcode.png'):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_name)

    @staticmethod
    def encrypt_data(data, key):
        cipher = Fernet(key)
        json_data = json.dumps(data)
        encrypted_data = cipher.encrypt(json_data.encode('utf-8'))
        return encrypted_data

    @staticmethod
    def decrypt_data(encrypted_data, key):
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
        return decrypted_data
    
    @staticmethod
    def create_excel_file(qr_data_list, excel_file_path):
        workbook = Workbook()
        sheet = workbook.active

        # Set column headers
        sheet['A1'] = 'QR ID'
        sheet['B1'] = 'QR Code File Name'

        # Set column widths
        sheet.column_dimensions['A'].width = 15
        sheet.column_dimensions['B'].width = 25

        # Set header alignment
        for cell in sheet[1]:
            cell.alignment = Alignment(horizontal='center')

        # Populate data
        for row_index, (qr_id, file_name) in enumerate(qr_data_list, start=2):
            sheet[f'A{row_index}'] = qr_id
            sheet[f'B{row_index}'] = file_name

        workbook.save(excel_file_path)








