from osgeo import gdal

# 打开tif文件
dataset = gdal.Open(r"预处理后的2012-2020年NPP-VIIRS夜光遥感数据\VV2019_C500.tif")

# 获取图像宽度和高度
width = dataset.RasterXSize
height = dataset.RasterYSize

# 获取图像的波段数
band_count = dataset.RasterCount

# 打印图像信息
print(f"Image size: {width} x {height}, number of bands: {band_count}")

# 读取像素值
for i in range(1, band_count+1):
    band = dataset.GetRasterBand(i)
    band_array = band.ReadAsArray(0, 0, width, height)
    print(f"Band {i} pixel values: {band_array}")
