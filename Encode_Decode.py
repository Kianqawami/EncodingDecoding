def Encode_Decoding():
        from os import system
        while True:
            choice = int(input("\n1-Encode\n2-Decode\n3-Exit\nEnter youe choice:"))
            if choice == 1 :
                x = input("Enter your text:")
                def Encode(x):
                    for i in x:
                        print(chr(ord(i) * 2),end='')
                        system("cls")
                Encode(x)
            elif choice == 2 :
                x = input("Enter your text:")
                def Decode(x):
                    for i in x:
                        print(chr(ord(i) // 2),end="")
                        system("cls")
                Decode(x)
            elif choice == 3:
                print("\ngood luck:))")
                break
            else:
                print("try again later!")


Encode_Decoding()
