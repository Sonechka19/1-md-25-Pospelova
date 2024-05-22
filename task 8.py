#задание 8

# def task1():
#     from PIL import Image
#
#     def new_image(input_image, output_image, left, top, right, bottom):
#             img = Image.open(input_image)
#             neew_img = img.crop((left, top, right, bottom))
#             neew_img.save(output_image)
#
#     if name == "__main__":
#         input_image = "1.jpg"
#         output_image = "neww_img.jpg"
#         left = 406
#         top = 372
#         right = 622
#         bottom = 464
#
#         new_image(input_image, output_image, left, top, right, bottom)
# task1()
#
# def task2():
#     from PIL import Image
#     cards = {
#         "День рождения": "birthday_card.jpg",
#         "Новый год": "new_year_card.jpg",
#         "23 февраля": "23_day_card.png",
#         "8 марта": "womens_day_card.png"
#     }
#
#     holiday = input("Какой праздник вас интересует? ")
#     if holiday in cards:
#         card = cards[holiday]
#         image = Image.open(card)
#         image.show()
#     else:
#         print("К сожалению, открытки для этого праздника нет.")
# task2()