import openpyxl

# 创建一个Excel工作簿对象
wb = openpyxl.Workbook()

# 获取默认工作表对象
ws = wb.active


data = '''SITE NAME	STATE	COUNTRY	CONTINENT	COLOR ZONE
Badlands National Park	South Dakota	United States	North America	Dark Gray
Abisko		Sweden	Europe	Dark Gray
Bighorn Canyon National Recreation Area	Montana	United States	North America	Dark Gray
Deadman’s Basin Reservoir	Montana	United States	North America	Dark Gray
Brockway Mountain	Michigan	United States	North America	Dark Gray
Dead Horse Point State Park	Utah	United States	North America	Dark Gray
Theodore Roosevelt National Park	North Dakota	United States	North America	Dark Gray
Grand Canyon National Park	Arizona	United States	North America	Dark Gray
Mojave National Preserve	California	United States	North America	Dark Gray
AstroTelePort	New Mexico	United States	North America	Dark Gray
Lake Sugema	Iowa	United States	North America	Light Blue
Whiterock Conservancy	Iowa	United States	North America	Light Blue
Ice House Observation Plateau 1	California	United States	North America	Light Blue
Assateague Island	Maryland	United States	North America	Light Blue
Westhavelland	Brandenburg	Germany	Europe	Light Blue
Naturpark Zirbitzkogel-Grebenzen	Styria	Austria	Europe	Light Blue
Cherry Springs State Park	Pennsylvania	United States	North America	Dark Blue
Wadi Rum		Jordan	Asia	Dark Blue
Kielder Forest Park	England	United Kingdom	Europe	Dark Blue
Potato City Airport	Pennsylvania	United States	North America	Light Blue
Fetterman Monument	Wyoming	United States	North America	Light Blue
Joshua Tree National Park	California	United States	North America	Light Blue
Big Cypress National Preserve	Florida	United States	North America	Light Blue
Sleep Bear Dunes National Lakeshore	Michigan	United States	North America	Light Blue
Cloud Cap	Oregon	United States	North America	Light Blue
Buffalo National River	Arkansas	United States	North America	Dark Blue
Stephen C Foster State Park	Georgia	United States	North America	Dark Blue
Beavertail Hill State Park	Montana	United States	North America	Light Gray
Kerry International Dark Sky Reserve		Ireland	Europe	Light Gray
Park Tmavej Oblohy Poloniny		Slovakia	Europe	Light Gray
Vlasina Lake		Serbia	Europe	Light Gray
Road 54 Ocean Viewpoint		Iceland	Europe	Light Gray
Thingvellir National Park		Iceland	Europe	Dark Blue
Buffalo Springs Campground	Colorado	United States	North America	Light Gray
Amboy Crater	California	United States	North America	Light Gray
Spruce Knob	West Virginia	United States	North America	Light Gray
Dupont Reservation Conservation Area	Missouri	United States	North America	Dark Green
Spring Lake State Wildlife Area	Illinois	United States	North America	Light Green
Cleary Summit	Alaska	United States	North America	Light Green
Green River State Wildlife Area	Illinois	United States	North America	Dark Green
Staunton River State Park	Illinois	United States	North America	Dark Green
Deerlick Astronomy Village	Georgia	United States	North America	Dark Green
John Glenn Astronomy Park	Ohio	United States	North America	Dark Green
Richard Bong State Recreation Area	Wisconsin	United States	North America	Dark Orange
Torrance Barrens Dark Sky Reserve	Ontario	Canada	North America	Dark Green
Kejimkujik National Park	Nova Scotia	Canada	North America	Dark Gray
Algonquin Provincial Park	Ontario	Canada	North America	Dark Gray
Beaver Hills Dark Sky Preserve	Alberta	Canada	North America	Dark Yellow
Outlaw Cave Campground	Wyoming	United States	North America	Black
Yellowstone National Park	Wyoming	United States	North America	Black
Black Mesa State Park	Oklahoma	United States	North America	Black
Great Basin National Park	Nevada	United States	North America	Black
Big Bend National Park	Texas	United States	North America	Black
Grasslands National Park	Saskatchewan	Canada	North America	Black
'''

# 将数据按行分离，并生成二维列表
rows = [row.split('\t') for row in data.strip().split('\n')]

for row_index, row in enumerate(rows, start=1):
    for col_index, cell_value in enumerate(row, start=1):
        # 写入单元格
        ws.cell(row=row_index, column=col_index, value=cell_value)

# 保存工作簿到文件
wb.save('世界各国地区天空颜色.xlsx')
