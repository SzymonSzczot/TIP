# JoinMe

Program do dwukierunkowej komunikacji głosowej napisany w ramach zajęć z Telefonii IP na Politechnice Poznańskiej.

## Autorzy
- Szymon Szczot
- Szymon Wasilewski

Aplikacja umożliwia połączenie z wcześniej zapisanym kontaktem i rozmowę głosową.

## Dokumentacja projektowa

TO_BE_ADDED

## Prezentacja działania

TO_BE_ADDED

## Uruchomienie

Żeby uruchomić aplikację należy:

1. (opcjonalnie) Uruchomić serwer z bazą kontaktów:  
  1.1. Pobierz pliki serwerowe `JoinMe_Server.zip` z Releases
  1.2. Wypakuj pliki w dogodnym (najlepiej pustym) folderze
  1.3. Uruchom skrypt `start_db.bat`
  
2. Uruchomić aplikację właściwą:  
  2.1. Pobierz aplikację kliencką `JoinMe_Client.exe` z Releases
  2.2. Uruchom aplikację

## Obsługa aplikacji klienckiej:

W tej chwili komunikacja jest możliwa tylko w sieci lokalnej.

W oknie aplikacji klikamy przycisk "Join network", aby móc przyjąc/wykonać jakiekolwiek połączenie.

Przed wykonaniem połączenia można dodać kontakt do bazy. Dodać je może klient z uruchomionym lokalnie serwerem kontaktów.
Aby to zrobić należy wpisać nazwę kontaktu do pola "CLIENT NAME" na samej górze okna i adres IP, który chcemy z daną nazwą powiązać w pole poniżej.
Następnie należy kliknąć przycisk "Add contact" na samym dole okna.

Przy wykonywaniu połączenia w pole "IP" możemy wpisać dokładny adres komputera w sieci lokalnej, z którym próbujemy się połączyć ALBO nazwę kontaktu zapisanego w bazie danych.
Jeśli nie będzie takiego wpisu w bazie program spróbuje odczytać wartość wpisaną w pole jako adres IP, a jeśli i to zawiedzie przerwie połączenie.

Po uzupełnieniu pola klikamy na przycisk "Connect", co powoduje nawiązanie połączenia.
Na maszynie o podanym IP wyświetli się popup pytający, czy przyjąć połączenie - po zaakceptowaniu można rozmawiać.
