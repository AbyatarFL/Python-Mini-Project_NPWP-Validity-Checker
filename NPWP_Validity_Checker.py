# Import regular expression library to split strings by 2 separator characters at a time
import re

# Create Function NPWP validation
def npwp_cek():
    # Input NPWP Number
    npwp = input("Masukkan NPWP: ")
    
    # Check NPWP Number (NPWP Must be 15 digit and only separated by . or -)
    if len(npwp) != 20: 
        return "NPWP harus 15 digit angka"
    if not all(char.isdigit() or char in '.-' for char in npwp):
        return "NPWP harus berupa angka"
    
    # Between digit 9 & 10 must be separated by '-'
    if npwp[12] != '-':
        return "Antara Digit 9 & 10 harus dipisah dengan '-'"
    
    # Split NPWP Number using reguler expression module (split by . or -)
    npwp_split = re.split(r'[.-]', npwp)
    
    # First 2 digit of NPWP Number must be 01-09
    if npwp_split[0] not in ['01', '02', '03', '04', '05', '06', '07', '08', '09']:
        return "NPWP harus diawali dengan 01-09"
    
    # Classify NPWP status based on the first 2 digits
    status = ""
    if npwp_split[0] in ['01','02','03']:
        status = "Wajib Pajak Badan"
    elif npwp_split[0] in ['04','06']:
        status = "Wajib Pajak Pengusaha"
    elif npwp_split[0] == '05':
        status = "Wajib Pajak Karyawan"
    elif npwp_split[0] in ['07', '08', '09']:
        status = "Wajib Pajak Orang Pribadi"

    # Return NPWP Number and Status if NPWP Number is valid
    return f'''
Kode Seri NPWP Valid!
NPWP: {npwp}
Identitas Wajib Pajak: {npwp_split[0]}, {status}
Nomor Registrasi: {npwp_split[1]}.{npwp_split[2]}
Alamat Pengamanan: {npwp_split[3]}
Kode KPP: {npwp_split[4]}
Status Wajib Pajak: {npwp_split[5]}'''
    
        
# Call & print Function NPWP validation
print(npwp_cek())
