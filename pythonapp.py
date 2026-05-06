import qrcode

upi_id = "8951136490-2@ibl"
bank_name = "Indian Post Payments Bank User"
upi_link = f"upi://pay?pa={upi_id}&pn={bank_name}"

qr = qrcode.make(upi_link)

qr.save("payment_qr.png")

display(qr)
display(qrcode.image)
