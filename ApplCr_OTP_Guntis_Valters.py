import sys
import os

def encrypt_file(input_file_name, otp_file_name, out_file_name):
    with open(input_file_name, 'rb') as f:
        data = f.read()

    # izmanto os finkciju urandom, kas ir drošāks nekā pseido-random ģenerators, lai ģenerētu otp ar garumu, kas vienāds ar ievaddatiem
    otp = os.urandom(len(data))
    # saglabā OTP
    with open(otp_file_name, 'wb') as f:
        f.write(otp)

    # šifrēšana izmantojot XOR ievaddati, otp
    encrypted_data = bytes(a ^ b for a, b in zip(data, otp))
    with open(out_file_name, 'wb') as f:
        f.write(encrypted_data)

    print(f"Success: Faila garums un ģenerētā OTP garums: {len(data)}")


def decrypt_file(input_file_name, otp_file_name, out_file_name):
    with open(input_file_name, 'rb') as f:
        data = f.read()

    # ielādē otp
    with open(otp_file_name, 'rb') as f:
        otp = f.read()

    # dešifrēšana izmantojot XOR ievaddati, otp
    decrypted_data = bytes(a ^ b for a, b in zip(data, otp))

    with open(out_file_name, 'wb') as f:
        f.write(decrypted_data)

    print(f"Success!")


def print_help():
    """OTP (One Time Pad) šifrēšana un OTP ģenerēšana, kā arī dešifrēšana padodot šifrēto failu un OTP"""
    print("Lietošana:")
    print("Šifrēšanai:")
    print("  python ApplCr_OTP_Guntis_Valters.py encrypt <šifrējamais fails> <otp fails> <šifrētais fails - rezultāts>")
    print("  Piem: python ApplCr_OTP_Guntis_Valters.py encrypt plain.txt file.otp file.crypto")
    print("Dešifrēšanai:")
    print("  python ApplCr_OTP_Guntis_Valters.py decrypt <šifrētais fails> <otp fails> <dešifrētais fails - rezultāts>")
    print("  Piem: python ApplCr_OTP_Guntis_Valters.py decrypt file.crypto file.otp plain_out.txt")

def main():
    if len(sys.argv) != 5:
        print(f"Kļūda: nav norādīti pareizi / visi parametri")
        print_help()
        sys.exit(1)

    mode = sys.argv[1].lower()
    
    if mode == 'encrypt':
        input_file = sys.argv[2]
        otp_file = sys.argv[3]
        encrypted_file = sys.argv[4]
        encrypt_file(input_file, otp_file, encrypted_file)
        
    elif mode == 'decrypt':
        encrypted_file = sys.argv[2]
        otp_file = sys.argv[3]
        decrypted_file = sys.argv[4]
        decrypt_file(encrypted_file, otp_file, decrypted_file)
        
    else:
        print(f"Kļūda: nav norādīts encrypt vai decrypt, tā vietā norādīts '{mode}'")
        print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()