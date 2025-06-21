import random

restaurants = {
   "便當類":[
       {"name":"天盛燒臘叉燒飯","price":85},
       {"name":"阿嬤的飯桶椒麻雞便當","price":100},
       {"name":"茗松快餐碳烤雞排飯","price":80}
   ],
   "自助餐":[
       {"name":"全美自助餐","price":100},
       {"name":"素怡園","price":95}
   ],
   "健康餐":[
       {"name":"Subway厚切嫩牛六吋潛艇堡","price":143},
       {"name":"強尼兄弟蒜香椒鹽雞胸餐盒","price":109}
   ],
   "速食":[
       {"name":"漢堡王皇家華堡+a餐","price":189},
       {"name":"麥當勞雙層牛肉吉事堡+b餐","price":145}
   ],
   "滷味":[
       {"name":"藤村屋滷味","price":100},
       {"name":"A華加湯滷味","price":90}
   ]
}


no_budget_limit = ["滷味","自助餐"]


def select_lunch(budget, categories):
   all_options = []
   for category in categories:
       if category not in restaurants:
           print (f"找不到類別:{category}(請確認拼字)")
       if category in no_budget_limit:
           filtered = [r["name"] for r in restaurants[category]]
       else:
           filtered = [r["name"] for r in restaurants[category] if r ["price"] <= budget]
       all_options.extend(filtered)
   if not all_options:
       return f"這些類別在${budget}元內找不到可以吃的店家喔~"
   else:
       choice = random.choice(all_options)
       return f"今天可以吃：{choice}！"


print("可選分類：便當類、自助餐、健康餐、速食、滷味")
input_categories = input("請輸入今天想吃的類別(用逗號分隔，例如：便當類,自助餐)：")
categories = [c.strip() for c in input_categories.split(",")]

budget = int(input("請輸入今天預算(元)："))

select_lunch(budget, categories)