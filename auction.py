lots = [
  { "title": "Vintage Rolex Submariner", "tags": ["watches", "vintage", "luxury"], "estimation_range": [5000, 8000], "seller_id": "s1" },
  { "title": "Antique Ming Dynasty Vase", "tags": ["ceramics", "antique", "asian art"], "estimation_range": [1500, 2500], "seller_id": "s2" },
  { "title": "Contemporary Abstract Painting", "tags": ["art", "modern", "painting"], "estimation_range": [400, 600], "seller_id": "s1" },
  { "title": "Gold Roman Coin", "tags": ["coins", "antique", "roman"], "estimation_range": [300, 500], "seller_id": "s2" },
  { "title": "Art Deco Diamond Ring", "tags": ["jewelry", "art deco", "diamond"], "estimation_range": [2000, 3000], "seller_id": "s3" },
  { "title": "Vintage Omega Speedmaster", "tags": ["watches", "vintage", "chronograph"], "estimation_range": [3500, 4500], "seller_id": "s4" },
  { "title": "Signed Picasso Lithograph", "tags": ["art", "modern", "signed"], "estimation_range": [1200, 1800], "seller_id": "s5" },
  { "title": "18th Century Silver Spoon", "tags": ["silver", "antique", "cutlery"], "estimation_range": [100, 200], "seller_id": "s2" },
  { "title": "Vintage Chanel Handbag", "tags": ["fashion", "vintage", "designer"], "estimation_range": [900, 1200], "seller_id": "s3" },
  { "title": "Classic Car Model 1965", "tags": ["cars", "vintage", "collectibles"], "estimation_range": [8000, 10000], "seller_id": "s6" }]


# print(type(lots[0].items()))
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []


for lot in lots:
    if lot["seller_id"] == "s1":
        s1.append(lot["title"])
        s1.append(lot["estimation_range"])
        

    elif lot["seller_id"] == "s2":
        s2.append(lot["title"])
        s2.append(lot["estimation_range"])

    elif lot["seller_id"] == "s3":
        s3.append(lot["title"])
        s3.append(lot["estimation_range"])

    elif lot["seller_id"] == "s4":
        s4.append(lot["title"])
        s4.append(lot["estimation_range"])

    elif lot["seller_id"] == "s5":
        s5.append(lot["title"])
        s5.append(lot["estimation_range"])

    elif lot["seller_id"] == "s6":
        s6.append(lot["title"])
        s6.append(lot["estimation_range"])

print("s1 = " , s1 , "s2 = " ,s2 , "s3 = " , s3)
'''
output should be a list of auctions and the criteria is
- an auction 1-3 lots
- all lots in the action should be from the same seller
- a lot can be a part of only one auction
- auction 1 ,with seller id, list of lots
2:20
auction [<lot1>, <lot>],
    s2
}
auction_1 = {
  title: "auction 1",
  seller_id: 's1',
  lots: [lot_1, lot2]
}

Step 1:
dictionary => 
lots_by_seller = {
    s1 => [<lot1>, <lot3>],
    s2: [<lot2>]
}

Step 2

list_of_auctions = [auction_1, auction_2]
'''
'''
#print(lots)
#print(type(lots))
seller_id1 = ["s1: ", ([5000, 8000], "Vintage Rolex Submariner")]
# seller_id1 = [("s1: ", (lot["estimation_range"],lot["title"]) for lot in lots if lot["seller_id"] == "s1"]
seller_id2 = [  print("s2: ",(lot["estimation_range"],lot["title"])) for lot in lots if lot["seller_id"] == "s2"]
seller_id3 = [ print("s3: ",(lot["estimation_range"],lot["title"])) for lot in lots if lot["seller_id"] == "s3"]
seller_id4 = [ print("s4: ",(lot["estimation_range"],lot["title"])) for lot in lots if lot["seller_id"] == "s4"]
seller_id5 = [ print("s5: ",(lot["estimation_range"],lot["title"])) for lot in lots if lot["seller_id"] == "s5"]
seller_id6 = [ print("s6: ",(lot["estimation_range"],lot["title"])) for lot in lots if lot["seller_id"] == "s6"]


# lots_with_ids = [seller_id1,seller_id2,seller_id3,seller_id4,seller_id5,seller_id6]
# lots_with_ids = []
print("....")
print(seller_id1)
# print(lots_with_ids)
#sorted_list_ids = [sorted_list_ids.append(sorted_list_ids) for sorted_list_ids in lots_with_ids if ]

print(len(lots_with_ids))

for item in lots_with_ids:
    print(item[0])
'''
