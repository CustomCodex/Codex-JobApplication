# Discord Sollicitatie Bot

Deze Discord bot maakt het mogelijk om sollicitaties voor verschillende functies binnen je Discord server te beheren via een eenvoudig formulier systeem. Sollicitaties worden ingediend via pop-up formulieren direct in Discord en de resultaten worden naar een aangewezen kanaal gestuurd.

## Installatie

Volg deze stappen om de bot te installeren en op te zetten:

1.  **Vereisten:**
    *   Python 3.8 of hoger is vereist. Je kunt Python downloaden van [python.org](https://www.python.org/).
    *   Zorg ervoor dat je `pip` hebt geïnstalleerd (meestal meegeleverd met Python).

2.  **Installeer de `discord.py` library:**
    Open je terminal of command prompt en voer het volgende commando uit:
    ```bash
    pip install discord.py
    ```

3.  **Maak een Discord Bot Applicatie:**
    *   Ga naar de [Discord Developer Portal](https://discord.com/developers/applications).
    *   Klik op "Create New Application".
    *   Geef je applicatie een naam (bijvoorbeeld "Sollicitatie Bot") en klik op "Create".
    *   Ga naar het "Bot" tabblad in het menu aan de linkerkant.
    *   Klik op "Add Bot".
    *   Bevestig door op "Yes, do it!" te klikken.

4.  **Verkrijg je Bot Token:**
    *   Op de "Bot" pagina, klik op "Reset Token".
    *   **Let op:** Dit token is geheim. Deel het met niemand! Kopieer het token en bewaar het veilig.

5.  **Verkrijg Kanaal en Rol ID's:**
    *   **Zet Developer Mode aan in Discord:** Ga naar Discord Instellingen (tandwiel naast je gebruikersnaam) > Geavanceerd > Developer Mode (inschakelen).
    *   **Kopieer de Kanaal ID voor sollicitaties:** Ga naar het Discord kanaal waar je de ingediende sollicitaties wilt ontvangen. Rechtermuisklik op het kanaal en kies "ID kopiëren".
    *   **Kopieer de Notificatie Rol ID:** Ga naar de server instellingen > Rollen. Rechtermuisklik op de rol die je wilt taggen wanneer er een nieuwe sollicitatie is. Kies "ID kopiëren".

6.  **Configureer de Bot Code:**
    *   Open het `sollicitatie_bot.py` bestand met een teksteditor.
    *   **Vervang de placeholders:**
        *   `BOT_TOKEN = 'VUL_IN'` - Vervang dit met het **Bot Token** dat je in stap 4 hebt gekopieerd.
        *   `NOTIFICATIE_ROL_ID = VUL_IN` - Vervang dit met de **Notificatie Rol ID** die je in stap 5 hebt gekopieerd.
        *   `KANAL_ID_VOOR_SOLLICITATIES = VUL_IN` - Vervang dit met de **Kanaal ID voor sollicitaties** die je in stap 5 hebt gekopieerd.

7.  **Start de Bot:**
    *   Open je terminal of command prompt.
    *   Navigeer naar de map waar je `sollicitatie_bot.py` hebt opgeslagen.
    *   Voer het volgende commando uit om de bot te starten:
        ```bash
        python sollicitatie_bot.py
        ```
    *   Je zou een bericht in de terminal moeten zien dat de bot is ingelogd.

8.  **Nodig de Bot uit naar je Server:**
    *   Ga terug naar de [Discord Developer Portal](https://discord.com/developers/applications) en selecteer je bot applicatie.
    *   Ga naar "OAuth2" > "URL Generator".
    *   Vink in "Scopes" de opties `bot` en `applications.commands` aan.
    *   Selecteer in "Bot Permissions" de permissies die je bot nodig heeft (minimaal "View Channels", "Send Messages", "Read Message History", "Use Application Commands").
    *   Kopieer de gegenereerde URL.
    *   Open de URL in je browser en selecteer de server waar je de bot wilt toevoegen. Klik op "Authorize".

## Commando's

Zodra de bot is toegevoegd aan je server, kun je de volgende commando's gebruiken door `/` te typen in een tekstkanaal:

*   **`/solliciteren`**: Start de sollicitatie procedure.
    *   **Gebruik:** Typ `/solliciteren` in een kanaal en druk op Enter. De bot zal een menu weergeven waarin je een functie kunt selecteren waarvoor je wilt solliciteren. Na het selecteren van een functie, opent er een pop-up formulier waar je de sollicitatie vragen kunt beantwoorden.
*   **`/functies`**: Bekijk de beschikbare functies om voor te solliciteren.
    *   **Gebruik:** Typ `/functies` in een kanaal en druk op Enter. De bot zal een lijst van de huidige beschikbare functies weergeven, alleen zichtbaar voor jou.
*   **`/bothelp`**: Krijg hulp en informatie over de bot commando's.
    *   **Gebruik:** Typ `/bothelp` in een kanaal en druk op Enter. De bot zal een help bericht weergeven met informatie over alle beschikbare commando's, alleen zichtbaar voor jou.

## Aanpassen van Functies en Vragen

Je kunt de bot eenvoudig aanpassen door de lijsten `FUNCTIES` en de dictionary `FORMULIER_VRAGEN` in het `sollicitatie_bot.py` bestand te bewerken:

*   **`FUNCTIES`**:  Verander de lijst van functienamen om de beschikbare functies voor sollicitaties aan te passen.
*   **`FORMULIER_VRAGEN`**:  Pas de vragen per functie aan. Voeg meer vragen toe, verwijder vragen, of verander de tekst van de vragen. Zorg ervoor dat de functienamen in `FORMULIER_VRAGEN` overeenkomen met die in de `FUNCTIES` lijst. Je kunt ook Unicode iconen toevoegen aan de vragen om ze visueel aantrekkelijker te maken.

**Let op:** Na het wijzigen van de code, moet je de bot stoppen en opnieuw starten om de veranderingen door te voeren.

## Probleemoplossing

*   **Bot commando's verschijnen niet:** Zorg ervoor dat de bot de permissie "Applicatiecommando's" heeft in je server rollen instellingen. Nodig de bot ook opnieuw uit met de `applications.commands` scope (zie installatie stap 8).
*   **Foutmelding "Er is een probleem met het indienen van je sollicitatie...":** Controleer **nauwkeurig** of de `NOTIFICATIE_ROL_ID` en `KANAL_ID_VOOR_SOLLICITATIES` correct zijn ingesteld in de code en dat de bot permissies heeft om berichten te sturen naar het sollicitatiekanaal. Bekijk de console output van de bot voor meer gedetailleerde foutmeldingen.

Voor vragen of hulp, bekijk de GitHub repository: [https://github.com/CustomCodex](https://github.com/CustomCodex)

---
_Deze sollicitatie bot is ontwikkeld door Bjorn L (CustomCodex) op Github._