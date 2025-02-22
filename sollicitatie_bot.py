import discord
from discord.ext import commands

# Bot instellingen
BOT_TOKEN = 'VUL_IN'  # Vervang dit met je echte bot token geen client id of client token!
NOTIFICATIE_ROL_ID = VUL_IN  # Vervang dit met de ID van de rol die getagged moet worden
KANAL_ID_VOOR_SOLLICITATIES = VUL_IN # Vervang dit met de ID van het kanaal waar sollicitaties binnenkomen

# Lijst van beschikbare functies
FUNCTIES = [
    "Politie",
    "Wegenwacht",
    "Ambulance",
    "KMar",
    "Taxi"
]

# Formulier vragen per functie (aanpasbaar)
FORMULIER_VRAGEN = {
    "Politie": [
        "👤 Naam:",
        "🔢 Leeftijd:",
        "🤔 Motivatie:",
        "👮‍♂️ Ervaring (indien van toepassing):"
    ],
    "Wegenwacht": [
        "👤 Naam:",
        "🚗 Rijbewijs categorieën:",
        "🔧 Technische kennis:",
        "❓ Waarom wegenwacht?"
    ],
    "Ambulance": [
        "👤 Naam:",
        "🩺 Medische achtergrond:",
        "🚛 Rijbewijs C (vereist):",
        "📅 Beschikbaarheid:"
    ],
    "KMar": [
        "👤 Naam:",
        "🇳🇱 Nederlandse nationaliteit:",
        "🤔 Motivatie KMar:",
        "🪖 Militaire ervaring (indien van toepassing):"
    ],
    "Taxi": [
        "👤 Naam:",
        "🚗 Rijbewijs B:",
        "😊 Klantvriendelijkheid (omschrijf):",
        "🗺️ Gebiedskennis:"
    ]
}

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

class SollicitatieFormModal(discord.ui.Modal):
    def __init__(self, functie, vragen, *args, **kwargs):
        super().__init__(*args, **kwargs, title=f"Sollicitatie Formulier - {functie}") # Titel aangepast met functie
        self.functie = functie
        self.vragen = vragen
        self.antwoorden = {}

        for vraag in vragen:
            self.add_item(discord.ui.TextInput(label=vraag, style=discord.TextStyle.long))

    async def on_submit(self, interaction: discord.Interaction):
        for index, vraag in enumerate(self.vragen):
            self.antwoorden[vraag] = self.children[index].value # Antwoorden opslaan in dictionary

        # Formulier is klaar, stuur naar kanaal
        formulier_tekst_lijnen = [f"**Sollicitatie voor: {self.functie}** door {interaction.user.name}#{interaction.user.discriminator}:\n"]
        for vraag, antwoord in self.antwoorden.items():
            formulier_tekst_lijnen.append(f"{vraag} {antwoord}")
        formulier_tekst = "\n".join(formulier_tekst_lijnen)

        notificatie_kanaal = bot.get_channel(KANAL_ID_VOOR_SOLLICITATIES)
        notificatie_rol = interaction.guild.get_role(NOTIFICATIE_ROL_ID)

        if notificatie_kanaal is None:
            print(f"Error: Notificatie kanaal NIET GEVONDEN. ID: {KANAL_ID_VOOR_SOLLICITATIES}") # Meer specifieke Error print 1
            await interaction.response.send_message("Er is een probleem met het indienen van je sollicitatie. Het notificatiekanaal kon niet worden gevonden. Neem contact op met een beheerder.", ephemeral=True)
        elif notificatie_rol is None:
            print(f"Error: Notificatie rol NIET GEVONDEN. ID: {NOTIFICATIE_ROL_ID}") # Meer specifieke Error print 2
            await interaction.response.send_message("Er is een probleem met het indienen van je sollicitatie. De notificatierol kon niet worden gevonden. Neem contact op met een beheerder.", ephemeral=True)
        else:
            print(f"Debug: Proberen sollicitatie te sturen naar kanaal {notificatie_kanaal.name} (ID: {notificatie_kanaal.id})") # Debug print 1
            try:
                await notificatie_kanaal.send(f"{notificatie_rol.mention} Nieuwe sollicitatie voor **{self.functie}** van {interaction.user.mention}:\n\n{formulier_tekst}")
                await interaction.response.send_message("Bedankt voor je sollicitatie! Deze is succesvol ingediend.", ephemeral=True)
                print("Debug: Sollicitatie succesvol verstuurd!") # Debug print 2
            except discord.Forbidden:
                print(f"Error: Geen permissie om berichten te sturen naar kanaal {notificatie_kanaal.name} (ID: {notificatie_kanaal.id})") # Error print 1
                await interaction.response.send_message("Er is een probleem met het indienen van je sollicitatie. Controleer de bot permissies in het sollicitatie kanaal en neem contact op met een beheerder.", ephemeral=True)
            except Exception as e:
                print(f"Error: Onverwachte fout bij versturen sollicitatie: {e}") # Error print 2
                await interaction.response.send_message("Er is een probleem met het indienen van je sollicitatie. Neem contact op met een beheerder.", ephemeral=True)


