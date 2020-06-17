from discord.ext import commands
import os
import traceback



@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send("active")


@bot.command()
async def msg(ctx, arg):
    await ctx.send(arg

+'''時開始の交流戦お相手を募集します。
こちらRovです。
主催相談、諸々あり。
#mkmg''')


@bot.command()
async def fcfuyuneko(ctx):
    await ctx.send('2380-1020-5849')

@bot.command()
async def fcwasabi(ctx):
    await ctx.send('0517-3532-9027')

@bot.command()
async def fchirase(ctx):
    await ctx.send('8506-9623-7014')

@bot.command()
async def fcten(ctx):
    await ctx.send('3526-7911-1702')

@bot.command()
async def fclotelia(ctx):
    await ctx.send('7232-9421-1827')

@bot.command()
async def fcmiya(ctx):
    await ctx.send('0259-4764-0798')

@bot.command()
async def fczero(ctx):
    await ctx.send('8290-1374-2628')

@bot.command()
async def fcpoze(ctx):
    await ctx.send('6788-3173-9789')

@bot.command()
async def fcbamos(ctx):
    await ctx.send('2710-2103-9053')

@bot.command()
async def fckirihara(ctx):
    await ctx.send('6743-9735-9003')

@bot.command()
async def fcikimono(ctx):
    await ctx.send('4561-8715-5410')

@bot.command()
async def fcakito(ctx):
    await ctx.send('8457-8576-3100')

@bot.command()
async def fcenu(ctx):
    await ctx.send('4519-0753-0991')

@bot.command()
async def fcmegafai(ctx):
    await ctx.send('6883-9102-4225')

@bot.command()
async def fc(ctx):
    if ctx.author.id == 628218157181435965: #fuyuneko
        await ctx.send("2380-1020-5849")
    elif ctx.author.id == 680026824356528142: #fuyuneko pc
        await ctx.send('2380-1020-5849')
    elif ctx.author.id == 633627369776742400: #maronsan
        await ctx.send('4016-5617-5609')
    elif ctx.author.id == 679358349128761374: #poze
        await ctx.send('6788-3173-9789')
    elif ctx.author.id == 567381167071035451: #wasabi
        await ctx.send('0517-3532-9027')
    elif ctx.author.id == 501420937267118098: #hriase
        await ctx.send('8506-9623-7014')
    elif ctx.author.id == 652141232406921263: #ten
        await ctx.send('3526-7911-1702')
    elif ctx.author.id == 651803917369212929: #lotelia
        await ctx.send('7232-9421-1827')
    elif ctx.author.id == 432749257133391895: #kirihara
        await ctx.send('6743-9735-9003')
    elif ctx.author.id == 526749691082309682: #ikimono
        await ctx.send('4561-8715-5410')
    elif ctx.author.id == 651232920014422056: #miyarin
        await ctx.send('0259-4764-0798')
    elif ctx.author.id == 545872069145919489: #zero
        await ctx.send('8290-1374-2628')
    elif ctx.author.id == 636842531828662272: #bamos
        await ctx.send('2710-2103-9053')
    elif ctx.author.id == 551406222952103937: #naru
        await ctx.send('3068-6710-6421')
    elif ctx.author.id == 362544282655129611: #メガファイ
        await ctx.send('6883-9102-4225')
    elif ctx.author.id == 552372558058487810: #アキト
        await ctx.send('8457-8576-3100')
    elif ctx.author.id == 675321641697542155: #えぬ
        await ctx.send('4519-0753-0991')
    else:
        await ctx.send('君はまだフレンドコードを登録してないよねぇ？')

@bot.command()
async def shikka(ctx):
    await ctx.send('https://discord.com/channels/664397630973018124/710788110123794432/712974401691451392')

@bot.command()
async def toad(ctx):
    await ctx.send('^mmr fuyuneko, maronsan, shikka, sharu, itto, TERU, burst, ten, ikimono, miya, hirase, ccc, Juliet, bamosu, Birucha, Shinoa')


