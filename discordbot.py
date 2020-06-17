from discord.ext import commands
import os
import traceback
import random

import gspread

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成。
from oauth2client.service_account import ServiceAccountCredentials

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定）
credentials = ServiceAccountCredentials.from_json_keyfile_name('search-mmr-3f65772d0602.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログイン。
gc = gspread.authorize(credentials)

#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納。
MMR_TEST = '1apt2Xo022Qp4PTx9S-wW9Re5Y7xcyZS1mmqCk-79JlI'
WR_LIST = '13rQVbu_VtcYA9iAmODcmncRDGgpMvHqSnkDBrt51cOg'
Rov_Result = '1ko9o7rUdIlQY9SmvTelz-KDEFpx6GVsrHkbPh9t8bW4'
Rov_kyosyu = '16CDFebCUZIughEDXF9sUAu2Sc49cPw34NVEPQqPPQB0'

#Rov mmrのシート1を開く
worksheet = gc.open_by_key(MMR_TEST).sheet1

#wr mrのシート1を開く
wrsheet = gc.open_by_key(WR_LIST).sheet1

#wr mrのfriendcodeシートを開く
fc_sheet = gc.open_by_key(WR_LIST)
friendcode_sheet = fc_sheet.worksheet('friend code')

#Rov_resultのresultシートを開く
rovresult = gc.open_by_key(Rov_Result)
result_sheet = rovresult.worksheet('Result')

#Rov_resutのシート１を開く
rov_result = gc.open_by_key(Rov_Result).sheet1

#Rovの挙手シートを開く
rov_kyosyu = gc.open_by_key(Rov_kyosyu).sheet1

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