@bot.event
async def on_ready():
    print(f'Bot is ingelogd als {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="aan het coderen...")) # Status aangepast naar "aan het coderen..."
    try:
        synced = await bot.tree.sync()
        print(f"Gesynchroniseerd {len(synced)} commando's")
    except Exception as e:
        print(f"Fout bij synchroniseren van commando's: {e}")


@bot.tree.command(name="solliciteren", description="Start de sollicitatie procedure.")
async def solliciteren_commando(interaction: discord.Interaction):
    embed = discord.Embed(title="Sollicitatie Formulier",
                          description="🎉 Welkom bij dit sollicitatie formulier!\n\n🏢 Wilt u aan de slag bij de overheid van deze stad?\n👇 U kunt hieronder uw keuze maken waarvoor u wilt solliciteren:\n\n_*Deze sollicitatie bot is ontwikkeld door Bjorn L (CustomCodex) op Github.*_", # Verbeterde beschrijving met icons en tekst + kleine regel - "sollicitatie" toegevoegd
                          color=discord.Color.blue())

    # Maak een dropdown menu (select menu) voor de functies
    functie_opties = [discord.SelectOption(label=functie) for functie in FUNCTIES]
    select_menu = discord.ui.Select(placeholder="Selecteer een functie", options=functie_opties) # Placeholder text aangepast

    async def select_callback(interaction_select):
        functie_keuze = select_menu.values[0]
        # await interaction_select.response.defer() # Bevestig ontvangst van de interactie - VERWIJDERD

        vragen = FORMULIER_VRAGEN[functie_keuze]
        modal = SollicitatieFormModal(functie_keuze, vragen) # Maak modal aan
        await interaction_select.response.send_modal(modal) # Stuur de modal naar de gebruiker


    select_menu.callback = select_callback
    view = discord.ui.View()
    view.add_item(select_menu)

    await interaction.response.send_message(embed=embed, view=view, ephemeral=True) # Ephemeral om het menu alleen voor de gebruiker zichtbaar te maken


@bot.tree.command(name="functies", description="Bekijk de beschikbare functies om voor te solliciteren.")
async def functies_commando(interaction: discord.Interaction):
    functie_lijst = "\n".join([f"- {functie}" for functie in FUNCTIES]) # Maak een lijst van functies met bullet points
    embed = discord.Embed(title="Beschikbare Functies",
                          description=f"Dit zijn de functies waar je momenteel voor kunt solliciteren:\n{functie_lijst}",
                          color=discord.Color.green())
    await interaction.response.send_message(embed=embed, ephemeral=True) # Ephemeral zodat alleen de gebruiker het ziet

@bot.tree.command(name="bothelp", description="Krijg hulp en informatie over de bot commando's.")
async def bothelp_commando(interaction: discord.Interaction):
    embed = discord.Embed(title="Help Commando's",
                          color=discord.Color.gold())
    embed.add_field(name="/solliciteren", value="Start de sollicitatie procedure. Volg de instructies in het popup formulier.", inline=False) # Aangepaste help tekst
    embed.add_field(name="/functies", value="Bekijk een lijst van alle beschikbare functies waar je op kunt solliciteren.", inline=False)
    embed.add_field(name="/bothelp", value="Toont dit help bericht met alle beschikbare commando's.", inline=False) # Naam veranderd naar bothelp
    embed.set_footer(text=f"⚙️ Ontwikkeld door CustomCodex (Bjorn)\n🔗 Meer info: https://github.com/CustomCodex") # Footer aangepast met naam en GitHub link
    await interaction.response.send_message(embed=embed, ephemeral=True) # Ephemeral zodat alleen de gebruiker het ziet


bot.run(BOT_TOKEN)