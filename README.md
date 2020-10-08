# TIP

Program do komunikacji głosowej - dwukierunkowej napisany w ramach zajęć z Telefonii IP Politechnika Poznańska.
Autorzy:
- Szymon Szczot
- Szymon Wasilewski

Aplikacja umożliwia połączenie z wcześniej zapisanym kontaktem i rozmowę głosową.

# Uruchomienie

Żeby uruchomić aplikację należy:

1. Uruchomić serwer z bazą kontaktów:
  1.1. Pobrać folder "TIP_address"  
  1.2. Wejść do głównego folderu za pomocą konsoli.  
  1.3. Uruchomić komendę 'python manage.py migrate'  
  1.4. Uruchomić komendę 'python manage.py runserver'  
  
2. Uruchomić aplikację właściwą:
  2.1. Pobrać folder "TIP_JoinMe"  
  2.2. Uruchomić komendę 'python <ścieżka do pliku "start_app.py">  

# Obsługa i działanie:

Na jednej z maszyn trzeba zacząć od Kliknięcia "Start server"
Po tej czynności najlepiej dodać swój kontakt do bazy.
Aby to zrobić należy Wpisać Nazwę do pola "PORT:" na samej górze okna i swoje IP w pole poniżej.
Następnie kliknąć "Dodaj kontakt" - przycisk na samym dole okna

Na drugiej maszynie W pole IP możemy wpisać Nazwę podaną w poprzednim punkcie, IP powinno automatycznie pobrać się z serwera.
Jeśli nie będzie takiego wpisu w bazie program spróbuje odczytać Nazwę wpisaną w pole jako IP a jeśli i to zawiedzie przerwie połączenie.

Po uzupełnieniu pól kliknąć na przycisk "Start Client" co powoduje nawiązanie połączenia.
Na maszynie 1 wyświetla się popup pytający czy przyjąć połączenie.

Po przyjęciu można rozmawiać.
