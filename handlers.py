from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import time 


router = Router()


# @router.message()
# async def greeting(mess:Message):
#     await mess.send_copy()


@router.message(F.text == "харош")
@router.message(F.text == "Харош")
@router.message(F.text == "молодец")
@router.message(F.text == "Молодец")
async def good_answer(mess:Message):
    await mess.answer("Thanks, man")

@router.message(F.text == "важные")
@router.message(F.text == "Важные")
async def important_finding(mess:Message):
    global peoples
    peoples = "Ваня - @sednp0_o\n" + "Илюха - @awesome_helzi\n" + "Даник Картошка - @thesquadwq\n" + "Лапшинтель - @Romulik_love\n"
    
    await mess.answer(str(peoples))


@router.message(Command('lets_talk'))
async def start_talking(mess:Message):
    await mess.answer(input('mess: '))


@router.message(Command('ya_ghoul'))
async def ghouling(mess:Message):
    global a
    a = 1000

    while a > 6:
        await mess.answer(f"{a}-7")
        a -= 7
        time.sleep(0.01)
    await mess.answer('6')
    await mess.answer('ya_ghoul')


@router.message(F.text == "Как дела?")
@router.message(F.text == "как дела?")
@router.message(F.text == "Как ты?")
@router.message(F.text == "как ты?")
@router.message(Command('how_are_you'))
async def replying_to_user(mess:Message):
    await mess.answer("Hawayou")


@router.message(F.text == "Привет")
@router.message(F.text == "привет")
@router.message(CommandStart())
async def starting_dialog(mess:Message):
    await mess.answer("Wassup, man")


@router.message(Command('stop'))
@router.message(F.text == "пока")
@router.message(F.text == "Пока")
async def ending_chating(mess:Message):
    await mess.answer("OK")
    await mess.answer("Bye, man")


@router.message(F.text.is_not(""))
async def except_finding(mess:Message):
    await mess.answer("Ne ponyal")

    