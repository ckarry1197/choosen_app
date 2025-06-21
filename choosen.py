#學餐選擇器 ver.1
#import random

# meals = ["7-11", "全家", "小木屋鬆餅", "Subway",
#         "太祖魷魚羹", "和食軒丼飯", "拉亞漢堡", "果汁甜品吧",
#         "阿嬤的飯桶", "素怡園", "茶壜","茗松","強尼兄弟健康廚房",
#         "這家咖啡","藤村屋滷味","粥","比司多","奶油廚房",
#         "李記小館","御膳堂鴨肉飯","細鳳果茶","義早早午餐","漢堡王",
#         "蕓泰閣東南亞料理","A華滷味","CL水果大亨","天晟燒臘","全美自助餐",
#         "翁記滷肉飯","麥當勞","極麵道","路易莎"]

#def random_meal():
#    return random.choice(meals)

#if __name__ == "__main__":
#    print(random_meal())

#-----學餐選擇器 ver.2----------------------------------------------------
#import random

#restaurant={
#    "7-11":["研三舍","二餐"],"全家":["研三舍","女二舍"],"比司多":["研三舍","女二舍"],
#    "小木屋鬆餅":["小木屋鬆餅"],"Subway":["二餐"],"茗松":["二餐"],
#    "太祖魷魚羹":["二餐"],"拉亞漢堡":["二餐"],"強尼兄弟健康廚房":["二餐"],
#    "和食軒丼飯":["二餐"],"果汁甜品吧":["二餐"],
#    "阿嬤的飯桶":["二餐"], "素怡園":["二餐"], "茶壜":["二餐"],
#    "這家咖啡":["二餐"],"藤村屋滷味":["二餐"],"粥":["二餐"],
#    "奶油廚房":["研三舍"],"李記小館":["研三舍"],"御膳堂鴨肉飯":["研三舍"],
#    "細鳳果茶":["研三舍"],"義早早午餐":["研三舍"],"漢堡王":["研三舍"],
#    "蕓泰閣東南亞料理":["研三舍"],"A華滷味":["女二舍"],"CL水果大亨":["女二舍"],
#    "天晟燒臘":["女二舍"],"全美自助餐":["女二舍"],"翁記滷肉飯":["女二舍"],
#    "極麵道":["女二舍"],"路易莎":["女二舍"]}

#def recommend_restaurant():
#    name = random.choice(list(restaurant.keys()))
#    location = random.choice(restaurant[name])
#    print(f"吃：{name}_位於{location}")

#if __name__ == "__main__":
#    recommend_restaurant()

#---------學餐選擇器 ver3.-------------------------------------------------
import json
import random

def restaurant_load():
    with open('restaurant.json', 'r',encoding='utf-8') as f:
        restaurants = json.load(f)
    return restaurants

def choose_categories(categories):
    print('您現在想吃：')
    for i, cat in enumerate(categories, 1):
        print(f'{i}. {cat}')
    while True:
        try:
            choice = int(input("請輸入編號："))
            if 1 <= choice <= len(categories):
                return categories[choice-1]
            else:
                print("輸入錯誤，請輸入有效編號")
        except ValueError:
            print("輸入錯誤，請輸入數字")

def recommend_restaurant(restaurants, selected_category):
    options = restaurants.get(selected_category, [])
    if not options:
        return None
    restaurant = random.choice(options)
    print(f"您的選擇是：{selected_category}")
    print(f"推薦您吃：{restaurant['餐廳名稱']}")
    print(f"它位於：{restaurant['餐廳位置']}")
    return restaurant

if __name__ == '__main__':
    filename = "restaurant.json"
    restaurant = restaurant_load()
    categories = list(restaurant.keys())
    selected = choose_categories(categories)
    recommend_restaurant(restaurant, selected)