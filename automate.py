import os
import pandas as pd
import mac_imessage

def sendMessage(phone_number:str, message:str):
    mac_imessage.send_sms(message=message,phone_number=phone_number)

def automate(file_name: str, message: str):
    files_directory = "cli"
    file_path = os.path.join(files_directory, file_name)

    """ Check if the file exists """
    if os.path.exists(file_path):
        df = pd.read_excel(file_path, engine="openpyxl")
        if "CONTACT" not in df.columns:
            print("La colonne 'CONTACT' est absente du fichier.")
            exit(1)

        def send_wrapper(row):
            numero = row["CONTACT"]

            return sendMessage(str(numero), message)

        df['statut_envoi'] = df.apply(send_wrapper, axis=1)
        print(df[['CONTACT', 'statut_envoi']])

    else:
        print(f"File does not exist: {file_path}")
    exit(1)