#map
@bot.command()
async def MKS(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/e/d/ed590862.jpg') #マリカス

@bot.command()
async def WP(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/6/a/6a33f204.jpg') #ウォタパ

@bot.command()
async def SSC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/7/2/72fd79db.jpg') #スイキャニ

@bot.command()
async def TR(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/1/5/15f34362.jpg') #ドッスン遺跡

@bot.command()
async def MC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/a/d/ad580247.jpg')

@bot.command()
async def TH(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/7/2/7209cba9.jpg')

@bot.command()
async def TM(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/c/5/c511aa6b.jpg')

@bot.command()
async def SGF(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/4/5/45c75a5f.jpg')

@bot.command()
async def SA(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/4/9/49c00edc.jpg')

@bot.command()
async def DS(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/5/9/595c8772.jpg')

@bot.command()
async def Ed(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/9/d/9d9ff290.jpg')

@bot.command()
async def MW(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/9/0/90a986d6.jpg')

@bot.command()
async def CC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/b/0/b0cd1c04.jpg')

@bot.command()
async def BDD(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/9/6/96d934b6.jpg')

@bot.command()
async def BC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/c/e/cefe99d2.jpg')

@bot.command()
async def RR(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/1/4/145ee22f.jpg')

@bot.command()
async def MMM(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/f/2/f2798db7.jpg')

@bot.command()
async def rMC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/f/9/f92fb6d8.jpg')

@bot.command()
async def CCB(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/0/c/0cda8996.jpg')

@bot.command()
async def TT(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/8/a/8afff8bd.jpg')

@bot.command()
async def DDD(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/2/f/2f5c14cd.jpg')

@bot.command()
async def DP3(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/3/c/3cdd7ff1.jpg')

@bot.command()
async def rRRy(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/5/f/5f9ce995.jpg')

@bot.command()
async def DKJ(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/c/4/c4a47802.jpg')

@bot.command()
async def WS(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/0/7/07fc914a.jpg')

@bot.command()
async def SL(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/0/a/0a0d8531.jpg')

@bot.command()
async def MP(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/2/d/2d48ca59.jpg')

@bot.command()
async def YV(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/b/1/b11cd77b.jpg')

@bot.command()
async def rTTC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/2/d/2df0e550.jpg')

@bot.command()
async def PPS(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/8/4/84c5073c.jpg')

@bot.command()
async def GV(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/8/7/877d953c.jpg')

@bot.command()
async def rRRd(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/5/a/5a7e0143.jpg')

@bot.command()
async def dYC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/6/f/6f0da888.jpg')

@bot.command()
async def dEA(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/1/e/1ee7a21b.jpg')

@bot.command()
async def dDD(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/a/9/a92cd120.jpg')

@bot.command()
async def dMC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/a/2/a29683e1.jpg')

@bot.command()
async def dWGM(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/e/9/e903662a.jpg')

@bot.command()
async def dRR(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/8/8/882f1441.jpg')

@bot.command()
async def dIIO(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/1/e/1e695700.jpg')

@bot.command()
async def dHC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/a/9/a94e7e1d.jpg')

@bot.command()
async def dBP(ctx):
    await ctx.send('no data')

@bot.command()
async def dCL(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/6/2/629a932d.jpg')

@bot.command()
async def dWW(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/2/c/2c5c229c.jpg')

@bot.command()
async def dAC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/c/6/c63a9866.jpg')

@bot.command()
async def dNBC(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/9/1/912a504d.jpg')

@bot.command()
async def dRiR(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/c/2/c29b5957.jpg')

@bot.command()
async def dSBS(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/e/2/e2efafa8.jpg')

@bot.command()
async def dBB(ctx):
    await ctx.send('https://livedoor.blogimg.jp/nim_2525/imgs/d/9/d9ee2a3d.jpg')


@bot.command()
async def list(ctx):
    embed = discord.Embed(title="コマンドリスト", description="""^fc      自分のフレンドコードを表示
^fcXX    XXのフレンドコードを表示
^XXX     コースXXXのアイテムテーブルを表示
^msg XX  XX時の外交文を表示
^toad    全員分のmmr検索文を表示""", color=0x2bc5ba) #16進数カラーコード
    embed.add_field(name="挙手コマンド", value="""!cXX        XX時に挙手する
!dXX      XX時の挙手を下げる
!rXX      XX時のメンバーをリセットする
!rall     21-23のメンバーをリセットする
!mlXX     XX時のメンバーを確認する
!mlall    21-23のメンバーを確認する
!a        みんなに呼びかけ
!X        @X人を募集する""", inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def listfc(ctx):
    embed = discord.Embed(title="フレンドコードリスト", description="""^fcfuyuenko
^fcwasabi
^fchirase
^fcten
^fclotelia
^fcmiya
^fczero
^fcpoze
^fcbamos
^fcikimono
^fckirihara
^fcakito
^fcenu
^fcmegafai""", color=0x2bc5ba) #16進数カラーコード
    await ctx.send(embed=embed)



bot.run(token)
