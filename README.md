# Python-Mini-Project_NPWP-Validity-Checker
This repository contains a Python Mini Project (Coding Challenge) on NPWP Validity using Python

<hr>

## NPWP Criteria

NPWP has a serial code with 15 numbers, which uses the following format: ***00.000.000.0-000.000***.

The first two digits, (00).xxx.xxx.x-xxx.xxx indicate the Taxpayer's Identity:

- 01 to 03 are Corporate Taxpayers
- 04 and 06 are Entrepreneur Taxpayers
- 05 is an Employee Taxpayer
- 07 to 09 are Individual Taxpayers

The next six digits, xx.(000,000).x-xxx.xxx indicate the Registration Number given by Kantor Pusat Direktorat Jenderal Pajak to Kantor Pelayanan Pajak (KPP).

The next digit xx.xxx.xxx.(0)-xxx.xxx use as a security tool to avoid forgery or errors in the NPWP.

The next three digits, xx.xx.xxx.x-(000).xxx are the KPP Code. For example, if the code is 015, it means that the NPWP was issued at KPP with code 015.

The last three digits, xx.xxx.xxx.x-xxx.(000) indicate Taxpayer Status:

- 000 means Central (usually called Central NPWP)
- 00x (001,002 etc.) means Branch, where the final number indicates the branch order (1st branch then 001; 2nd branch then 002; etc.).

<hr>

## Notification Example

Output example if the NPWP is valid:

    Kode seri NPWP valid!
    Identitas Wajib Pajak: 01 Wajib Pajak Pengusaha
    Nomor Registrasi: 885.434
    Alat Pengaman: 4
    Kode KPP: 215
    Status Wajib Pajak: 000

If it is invalid, a notification will appear according to the reason: 

    - This NPWP is invalid because it contains non-numerical characters in it.
    - This NPWP is invalid because it has more than 15 digits.
    - This NPWP is invalid because it does not follow the standard format: 00.000.000.0-000.000.
    - This NPWP is invalid because the first 2 digits can only be entered from 01 to 09.
