import qrcode


print("===== Wi-Fi QR Generator =====")

ssid = input("Enter Wi-Fi name (SSID): ")
password = input("Enter Wi-Fi password: ")
security = input("Enter security type (WPA/WEP/nopass): ").upper()

wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(wifi_data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")

filename = "wifi_qr.png"
image.save(filename)

print("\nQR code generated successfully!")
print("Saved as:", filename)
