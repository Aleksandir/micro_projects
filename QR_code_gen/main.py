import os

import qrcode

save_path = "/Users/aleks/Documents/_GIthub_Repositories/micro_projects/QR_code_gen"


def encode_text(text: str, save_path: str = save_path):
    img = qrcode.make(text)
    img.save(os.path.join(save_path, "QR.png"))


encode_text("")
