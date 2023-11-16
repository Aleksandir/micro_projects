import os

import qrcode

save_path = "/Users/aleks/Documents/_GIthub_Repositories/micro_projects/QR_code_gen"


def encode_text(text: str):
    return qrcode.make(text)


img = encode_text("I love you most! <3")
img.save(os.path.join(save_path, "QR.png"))
