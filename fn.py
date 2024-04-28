import qrcode
import io


def generate_qr(value, latitude=None, longitude=None):
    if latitude and longitude:
        location = f'geo:{latitude},{longitude}'
    data = value.text
    qr_bytes_io = io.BytesIO()

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
        error_correction=qrcode.constants.ERROR_CORRECT_L
    )
    if latitude and longitude:
        location = f'geo:{latitude},{longitude}'
        qr.add_data(location)
    else:
        qr.add_data(data)

    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(qr_bytes_io)
    qr_bytes_io.seek(0)

    return qr_bytes_io
