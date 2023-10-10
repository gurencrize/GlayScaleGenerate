from PIL import Image

# 16x16の画像を生成
width, height = 16, 16
image = Image.new("RGB", (width, height))

# RGB(1,1,1)からRGB(255,255,255)までの色を1つずつ生成して描画
for c in range(256):
    image.putpixel((c % 16, c // 16), (c, c, c))

# 画像を保存
image.save("glayscale.png")

# 画像を表示（オプション）
image.show()
