import qrcode
import io

def generate_qr(value, latitude=None, longitude=None, photo=None, backcolor='white', vr=1):
    data = value
    qr_bytes_io = io.BytesIO()

    qr = qrcode.QRCode(
        version=vr,
        box_size=10,
        border=4,
        error_correction=qrcode.constants.ERROR_CORRECT_L
    )

    if latitude and longitude:
        location = f'geo:{latitude},{longitude}'
        qr.add_data(location)

    elif photo:
        pass

    else:
        qr.add_data(data)

    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color=backcolor)
    img.save(qr_bytes_io)
    qr_bytes_io.seek(0)

    return qr_bytes_io





