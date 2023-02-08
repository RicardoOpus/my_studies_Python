import json, csv

with open("doom.json", mode="r") as doom_classics:
    print(json.load(doom_classics)[0])


# Itering JSON:
with open("doom.json", mode="r") as doom_classics:
    doom_albums_list = json.load(doom_classics)
    for item in doom_albums_list:
        print(item["album"])


# Itering CSV:
with open("doom.csv", mode="r") as doom_classics:
    doom_albums_list = csv.DictReader(doom_classics)
    for item in doom_albums_list:
        print(item["band"])


# Wrinting JSON:
with open("doom.json") as file:
    albums = json.load(file)
pagan_albums = [
    pagan for pagan in albums if "Pagan Altar" in pagan["band"] 
]
with open("pagan_altar_albums.json", "w") as file:
    file.write(json.dumps(pagan_albums))


# Other way:
with open("pagan_altar_albums.json", "w") as file:
    json.dump(pagan_albums, file)


# Open CSV detail
with open("doom.csv", encoding="utf-8") as file:
    class_albums = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = class_albums
print(data)


group_by_band = {}
for line in data:
    band_name = line[0]
    if band_name not in group_by_band:
        group_by_band[band_name] = 0
    group_by_band[band_name] += 1


# Wrinting CSV:
with open("list_doom_bands_qty.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    header = [
        "Band",
        "Quantity"
    ]
    writer.writerow(header)

    for band, qty in group_by_band.items():
        row = [
            band,
            qty,
        ]
        writer.writerow(row)