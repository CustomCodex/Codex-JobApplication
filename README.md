# Discord Application Bot

This Discord bot enables you to manage applications for various positions within your Discord server through a simple form system. Applications are submitted via pop-up forms directly in Discord, and the results are sent to a designated channel.

![Codex Job Application](https://i.imgur.com/lWReth7.png)

## Installation

Follow these steps to install and set up the bot:

1.  **Prerequisites:**
    *   Python 3.8 or higher is required. You can download Python from [python.org](https://www.python.org/).
    *   Ensure you have `pip` installed (usually included with Python).

2.  **Install the `discord.py` library:**
    Open your terminal or command prompt and run the following command:
    ```bash
    pip install discord.py
    ```

3.  **Create a Discord Bot Application:**
    *   Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    *   Click on "Create New Application".
    *   Give your application a name (e.g., "Application Bot") and click "Create".
    *   Go to the "Bot" tab in the menu on the left.
    *   Click on "Add Bot".
    *   Confirm by clicking "Yes, do it!".

4.  **Obtain your Bot Token:**
    *   On the "Bot" page, click on "Reset Token".
    *   **Important:** This token is secret. Do not share it with anyone! Copy the token and store it safely.

5.  **Obtain Channel and Role IDs:**
    *   **Enable Developer Mode in Discord:** Go to Discord Settings (gear icon next to your username) > Advanced > Developer Mode (toggle on).
    *   **Copy the Channel ID for applications:** Go to the Discord channel where you want to receive submitted applications. Right-click on the channel and choose "Copy ID".
    *   **Copy the Notification Role ID:** Go to Server Settings > Roles. Right-click on the role you want to tag when a new application is submitted. Choose "Copy ID".

6.  **Configure the Bot Code:**
    *   Open the `sollicitatie_bot.py` file with a text editor.
    *   **Replace the placeholders:**
        *   `BOT_TOKEN = 'FILL_IN'` - Replace this with the **Bot Token** you copied in step 4.
        *   `NOTIFICATIE_ROL_ID = FILL_IN` - Replace this with the **Notification Role ID** you copied in step 5.
        *   `KANAL_ID_VOOR_SOLLICITATIES = FILL_IN` - Replace this with the **Channel ID for applications** you copied in step 5.

7.  **Start the Bot:**
    *   Open your terminal or command prompt.
    *   Navigate to the folder where you saved `sollicitatie_bot.py`.
    *   Run the following command to start the bot:
        ```bash
        python sollicitatie_bot.py
        ```
    *   You should see a message in the terminal indicating that the bot has logged in.

8.  **Invite the Bot to your Server:**
    *   Go back to the [Discord Developer Portal](https://discord.com/developers/applications) and select your bot application.
    *   Go to "OAuth2" > "URL Generator".
    *   In "Scopes", check the options `bot` and `applications.commands`.
    *   In "Bot Permissions", select the permissions your bot needs (at least "View Channels", "Send Messages", "Read Message History", "Use Application Commands").
    *   Copy the generated URL.
    *   Open the URL in your browser and select the server where you want to add the bot. Click "Authorize".
  
      ![Codex Job Application](https://i.imgur.com/dKeD0Kj.png)

## Commands

Once the bot is added to your server, you can use the following commands by typing `/` in a text channel:

*   **`/solliciteren`**: Start the application procedure.
    *   **Usage:** Type `/solliciteren` in a channel and press Enter. The bot will display a menu where you can select a position you want to apply for. After selecting a position, a pop-up form will open where you can answer the application questions.
*   **`/functies`**: View the available positions to apply for.
    *   **Usage:** Type `/functies` in a channel and press Enter. The bot will display a list of currently available positions, visible only to you.
*   **`/bothelp`**: Get help and information about the bot commands.
    *   **Usage:** Type `/bothelp` in a channel and press Enter. The bot will display a help message with information about all available commands, visible only to you.

## Customizing Positions and Questions

You can easily customize the bot by editing the `FUNCTIES` lists and the `FORMULIER_VRAGEN` dictionary in the `sollicitatie_bot.py` file:

*   **`FUNCTIES`**: Change the list of position names to customize the available positions for applications.
*   **`FORMULIER_VRAGEN`**: Customize the questions per position. Add more questions, remove questions, or change the text of the questions. Ensure that the position names in `FORMULIER_VRAGEN` match those in the `FUNCTIES` list. You can also add Unicode icons to the questions to make them visually appealing.

**Note:** After modifying the code, you must stop and restart the bot for the changes to take effect.

## Troubleshooting

*   **Bot commands do not appear:** Ensure that the bot has the "Use Application Commands" permission in your server role settings. Also, re-invite the bot with the `applications.commands` scope (see installation step 8).
*   **Error message "There is a problem submitting your application...":** Double-check **carefully** whether the `NOTIFICATIE_ROL_ID` and `KANAL_ID_VOOR_SOLLICITATIES` are set correctly in the code and that the bot has permissions to send messages to the application channel. Check the console output of the bot for more detailed error messages.

For questions or assistance, visit the GitHub repository: [https://github.com/CustomCodex](https://github.com/CustomCodex)

---
_This application bot is developed by Bjorn L (CustomCodex) on Github._
