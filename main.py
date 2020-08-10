import ctx as ctx
import discord
import asyncio

from discord.ext.commands import bot
import time






fazendo = 0
client = discord.Client()
ROLE = "「✅」 ᴡʜɪᴛᴇʟɪsᴛ"

nome =''



from discord.utils import get


@client.event
async def on_ready():
    print("BOT ONLINE")
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)

    print('------------------')



@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="「 sᴇᴍ ᴡʜɪᴛᴇʟɪsᴛ🔰 」")
    await member.add_roles(role)
    for channel in member.guild.channels:
        if str(channel) == "✈ʙᴇᴍ-ᴠɪɴᴅᴏ":
            await channel.send(f"""{member.mention} Seja Bem Vindo à nossa cidade! ❤""")


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == '🚫ᴅᴇᴘᴏʀᴛᴀᴅᴏ':
            await channel.send(f'{member.name}#{member.discriminator} E uma pena a sua saída, até mais!')


@client.event
async def on_message(message, fazendo=0):
    ch = message.channel

    jogadorId = -1
    x = 0
    
    status = []
    respostas = []
    acertos = 0
    fazendowhitelist = "fazendo-whitelist-" + str(x)
    canalExiste = 0
    for channel in message.author.guild.channels:
        if str(channel) == fazendowhitelist:
            canalExiste = 1
            break
        else:
            canalExiste = 0
            #📲fɑzer - whitelist
    if (not message.author.bot) and message.content.lower().startswith('!whitelist') and str(ch) == "whitelist" and canalExiste == 0 :
        await ch.send(
            f"""{message.author.mention} Entre no canal de texto 'fazendo-whitelist' e digite iniciar para iniciar sua whitelist""")
        guild = message.guild
        name = "📜𝘞𝘏𝘐𝘛𝘌𝘓𝘐𝘚𝘛"

        category = discord.utils.get(guild.categories,name=name)
        member = message.author
        #admin_role = get(guild.roles, name="𝐅𝐎𝐔𝐍𝐃𝐄𝐑👑")
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            message.author: discord.PermissionOverwrite(read_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            #admin_role: discord.PermissionOverwrite(read_messages=True)
        }
        #tempo para outra pessoa fazer = 10 min criar isso e limitar a criação do canal
        await guild.create_text_channel(fazendowhitelist, category = category , overwrites=overwrites)


            
        for channel in message.author.guild.channels:
            if str(channel) == fazendowhitelist:

                await channel.send("Digite iniciar para começar")
    else:
        if (not message.author.bot) and  str(ch) == "whitelist":
            await  ch.send("Alguém esta fazendo a whitelist espere alguns minutos e tente novamente")
    #criar variavel fazendo whitelist com valores de 1-100 randomicos a cada vez que criar e no str(ch) comparar c ele
    if (not message.author.bot) and str(ch) == fazendowhitelist and message.content.lower().startswith('iniciar'):

        respostasCertasUpper = ["Id", "nome", "nome de usuario", "A", "B", "A", "C", "C", "B", "A", "B", "C", "A", "A",
                                "B", "C", "A", "B"]
        respostasCertasLower = ["Id", "nome", "nome de usuario", "a", "b", "a", "c", "c", "b", "a", "b", "c", "a", "a",
                                "b", "c", "a", "b"]
        respostas = []
        channel = message.channel


        def check(m):
            if(not m.author.bot):
                respostas.append(m.content)
                return True
            else:
                return False



        try:
            await channel.send('Qual seu ID?')
            msg = await client.wait_for('message', check=check)

            await channel.send('Qual seu nome?')
            msg = await client.wait_for('message', check=check)

            await channel.send('Qual o seu nome de usuário no Discord com a #?')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'O que é PowerGaming?\nA - Realizar ações que seriam impossíveis na vida real.\nB - Reconhecer alguém pela voz.\nC - Deslogar durante uma açao.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'O que é MetaGaming?\nA - Meta Gaming é definir uma meta de quanto você consegue farmar no jogo.\nB - Receber uma mensagem fora do RP e se beneficiar dentro do jogo com as informações dessa mensagem..\nC - Disputa de território entre gangues.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'O que é anti RP?\nA - Sair do seu personagem em qualquer situação de jogo.\nB - Chamar a polícia para conversar na praça.\nC - Realizar um encontro com um amigo.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'O que é safezone?\nA - Locais em que você pode curar seus ferimentos.\nB - Locais que a polícia não pode passar.\nC - Locais em que não pode ocorrer nenhuma atividade criminosa.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'O que é VDM?\nA - Parar nos sinais vermelhos.\nB - Estacionar em locais proibidos.\nC - Usar o veículo para matar pessoas.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'O que é RDM?\nA - Realizar corridas de racha.\nB - Matar pessoas aleatoriamente sem motivo.\nC - Matar um assaltante numa operação policial.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'Para assaltar as pessoas na cidade necessita ter no mínimo quantos policiais online?\nA - 2 policiais online.\nB - 4 policiais online.\nC - Não há necessidade de policiais online.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'Durante uma perseguição policial você perde o controle do veículo e capota, o que você faria em seguida?\nA - Levanto e saio correndo a pé.\nB -  Fico jogado no chão aguardando os policiais me renderem.\nC - Ligo para o SAMU imediatamente.')
            msg = await client.wait_for('message', check=check)

            await channel.send('Qual desses locais não é safezone?\nA - Praça.\nB - Oficina.\nC - Favelas.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'O que é combat-logging?\nA - Deslogar durante uma ação.\nB - Matar todos os policiais durante uma ação.\nC - Roubar o banco central sem policiais em serviço.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'Você está em uma ação e morre, o que você faz?\nA - Aguardo o fim da ação e a chegada do SAMU.\nB - Informo a posição dos adversários aos meus amigos.\nC - Fico gritando pedindo socorro para me ajudarem.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'Durante um assalto você está sendo abordado por dois assaltantes com armas apontadas para você. O que faria?\nA - Me rendo, mas aviso aos meus amigos pelo discord.\nB - Me rendo e sigo as ordens dos criminosos.\nC - Puxo minha arma e tento matar os dois assaltantes que estão com armas apontadas para mim.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'Após um assalto você reconhece os meliantes pela voz em uma conversa na praça, qual sua atitude?\nA - Saco minha arma e mato todos para me vingar.\nB - Crio uma emboscada para que eles sejam mortos por mim.\nC - Ignoro, pois não posso reconhecer ninguém pela voz.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'Um jogador pratica AntiRP com você, o que é melhor a se fazer?\nA - Gravo e faço a denúncia formalmente no Xcord, prosseguindo com o RP.\nB - Paro todo o RP e chamo os deuses para que resolvam.\nC - Mato com uma facada quem está realizando AntiRP.')
            msg = await client.wait_for('message', check=check)

            await channel.send(
                'Você está assistindo a uma live de um streaming em nossa cidade e usa essas informações para se beneficiar no jogo. Qual o nome dessa prática?\nA - AntiRP.\nB - Metagaming.\nC - Combat logging.')
            msg = await client.wait_for('message', check=check)

        except asyncio.TimeoutError:
            await channel.send('Refaça a whitelist')
        for i in range(len(respostas)):
            if respostas[i] == respostasCertasLower[i] or respostas[i] == respostasCertasUpper[i]:
                acertos += 1

        if acertos >= 13:

            role = get(message.author.guild.roles, name=ROLE)
            role2 = get(message.author.guild.roles, name="「 sᴇᴍ ᴡʜɪᴛᴇʟɪsᴛ🔰 」")
            await message.author.add_roles(role)


            await ch.send(f"""{message.author.mention} Parabéns vc foi aprovado em breve seu id será liberado!""")
            await asyncio.sleep(10)
            await message.author.remove_roles(role2)
            if str(ch) == fazendowhitelist:
                await discord.TextChannel.delete(message.channel)
            for channel in message.author.guild.channels:
                if str(channel) == "✅ᴀᴘʀᴏᴠᴀᴅᴏs" and channel.category == discord.utils.get(message.author.guild.categories,name="📜𝘞𝘏𝘐𝘛𝘌𝘓𝘐𝘚𝘛"):
                    await channel.send("Aprovado:\n Id: "+ respostas[0] + "\n " + "Nome: "+ respostas[1] +"\n " + "Nome discord: " + respostas[2])

        else:
            await ch.send(f"""{message.author.mention} Você foi reprovado!""")
            await asyncio.sleep(10)
            if str(ch) == fazendowhitelist:
                await discord.TextChannel.delete(message.channel)
            for channel in message.author.guild.channels:
                if str(channel) == "❌ʀᴇᴘʀᴏᴠᴀᴅᴏs" and channel.category == discord.utils.get(message.author.guild.categories,name="📜𝘞𝘏𝘐𝘛𝘌𝘓𝘐𝘚𝘛"):
                    await channel.send("Reprovado:\n Id: "+ respostas[0] + "\n " + "Nome: "+ respostas[1] +"\n " + "Nome discord: " + respostas[2])





client.run(token)
