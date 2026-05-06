import qrcode
from IPython.display import display
import ipywidgets as widgets
from IPython.display import clear_output


text_box = widgets.Text(
    value='https://www.google.com',
    description='Link:',
    layout=widgets.Layout(width='500px')
)


button = widgets.Button(
    description='Generate QR',
    button_style='success'
)


output = widgets.Output()

def generate_qr(b):

    with output:

        clear_output()

        
        data = text_box.value

        qr = qrcode.QRCode(
            version=4,
            box_size=10,
            border=5
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        img.save("website_qr.png")

        display(img)


button.on_click(generate_qr)

display(text_box)
display(button)
display(output)
