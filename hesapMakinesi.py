a= float(input("1.sayıyı gir:"))
b= float(input("2.sayıyı gir:"))
islem= input("İşlem seç (+, -, *, /):")

if islem == "+":
    print ("Sonuç:", a + b)
elif islem == "-":   
    print ("Sonuç:", a - b)
elif islem == "*":
    print ("Sonuç:", a * b)
 elif islem == "/":
    print ("Sonuç:", a / b if b |= 0 else "sıfıra bölünemez!"
else:
    print("Geçersiz İşlem!")
