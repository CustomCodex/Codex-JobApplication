# Discord Sollicitatie Bot (Application Bot)

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg?style=flat-square)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-v2.x-blueviolet.svg?style=flat-square)](https://discordpy.readthedocs.io/en/stable/)

This Python script implements a Discord bot that provides a **sollicitatie (application) system** for your Discord server.  Users can easily apply for various roles or positions within your community through interactive forms directly within Discord. The bot streamlines the application process by sending applications to a designated channel and notifying relevant staff members.

![Codex Refund](https://i.imgur.com/J4xk4BX.png)

## Description

This bot is designed to simplify the application process for Discord servers, especially for roleplay communities, gaming guilds, or any server that requires applications for specific roles or teams.

**Key Features:**

*   **Interactive Application Forms:**  Users can apply for different positions by filling out structured forms directly within Discord modals.
*   **Customizable Positions:** Easily define the available positions users can apply for (e.g., Police, Ambulance, Moderator, etc.).
*   **Position-Specific Questions:**  Configure unique sets of questions for each application position, ensuring relevant information is collected.
*   **Automated Application Submission:** Submitted applications are automatically sent to a designated channel for review.
*   **Role Notifications:**  The bot can tag a specific role in the application channel to notify staff members of new submissions.
*   **User-Friendly Commands:** Simple and intuitive slash commands (`/solliciteren`, `/functies`, `/bothelp`) for easy interaction.
*   **Ephemeral Responses:**  Most bot interactions are ephemeral, meaning only the user interacting with the bot can see the responses, keeping channels clean.
*   **Informative Embeds:**  Uses Discord embeds to present information in a clear and organized manner.
*   **"Coding..." Status:**  Sets a custom "Coding..." status to indicate the bot is running and developed by CustomCodex.

## Available Commands

*   **/solliciteren**: Starts the application process. Presents users with a dropdown menu to select the position they want to apply for and then opens an interactive form modal.
*   **/functies**: Displays a list of currently available positions that users can apply for.
*   **/bothelp**: Shows a help message with information about all available bot commands and their usage.

## Setup and Installation

1.  **Prerequisites:**
    *   **Python 3.6 or higher:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
    *   **discord.py library:** Install the discord.py library. It's recommended to use a virtual environment.
        ```bash
        pip install discord.py
        ```

2.  **Download the Script:**
    *   Download the Python script (`your_script_name.py`) from this repository.

3.  **Bot Token:**
    *   Create a Discord Bot application at the [Discord Developer Portal](https://discord.com/developers/applications).
    *   Navigate to your bot application and go to the "Bot" tab.
    *   Click "Reset Token" to generate a bot token. **Keep this token secure and do not share it publicly.**
    *   Replace `'YOUR_BOT_TOKEN'` in the script with your actual bot token:
        ```python
        BOT_TOKEN = 'YOUR_BOT_TOKEN' # Replace with your real bot token
        ```

4.  **Channel and Role IDs:**
    *   **Notification Role ID:**  Get the ID of the Discord role that should be tagged when a new application is submitted. To get the ID, enable Developer Mode in Discord settings (Appearance -> Advanced), then right-click the role and select "Copy ID".
    *   **Application Channel ID:** Get the ID of the Discord channel where you want the applications to be sent.  Similarly, right-click the channel and select "Copy ID".
    *   Replace the placeholder IDs in the script with your actual IDs:
        ```python
        NOTIFICATIE_ROL_ID = ENTERHERE  # Replace with the ID of the role to tag
        KANAL_ID_VOOR_SOLLICITATIES = ENTERHERE # Replace with the ID of the application channel
        ```

5.  **Customize Positions and Forms (Optional):**
    *   **`FUNCTIES` list:** Modify the `FUNCTIES` list to include the positions relevant to your server.
    *   **`FORMULIER_VRAGEN` dictionary:**  Customize the questions for each position in the `FORMULIER_VRAGEN` dictionary. Ensure the keys match the `FUNCTIES` list.

6.  **Run the Bot:**
    *   Navigate to the directory where you saved the script in your terminal.
    *   Run the script using Python:
        ```bash
        python your_script_name.py
        ```
    *   Invite the bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal (OAuth2 -> URL Generator, select `applications.commands` and `bot` scopes, and the necessary bot permissions).

## Configuration

You can configure the bot by modifying the following variables in the script:

*   **`BOT_TOKEN`**:  **(Required)** Your Discord bot token.
*   **`NOTIFICATIE_ROL_ID`**: **(Required)** The ID of the Discord role to tag for notifications.
*   **`KANAL_ID_VOOR_SOLLICITATIES`**: **(Required)** The ID of the Discord channel where applications will be sent.
*   **`FUNCTIES`**:  A list of strings representing the available positions users can apply for.
*   **`FORMULIER_VRAGEN`**: A dictionary where keys are position names (matching `FUNCTIES`) and values are lists of questions (strings) for the application form for that position.

## Contributing

Contributions to improve the bot are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Developed by [CustomCodex](https://github.com/CustomCodex) (Bjorn L).
