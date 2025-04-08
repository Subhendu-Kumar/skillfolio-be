import base64
import fitz  # type: ignore


def pdf_to_base64_images(file):
    images_base64 = []
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            pix = page.get_pixmap(dpi=300)
            img_bytes = pix.tobytes("png")
            b64_image = base64.b64encode(img_bytes).decode("utf-8")
            images_base64.append({"mime_type": "image/png", "data": b64_image})
    return images_base64
