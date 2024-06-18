class Game:
    def __init__(self):
        self.friend_level = 0
        self.flirt_level = 0

    def start_game(self):
        print("Hoş geldiniz! Adınız Cedric ve inek bir öğrenci olarak okulda aşık olduğunuz kızı tavlamaya çalışacaksınız.")
        print("İlk adım olarak ona sosyal medyadan mesaj atmaya karar verdiniz.")
        self.first_choice()

    def first_choice(self):
        print("\nMesajınızı nasıl göndermek istersiniz?")
        print("1. Merhaba, nasılsın? Uzun zamandır seni görüyorum ve tanışmak isterim.")
        print("2. Selam, seni fark ettim ve harika olduğunu düşündüm. Biraz sohbet etmek ister misin?")
        choice = input("Seçiminiz (1 veya 2): ")

        if choice == "1":
            print("\nMesajınız gönderildi ve cevap bekliyorsunuz...")
            self.friend_level += 1
            self.first_response(1)
        elif choice == "2":
            print("\nMesajınız gönderildi ve cevap bekliyorsunuz...")
            self.flirt_level += 1
            self.first_response(2)
        else:
            print("\nGeçersiz seçim. Lütfen 1 veya 2 seçin.")
            self.first_choice()

    def first_response(self, choice):
        if choice == 1:
            print("Kız mesajınızı okudu ve şöyle cevap verdi: 'Merhaba, iyiyim teşekkürler. Sen nasılsın?'")
            self.second_choice()
        elif choice == 2:
            print("Kız mesajınızı okudu ve şöyle cevap verdi: 'Merhaba! Tabii ki, biraz sohbet edebiliriz.'")
            self.second_choice()

    def second_choice(self):
        print("\nŞimdi ne yapmak istersiniz?")
        print("1. Onunla ortak ilgi alanlarınızdan bahsetmek.")
        print("2. Ona doğrudan buluşmak isteyip istemediğini sormak.")
        print("3. Ona hobileri hakkında sorular sormak.")
        print("4. Ona okuldaki dersler hakkında konuşmak.")
        choice = input("Seçiminiz (1, 2, 3 veya 4): ")

        if choice == "1":
            print("\nOrtak ilgi alanlarınızdan bahsettiniz ve o da sizinle ilgilenmeye başladı.")
            self.friend_level += 2
            self.third_choice()
        elif choice == "2":
            print("\nBuluşma teklif ettiniz.")
            self.flirt_level += 2
            self.meet_up()
        elif choice == "3":
            print("\nHobileri hakkında sordunuz ve ortak hobileriniz olduğunu keşfettiniz.")
            self.friend_level += 2
            self.third_choice()
        elif choice == "4":
            print("\nOkuldaki dersler hakkında konuştunuz ve benzer derslerden hoşlandığınızı öğrendiniz.")
            self.friend_level += 1
            self.third_choice()
        else:
            print("\nGeçersiz seçim. Lütfen 1, 2, 3 veya 4 seçin.")
            self.second_choice()

    def third_choice(self):
        print("\nKonuşmanız derinleşiyor. Şimdi ne yapmak istersiniz?")
        print("1. Onu daha yakından tanımak için sorular sormak.")
        print("2. Ona doğrudan buluşmak isteyip istemediğini sormak.")
        print("3. Ona bir hediye vermek.")
        print("4. Ona okul projelerinde yardım etmeyi teklif etmek.")
        choice = input("Seçiminiz (1, 2, 3 veya 4): ")

        if choice == "1":
            print("\nOnu daha yakından tanımak için sorular sordunuz ve o da sizinle daha çok ilgilenmeye başladı.")
            self.friend_level += 3
            self.check_levels()
        elif choice == "2":
            print("\nBuluşma teklif ettiniz.")
            self.flirt_level += 3
            self.meet_up()
        elif choice == "3":
            print("\nOna güzel bir hediye verdiniz ve çok mutlu oldu.")
            self.flirt_level += 2
            self.check_levels()
        elif choice == "4":
            print("\nOna okul projelerinde yardım etmeyi teklif ettiniz ve çok memnun oldu.")
            self.friend_level += 2
            self.check_levels()
        else:
            print("\nGeçersiz seçim. Lütfen 1, 2, 3 veya 4 seçin.")
            self.third_choice()

    def meet_up(self):
        if self.flirt_level > 3:
            print("\nKız buluşma teklifinizi kabul etti ve bir buluşma ayarladınız. Tebrikler!")
            self.fourth_choice()
        else:
            print("\nKız buluşma teklifinizi reddetti. Arkadaş olarak kalmak istediğini belirtti.")
            self.fail()

    def check_levels(self):
        if self.friend_level >= 5:
            print("\nKız sizi çok seviyor ve arkadaş olarak görmekten çok mutlu.")
            self.fourth_choice()
        elif self.flirt_level >= 5:
            print("\nKız size karşı romantik hisler beslemeye başladı.")
            self.fourth_choice()
        else:
            print("\nKız sizinle daha çok vakit geçirmek istiyor. İlişkiniz olumlu ilerliyor.")
            self.fourth_choice()

    def fourth_choice(self):
        print("\nİlişkiniz ilerliyor. Şimdi ne yapmak istersiniz?")
        print("1. Onu sinemaya davet etmek.")
        print("2. Birlikte yürüyüşe çıkmayı teklif etmek.")
        print("3. Onunla bir kafede buluşmayı önermek.")
        print("4. Okul sonrası etkinliklere birlikte katılmayı teklif etmek.")
        choice = input("Seçiminiz (1, 2, 3 veya 4): ")

        if choice == "1":
            print("\nOnu sinemaya davet ettiniz ve kabul etti. Güzel bir akşam geçirdiniz.")
            self.flirt_level += 2
            self.fifth_choice()
        elif choice == "2":
            print("\nBirlikte yürüyüşe çıktınız ve samimi bir sohbet ettiniz.")
            self.friend_level += 2
            self.fifth_choice()
        elif choice == "3":
            print("\nKafede buluştunuz ve güzel bir sohbet ettiniz.")
            self.flirt_level += 1
            self.fifth_choice()
        elif choice == "4":
            print("\nOkul sonrası etkinliklere birlikte katıldınız ve eğlenceli zaman geçirdiniz.")
            self.friend_level += 1
            self.fifth_choice()
        else:
            print("\nGeçersiz seçim. Lütfen 1, 2, 3 veya 4 seçin.")
            self.fourth_choice()

    def fifth_choice(self):
        print("\nİlişkiniz derinleşiyor. Şimdi ne yapmak istersiniz?")
        print("1. Ona içten bir mesaj göndermek.")
        print("2. Ona komik bir video paylaşmak.")
        print("3. Birlikte vakit geçirmek için okul sonrası buluşmayı teklif etmek.")
        print("4. Ona duygusal bir hediye vermek.")
        choice = input("Seçiminiz (1, 2, 3 veya 4): ")

        if choice == "1":
            print("\nOna içten bir mesaj gönderdiniz ve çok etkilendi.")
            self.flirt_level += 2
            self.sixth_choice()
        elif choice == "2":
            print("\nOna komik bir video gönderdiniz ve çok güldü.")
            self.friend_level += 2
            self.sixth_choice()
        elif choice == "3":
            print("\nBirlikte vakit geçirmek için okul sonrası buluşmayı teklif ettiniz ve kabul etti.")
            self.flirt_level += 1
            self.sixth_choice()
        elif choice == "4":
            print("\nOna duygusal bir hediye verdiniz ve çok duygulandı.")
            self.flirt_level += 2
            self.sixth_choice()
        else:
            print("\nGeçersiz seçim. Lütfen 1, 2, 3 veya 4 seçin.")
            self.fifth_choice()

    def sixth_choice(self):
        print("\nİlişkiniz çok ileri bir seviyede. Şimdi ne yapmak istersiniz?")
        print("1. Ona duygularınızı itiraf etmek.")
        print("2. Onunla romantik bir akşam yemeği organize etmek.")
        print("3. Birlikte bir hafta sonu kaçamağı planlamak.")
        print("4. Ona gelecekle ilgili planlarınızdan bahsetmek.")
        choice = input("Seçiminiz (1, 2, 3 veya 4): ")

        if choice == "1":
            if self.flirt_level >= 5:
                print("\nOna duygularınızı itiraf ettiniz ve o da size karşılık verdi. Artık birlikte mutlu bir çift oldunuz!")
                self.success()
            else:
                  print("\nOna duygularınızı itiraf ettiniz ama o sizi sadece arkadaş olarak gördüğünü söyledi.")
                  self.fail()
        elif choice == "2":
            if self.flirt_level >= 5:
                print("\nOnunla romantik bir akşam yemeği organize ettiniz ve çok romantik bir akşam geçirdiniz. Artık birlikte mutlu bir çift oldunuz!")
                self.success()
            else:
                print("\nOnunla romantik bir akşam yemeği organize ettiniz ama o bu durumu arkadaşça bir buluşma olarak gördü.")
                self.fail()
        elif choice == "3":
            if self.flirt_level >= 5:
                print("\nBirlikte bir hafta sonu kaçamağı planladınız ve çok güzel zaman geçirdiniz. Artık birlikte mutlu bir çift oldunuz!")
                self.success()
            else:
                print("\nBirlikte bir hafta sonu kaçamağı planladınız ama o bu durumu arkadaşça bir gezi olarak gördü.")
                self.fail()
        elif choice == "4":
            if self.flirt_level >= 5:
                print("\nOna gelecekle ilgili planlarınızdan bahsettiniz ve o da sizinle aynı hayalleri paylaştığını söyledi. Artık birlikte mutlu bir çift oldunuz!")
                self.success()
            else:
                print("\nOna gelecekle ilgili planlarınızdan bahsettiniz ama o bu durumu sadece arkadaşça bir paylaşım olarak gördü.")
                self.fail()
        else:
            print("\nGeçersiz seçim. Lütfen 1, 2, 3 veya 4 seçin.")
            self.sixth_choice()

    def success(self):
        print("\nTebrikler! Kızı tavladınız ve artık mutlu bir çiftsiniz. Oyun sona erdi.")

    def fail(self):
        print("\nMaalesef, kızı tavlayamadınız ve arkadaş olarak kaldınız. Oyun sona erdi.")
        self.retry()

    def retry(self):
        print("\nTekrar denemek ister misiniz? (Evet veya Hayır)")
        choice = input("Seçiminiz: ")
        if choice.lower() == "evet":
            self.__init__()
            self.start_game()
        else:
            print("\nOyun sona erdi. Teşekkürler!")

game = Game()
game.start_game()