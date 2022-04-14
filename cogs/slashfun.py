import discord
from discord.commands import \
    slash_command
import traceback
import random
from discord.ext import commands
import asyncio
import random
import string
import pyfiglet
import humanize
from datetime import datetime
import pyjokes
from data import Data 

class slashfun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.emojify_symbols = {
            "0": ":zero:",
            "1": ":one:",
            "2": ":two:",
            "3": ":three:",
            "4": ":four:",
            "5": ":five:",
            "6": ":six:",
            "7": ":seven:",
            "8": ":eight:",
            "9": ":nine:",
            "!": ":exclamation:",
            "#": ":hash:",
            "?": ":question:",
            "*": ":asterisk:",
        }

        self.emoji_numbers = {
            1: "1️⃣",
            2: "2️⃣",
            3: "3️⃣",
            4: "4️⃣",
            5: "5️⃣",
            6: "6️⃣",
            7: "7️⃣",
            8: "8️⃣",
            9: "9️⃣",
        }
        self.launched_at = datetime.now()
        self.suggestion_channel = 846273239546462249

    @commands.slash_command(name="suggest", description="Give a suggestion to the bot")
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def suggest(self, ctx, *, msg):
        channel = self.bot.get_channel(846273239546462249)
        embed = discord.Embed(title=f"Suggestion",
                              description="{}".format(msg), color=ctx.author.color)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        success_embed = discord.Embed(
            title=":white_check_mark: Success!", description="Your suggestion has been sent to the devolopers!", color=discord.Color.green)
        await ctx.respond(embed=success_embed)

        my_msg = await channel.send(embed=embed)
        await my_msg.add_reaction("⬆️")
        await my_msg.add_reaction("⬇️")
        await ctx.message.delete()

    @commands.slash_command(name="joke", description="Gives you a joke")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def joke(self, ctx):
        joke = pyjokes.get_joke(language="en", category="neutral")
        await ctx.respond(joke)

    # @commands.command()
    # async def embed(self, ctx):
    #     await ctx.channel.purge(limit=1)
    #     questions = ["Enter a title",
    #                  "Enter a Description for the embed"]
    #     answers = []

    #     def check(m):
    #         return m.author == ctx.author and m.channel == ctx.channel

    #     for i in questions:
    #         await ctx.respond(i)

    #         try:
    #             msg = await bot.wait_for('message', timeout=1000.0, check=check)
    #         except asyncio.TimeoutError:
    #             await ctx.respond('It\' been alot of time still no response so I\'m closing this application! re-apply with =apply')
    #             return
    #         else:
    #             answers.append(msg.content)

    #     tittle = answers[0]

    #     desc = answers[1]

    #     embed = discord.Embed(
    #         title=f"{tittle}", description=f"{desc}", color=ctx.author.color)
    #     embed.set_footer(text=f"Requested by {ctx.author.name}")
    #     await ctx.respond(embed=embed)

    @commands.slash_command(description="Turn a sentence into emojis")
    async def emojify(self, ctx, *, sentence: str):
        emojified_sentence = ""
        sentence = sentence.lower()

        for char in sentence:
            char_lower = char.lower()

            if char_lower in string.ascii_lowercase:
                emojified_sentence += f":regional_indicator_{char}:"
            elif char_lower in self.emojify_symbols:
                emojified_sentence += self.emojify_symbols[char_lower]
            else:
                emojified_sentence += char

        await ctx.respond(emojified_sentence)

    @commands.slash_command(name="ascii", description="Turn a sentence into cool ASCII art")
    async def ascii(self, ctx: commands.Context, *, sentence: str):
        ascii_text = pyfiglet.figlet_format(sentence)
        await ctx.respond(f"```{ascii_text}```")

    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def sayembed(self, ctx, *, msg):
    #     await ctx.message.delete()
    #     embed = discord.Embed(title="{}".format(msg))
    #     embed.add_field(name=f"Requested by ", value=f"{ctx.author}")
    #     embed.set_footer(text="Discord: https://discord.gg/b8Sj7SS ")
    #     await ctx.respond(embed=embed)
    #     print("sayembed")

    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def Sayembed(self, ctx, *, msg):
    #     await ctx.message.delete()
    #     embed = discord.Embed(title="{}".format(msg))
    #     embed.add_field(name=f"Requested by ", value=f"{ctx.author}")
    #     embed.set_footer(text="Discord: https://discord.gg/b8Sj7SS ")
    #     await ctx.respond(embed=embed)

    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def SayEmbed(self, ctx, *, msg):
    #     await ctx.message.delete()
    #     embed = discord.Embed(title="{}".format(msg))
    #     embed.add_field(name=f"Requested by ", value=f"{ctx.author}")
    #     embed.set_footer(text="Discord: https://discord.gg/b8Sj7SS ")
    #     await ctx.respond(embed=embed)

    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def SAYEMBED(self, ctx, *, msg):
    #     await ctx.message.delete()
    #     embed = discord.Embed(title="{}".format(msg))
    #     embed.add_field(name=f"Requested by ", value=f"{ctx.author}")
    #     embed.set_footer(text="Discord: https://discord.gg/b8Sj7SS ")
    #     await ctx.respond(embed=embed)

    # @commands.command()
    # @commands.cooldown(1, 3, commands.BucketType.user)
    # async def say(self, ctx, *, msg):
    #     await ctx.message.delete()
    #     await ctx.respond("{}" .format(msg))
    #     await ctx.respond(f"Requested by {ctx.author.mention} ")
    #     print("say")

    # @commands.command()
    # @commands.cooldown(1, 3, commands.BucketType.user)
    # async def Say(self, ctx, *, msg):
    #     await ctx.message.delete()
    #     await ctx.respond("{}" .format(msg))
    #     await ctx.respond(f"Requested by {ctx.author.mention} ")
    #     print("say")

    # @commands.command()
    # @commands.cooldown(1, 3, commands.BucketType.user)
    # async def SAY(self, ctx, *, msg):
    #     await ctx.message.delete()
    #     await ctx.respond("{}" .format(msg))
    #     await ctx.respond(f"Requested by {ctx.author.mention} ")
    #     print("say")

    @commands.slash_command(name="password", description="Generates a password")
    async def _pass(self, ctx, amt: int = 2):
        try:
            nwpss = []
            lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@',
                   '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', ",", '}', ']',
                   '[', ';', ':', '<', '>', '?', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            for x in range(amt):
                newpass = random.choice(lst)
                nwpss.append(newpass)
            fnpss = ''.join(nwpss)

            e = discord.Embed(title="Attempting to generate a password for you! **Please check your direct messages!**", color=discord.Color.blue())
            await ctx.respond(embed=e)
            e = discord.Embed(title="Password generator", description=f"Your password: {fnpss}", color=discord.Color.green())
            await ctx.author.send(embed=e)
        except Exception as e:
            print(e)

    @commands.slash_command(name="8ball", description="Call upon the powers of the all knowning magic 8Ball")
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later."
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        em = discord.Embed(title='Magic 8ball!',
                           color=discord.Color.orange())
        em.add_field(name=f"**Question:** {question}",
                     value=f"**Answer:** {random.choice(responses)}")
        await ctx.respond(embed=em)

    # @commands.slash_command()
    # async def whisper(self, ctx, member: discord.Member, *, content):
    #     embed = discord.Embed(color=discord.Color.orange())
    #     embed = discord.Embed(title='Someone whispered to you!')
    #     embed.add_field(name='Message: ' + str(content),
    #                     value="From: " + str(ctx.author.mention))
    #     await member.send(embed=embed)
    #     await ctx.message.delete()

    # @commands.slash_command()
    # async def sayname(self, ctx, *,  avamember: discord.Member = None):
    #     await ctx.respond(f"Your name is {ctx.author.mention}")

    # @commands.slash_command()
    # async def count(self, ctx, channel: discord.TextChannel = None):
    #     channel = channel or ctx.channel
    #     messages = await channel.history(limit=None).flatten()
    #     count = len(messages)
    #     embed = discord.Embed(
    #         title="Total Messages",
    #         color=discord.Color.green(),
    #         description=f"There were {count} messages in {channel.mention}")
    #     await ctx.respond(embed=embed)

    # @commands.slash_command()
    # async def info(self, ctx):
    #     ping = int(self.bot.latency * 1000)
    #     guild_count = str(len(self.bot.guilds))
    #     total_member_count = 0

    #     for guild in self.bot.guilds:
    #         total_member_count += guild.member_count

    #     info_embed = discord.Embed(
    #         title="Edith Bot Information"
    #     )
    #     info_embed.set_thumbnail(url=self.bot.user.avatar_url)

    #     info_embed.add_field(
    #         name="Latency/Ping", value=f"{ping}ms", inline=False
    #     )
    #     info_embed.add_field(
    #         name="Server Count", value=guild_count, inline=False
    #     )
    #     info_embed.add_field(
    #         name="Total Member Count",
    #         value=str(total_member_count),
    #         inline=False,
    #     )
    #     await ctx.respond(embed=info_embed)


    @commands.slash_command(name="uptime", description="Get the bots uptime")
    async def uptime(self, ctx):
        now = datetime.now()
        uptime = self.launched_at - now
        humanized_time = humanize.precisedelta(uptime)
        await ctx.respond(f"I have been online for {humanized_time}")

    @commands.slash_command(name="credits", description="Shows credits for Edith")
    async def credits(self, ctx):
        embed = discord.Embed(
            title="Credits", description="**Owners**\n<@702385226407608341> and <@929270204222046249>\n\n**Developers**\n<@702385226407608341>", color=discord.Color.blue())
        await ctx.respond(embed=embed)

    @commands.slash_command(name="invite", description="Get a link to invite the bot")
    async def invite(self, ctx):
        embed = discord.Embed(
            title="Invite Me", description="[Click here!](https://discord.com/api/oauth2/authorize?client_id=731807331796385812&permissions=4281724790&scope=bot)", color=discord.Color.blue())
        await ctx.respond(embed=embed)

    @commands.slash_command(name="coinflip", description="Flip a coin")
    async def flip(self, ctx):
        choices = ["Heads", "Tails"]
        rancoin = random.choice(choices)
        await ctx.respond(rancoin)


@commands.slash_command
async def impersonate(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
        message: str,
    ):
        """
        Pretend to be another member of your server
        """

        webhook_url = Data.webhook_entry_exists(ctx.channel)

        if webhook_url:
            webhook = discord.utils.get(
                await ctx.channel.webhooks(), url=webhook_url
            )

            if not webhook:
                webhook: discord.Webhook = await ctx.channel.create_webhook(
                    name="Edith Impersonate Command",
                    reason="Impersonation Command",
                )
                Data.c.execute(
                    "UPDATE webhooks SET webhook_url = :new_url WHERE channel_id = :ch_id",
                    {"new_url": webhook.url, "ch_id": ctx.channel.id},
                )
                Data.conn.commit()

        else:
            webhook: discord.Webhook = await ctx.channel.create_webhook(
                name="Impersonate Webhook for Edith",
                reason="Impersonation Command",
            )
            Data.create_new_webhook_data(ctx.channel, webhook.url)

        await webhook.send(
            message,
            username=member.display_name,
            avatar_url=member.avatar.url,
            allowed_mentions=discord.AllowedMentions.none(),
        )
        await ctx.respond("SUS", ephemeral=True)



def setup(bot):
    bot.add_cog(slashfun(bot))