OTP (One Time Pad) šifrēšana un OTP ģenerēšana, kā arī dešifrēšana padodot šifrēto failu un OTP

Lietošana:

- Šifrēšanai:

python ApplCr_OTP_Guntis_Valters.py encrypt <šifrējamais fails> <otp fails> <šifrētais fails - rezultāts>

Piem: python ApplCr_OTP_Guntis_Valters.py encrypt plain.txt file.otp file.crypto

- Dešifrēšanai:

python ApplCr_OTP_Guntis_Valters.py decrypt <šifrētais fails> <otp fails> <dešifrētais fails - rezultāts>

Piem: python ApplCr_OTP_Guntis_Valters.py decrypt file.crypto file.otp plain_out.txt