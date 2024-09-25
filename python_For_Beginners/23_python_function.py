# 扇形面积 = 圆心角度 / 360° x π x r²

# central_angle_1 = 160
# radius_1 = 30
# sector_area_1 = central_angle_1 / 360 * 3.14 * radius_1 ** 2
# print(f"此扇面积为：{sector_area_1}")
# print("此扇面积为：" + str(sector_area_1))

def calculate_sector(central_angle,radius):
    # 以下是定义的函数代码
    # central_angle = 160
    # radius = 30
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"此扇面积为：{sector_area}")
    return sector_area

sector_area_1 = calculate_sector(160,30)

sector_area_2 = calculate_sector(260,10)

sector_area_3 = calculate_sector(15,10)
