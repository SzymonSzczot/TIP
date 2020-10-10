# JoinMe

Program do dwukierunkowej komunikacji głosowej napisany w ramach zajęć z Telefonii IP na Politechnice Poznańskiej.

## Autorzy
- Szymon Szczot
- Szymon Wasilewski

Aplikacja umożliwia połączenie z wcześniej zapisanym kontaktem i rozmowę głosową.

## Dokumentacja projektowa

Dokumentację można obejrzeć [tutaj](https://github.com/SzymonSzczot/TIP/blob/master/TIP_Szczot_Wasilewski_dokumentacja.pdf)

## Prezentacja działania

[![](http://img.youtube.com/vi/BuInwu4UmT0/0.jpg)](http://www.youtube.com/watch?v=BuInwu4UmT0 "")

## Uruchomienie

Żeby uruchomić aplikację należy:

0. Zainstalować Python w wersji przynajmniej 3.7.2

1. Uruchomić serwer z bazą kontaktów (jeżeli chcemy wykonać połączenie):  
  - Pobierz pliki serwerowe `JoinMe_Server.zip` z Releases
  - Wypakuj pliki w dogodnym (najlepiej pustym) folderze
  - Uruchom skrypt `start_db.bat`
  
2. Uruchomić aplikację właściwą:  
  - Pobierz aplikację kliencką `JoinMe_Client.exe` z Releases
  - Uruchom aplikację

## Obsługa aplikacji klienckiej:

W tej chwili komunikacja jest możliwa tylko w sieci lokalnej.

W oknie aplikacji klikamy przycisk "Join network", aby móc przyjąc jakiekolwiek połączenie.

Przed wykonaniem połączenia można dodać kontakt do bazy. Dodać je może klient z uruchomionym lokalnie serwerem kontaktów.
Aby to zrobić należy wpisać nazwę kontaktu do pola "CLIENT NAME" na samej górze okna i adres IP, który chcemy z daną nazwą powiązać w pole poniżej.
Następnie należy kliknąć przycisk "Add contact" na samym dole okna.

Przy wykonywaniu połączenia w pole "IP" możemy wpisać dokładny adres komputera w sieci lokalnej, z którym próbujemy się połączyć ALBO nazwę kontaktu zapisanego w bazie danych.
Jeśli nie będzie takiego wpisu w bazie program spróbuje odczytać wartość wpisaną w pole jako adres IP, a jeśli i to zawiedzie przerwie połączenie.

Po uzupełnieniu pola klikamy na przycisk "Connect", co powoduje nawiązanie połączenia.
O ile maszyna o podanym IP nasłuchuje za połączeniem, to na jej ekranie wyświetli się popup pytający, czy przyjąć połączenie - po zaakceptowaniu można rozmawiać.
