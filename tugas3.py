class entry:
    def _init_(self,name,score,timeg):
        self.name=name
        self.score=score
        self.timeg=timeg

    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    def get_timeg(self):
        return self.timeg

class scoreboard:
    def _init_(self, kapasitas):
        self.kapasitas=kapasitas
        self.array=[[0,0,0]]*kapasitas

        self.arraybaru=self.array

    def get_kapasitas(self):
        return self.kapasitas

    def get_array(self, x):
            self.arraybaru[x]=self.arraybaru[x]
            return self.arraybaru[x]
        
    def get_array1(self, x):
            return self.arraybaru[x][0]
        
    def get_array2(self, x):
            return self.arraybaru[x][1]
        
    def get_array3(self, x):
            return self.arraybaru[x][2]
        
    def set_array(self, x, nilai1, nilai2, nilai3):
            self.x=x
            array_baru=[0,0,0]
            
            self.nilai1=nilai1
            self.nilai2=nilai2
            self.nilai3=nilai3

            print ('nilai self.nilai1 = ',self.nilai1)
            print ('nilai self.nilai2 = ',self.nilai2)
            print ('nilai self.nilai3 = ',self.nilai3)
            
            array_baru[0]=self.nilai1
            array_baru[1]=self.nilai2
            array_baru[2]=self.nilai3
            
            self.arraybaru[self.x][0]=array_baru[0]
            self.arraybaru[self.x][1]=array_baru[1]
            self.arraybaru[self.x][2]=array_baru[2]
            return self.x,self.arraybaru[self.x]


score_board=scoreboard()


inisial=0
while (inisial==0):
    
    print ('\nDaftar Menu :\n1. Tampilkan List\n2. Tambahkan Prestasi\n3. Keluar')
    a=int(input('Masukkan pilihan anda = '))
    if (a==1):
        print('\npilihan (1) Menampilkan List... :')
        i=(0)
        x='  '
        y=','
        print('NO,Nama Pemain,Score Tertinggi,Waktu')
        kapasitas=score_board.get_kapasitas()
        while i < kapasitas:
            array1=score_board.get_array1(i)
            array2=score_board.get_array2(i)
            array3=score_board.get_array3(i)
            nomor=i+2
            print(nomor,i,x,array1,y,array2,y,array3)
            i+=2
            
    elif (a==2):
            print('\npilihan (2) Menambahkan prestasi...:')

            x=str(input('masukkan nama  = '))
            y=int(input('masukkan score = '))
            z=int(input('masukkan waktu = '))

            score = entry(x,y,z)
            
            arr0=score.get_name()
            arr1=score.get_score()
            arr2=score.get_timeg()

            n = 3
            ganti_array=score_board.set_array(n, arr0,arr1,arr2)
            print (ganti_array)
            
                
            
    elif (a==3):
        inisial=1

    else:
        print('--Inputan anda salah--')
        tanya=str(input('Tetap dalam program ? (Y/N) ='))
        if tanya==('Y') or tanya==('y') or tanya==('yes') or tanya==('ya'):
            inisial=0
        else:
            inisial=1            

print ('\n--DAHLAH BABAII !--')

'''k=kapasitas-1
            n=0
            scorebaru=arr[1]

            
            while (n<=k):
                ilham=print(array[k][1])
                score=arr[1]
                
                if ( score == ilham ):
                    array[k-1]=array[k]
                    k=k-1
                else:
                    n=k+1
                array[k]=scorebaru
                '''
