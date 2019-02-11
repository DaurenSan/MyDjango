from django.http import HttpResponse
import qrcode

def index(request):
    # Create qr code instance
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
    )

    # The data that you want to store
    data = "The Data that you need to store in the QR Code"

    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    response = HttpResponse(content_type='image/png')
    img.save(response, "PNG")
    return response
