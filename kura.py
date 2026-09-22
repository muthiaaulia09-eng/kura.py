import turtle

# Membuka layar untuk menggambar
layar = turtle.Screen()
layar.title("Contoh Gambar Turtle")
layar.bgcolor("black")

# Membuat objek turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("cyan")
pen.speed(3)

# Menggambar persegi
for _ in range(4):
    pen.forward(100)  # Maju 100 piksel
    pen.left(90)      # Belok kiri 90 derajat

# Menjaga agar jendela tidak langsung tertutup
turtle.done()

# ini kura-kura