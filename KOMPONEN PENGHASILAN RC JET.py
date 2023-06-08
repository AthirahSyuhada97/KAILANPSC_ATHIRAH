jenis_komponen_penghasilan_rc_jet = ["MPPF FORM 5x1000x900 mm", "Control Horn", "Push Rod Wire", "Linkage Stopper","ESC (5W50A)",   "Receiver (1A10B RX)", "Serro 9g", "Carbon Fiber Rod 3 mm", "RC Lippo Battery", "Propeller", "Flyshy -i6x remote control","Brushless Motor"]
harga_komponen_penghasilan_rc_jet = [23,3,2,12,67,61,5.20,25.30,57.56,5,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]

print("HARGA MPPF FORM 5x1000x900 mm=RM23, Control Horn=RM3,Push Rod Wire=RM2,Linkage Stopper=RM12,ESC (5W50A)=RM67, Receiver (1A10B RX)=RM61, Serro 9g=RM5.20,Carbon Fiber Rod 3 mm=RM25.30, RC Lippo Battery=RM57.56, Propeller=RM5,Flyshy -i6x remote control=RM161,Brushless Motor=RM15.79")
a=int(input("Masukkan tempahan untuk MPPF FORM 5x1000x900:"))
b=int(input("Masukkan tempahan untuk Control Horn:"))
c=int(input("Masukkan tempahan untuk Push Rod Wire:"))
d=int(input("Masukkan tempahan untuk Linkage Stopper:"))
e=int(input("Masukkan tempahan untuk ESC (5W50A):"))
f=int(input("Masukkan tempahan untuk Receiver (1A10B RX):"))
g=int(input("Masukkan tempahan untuk Serro 9g:"))
h=int(input("Masukkan tempahan untuk Carbon Fiber Rod 3 mm:"))
i=int(input("Masukkan tempahan untuk RC Lippo Battery:"))
j=int(input("Masukkan tempahan untuk Propeller:"))
k=int(input("Masukkan tempahan untuk Push Rod Wire:"))
l=int(input("Masukkan tempahan untuk Flyshy -i6x remote control:"))
m=int(input("Masukkan tempahan untuk Brushless Motor:"))

tempahan = [a,b,c,d,e,f,g,h,i,j,k,l,m]

def jumlah_harga() :
    for i in range (12) :
        jumlah[i] = harga_komponen_penghasilan_rc_jet[i]*tempahan[i]
        return(jumlah)
def cetak() :
    print("\n Tempahan anda ialah: ")
    print(a, "komponen", jenis_komponen_penghasilan_rc_jet[0])
    print(b, "komponen", jenis_komponen_penghasilan_rc_jet[1])
    print(c, "komponen", jenis_komponen_penghasilan_rc_jet[2])
    print(d, "komponen", jenis_komponen_penghasilan_rc_jet[3])
    print(e, "komponen", jenis_komponen_penghasilan_rc_jet[4])
    print(f, "komponen", jenis_komponen_penghasilan_rc_jet[5])
    print(g, "komponen", jenis_komponen_penghasilan_rc_jet[6])
    print(h, "komponen", jenis_komponen_penghasilan_rc_jet[7])
    print(i, "komponen", jenis_komponen_penghasilan_rc_jet[8])
    print(j, "komponen", jenis_komponen_penghasilan_rc_jet[9])
    print(k, "komponen", jenis_komponen_penghasilan_rc_jet[10])
    print(l, "komponen", jenis_komponen_penghasilan_rc_jet[11])
   
    print("\n Jumlah harga untuk tempahan ialah RM",sum (jumlah))
jumlah_harga()
cetak()    