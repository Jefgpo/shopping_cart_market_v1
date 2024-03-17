# Importaciones
from tkinter import *
from tkinter import messagebox
import os
from PIL import ImageTk, Image

# ---- Carga de directorios -----
main_directory = os.path.dirname(__file__)


# Carpeta de imágenes
images_directory = os.path.join(main_directory, "images")
wallpaper_img_directory = os.path.join(images_directory, "wallpaper_img")
#print(front_img_directory)



# Creación de los diccionarios principales: Producto y depósito 
product_dictionary = {}
store_dictionary = {}

# Esta función procesa una lista de líneas que representan productos, 
# Crea un diccionario para cada producto y luego los añade a un diccionario principal.
def add_lines(lines):
    global product_dictionary
    product_list = []
    my_first_dictionary = {}
    for j in range(len(lines)):
        product_list = lines[j].split()
        product_dictionary = {product_list[0]:{"precio":float(product_list[1]), "stock":int(product_list[2])}}
        my_first_dictionary.update(product_dictionary)
        print(my_first_dictionary)
        print("******************************")


def write_file():
    file = open("stock.txt", "w")
    for i in product_dictionary:
        file.write(i)
        file.write(" ")
        for j in product_dictionary[i]:
            file.write(str(product_dictionary[i][j]))
            file.write(" ")
        file.write("\n")
    file.close()


def read_file():
    file = open("stock.txt", "r")
    lines = file.readlines()
    file.close()
    add_lines(lines)


def product_validation(x):
    if x in product_dictionary:
        messagebox.showwarning(" Bien ","¡El producto se encuentra ingresado!")
    else:
        messagebox.showwarning(" Error ","¡Producto no ingresado!")

# revisar esta función mañana ya que da keyerror
# def check_stock():
#     my_check_stock_window = Tk()
#     my_check_stock_window.title("Stock")
#     my_check_stock_window.geometry("500x350")
#     my_check_stock_window.config(bg = "spring green")

#     for i in product_dictionary:
#         if i in product_dictionary: #error en linea 53
#             print(i + " precio: " + str(product_dictionary[i]["precio"]) + "---- stock: " + str(product_dictionary[i]["stock"]))
#             my_check_stock_label = Label(my_check_stock_window, text = i + " precio: " + str(product_dictionary[i]["precio"]) + "---- stock: " + str(product_dictionary[i]["stock"]))
#             my_check_stock_label.pack()


def check_stock():
    my_check_stock_window = Tk()
    my_check_stock_window.title("Stock")
    my_check_stock_window.geometry("500x350")
    my_check_stock_window.config(bg = "spring green")
    my_check_stock_window.iconbitmap(os.path.join(images_directory, "shopping_cart.ico"))

    for i in product_dictionary:
        print(i + " precio: " + str(product_dictionary[i]["precio"]) + "---- stock: " + str(product_dictionary[i]["stock"]))
        my_check_stock_label = Label(my_check_stock_window, text = i + " precio: " + str(product_dictionary[i]["precio"]) + "---- stock: " + str(product_dictionary[i]["stock"]))
        my_check_stock_label.pack()


def check_product():
    def authenticate_product():
        verfication = verify_product.get()
        product_validation(verfication)
        my_verification_window.destroy()

    my_verification_window = Tk()
    my_verification_window.title("Verificando producto")
    my_verification_window.geometry("480x200")
    my_verification_window.config(bg="spring green")
    my_verification_window.resizable(0,0)
                
    my_verification_window.iconbitmap(os.path.join(images_directory, "shopping_cart.ico"))

    my_check_product_label = Label( my_verification_window, text = "Ingrese el nombre del producto: ", fg="black")
    my_check_product_label.grid(row=0, column=0)
    verify_product = Entry(my_verification_window)
    verify_product.grid(row= 0, column = 2)

    my_verification_btn = Button(
        my_verification_window, 
        text= "Verificar", 
        fg = "snow", 
        width = 20, 
        height= 3, 
        bd = 1, 
        bg = "tomato", 
        cursor = "hand2",
        command= authenticate_product)
    my_verification_btn.grid(row = 3, column = 2, padx = 5, pady = 5)
    
    

def get_product(x,y,z):
    if x in product_dictionary:
        messagebox.showwarning("El producto ya existe.")
    else:
        product_dictionary.update({x:{"precio":y, "stock":z}})


def add_product():
    def get_product_information():
        my_first_product = product_input.get() #problema con esta linea, verificar mañana
        my_first_price = float(price_input.get())
        my_first_stock = int(stock_input.get())

        if my_first_stock > 0:
            get_product(my_first_product, my_first_price, my_first_stock)
            my_add_product_window.destroy()
        else:
            messagebox.showwarning("La cantidad no es válida.")

    my_add_product_window = Tk()
    my_add_product_window.title("Alta de producto")
    my_add_product_window.geometry("300x200")
    my_add_product_window.config(bg="spring green")

    my_add_product_window.iconbitmap(os.path.join(images_directory, "shopping_cart.ico"))

    my_product_label = Label(my_add_product_window, text="Nombre del producto: ")
    my_product_label.grid(row=1,column=1)
    product_input = Entry(my_add_product_window)
    product_input.grid(row=1, column=2)
    
    my_price_label = Label(my_add_product_window, text="Precio: ")
    my_price_label.grid(row=2, column=1)
    price_input = Entry(my_add_product_window)
    price_input.grid(row = 2, column = 2)

    my_stock_label = Label(my_add_product_window, text="Stock: ")
    my_stock_label.grid(row= 3, column=1)
    stock_input = Entry(my_add_product_window)
    stock_input.grid(row=3,column=2)

    my_first_btn = Button(
        my_add_product_window, 
        text = "Ok", 
        fg = "snow",
        width = 20,
        height= 3,
        bd = 0,
        bg = "tomato",
        cursor = "hand2",
        command = get_product_information
        )
    my_first_btn.grid(row = 4, column= 2, padx = 10, pady=10)
    my_add_product_window.resizable(0,0)
        
def cart_market(price, stock):
    global store_dictionary
    cart_market_total = 0
    if price in product_dictionary:
        store_dictionary.update({price:{"precio":product_dictionary[price]["precio"], "stock":stock}})
        print(store_dictionary)
        cart_market_total = product_dictionary[price]["precio"] * stock
        print(f"El precio sería: {cart_market_total}")
    else:
        messagebox.showwarning("El producto no existe")


#Ver carrito 
def include_product():
    def calculate_product():
        new_product = product_added.get()
        add_stock = int(stock_added.get())
        if add_stock <= product_dictionary[new_product]["stock"] and add_stock > 0: #problema con stock
            cart_market(new_product, add_stock)
            my_cart_market_window.destroy()
        else:
            messagebox.showwarning("El stock no es el correcto.")
            my_cart_market_window.destroy()

    my_cart_market_window = Tk()
    my_cart_market_window.title("Agregar producto")
    my_cart_market_window.geometry("400x260")
    my_cart_market_window.config(bg="spring green")
    my_cart_market_window.resizable(0,0)

    my_cart_market_window.iconbitmap(os.path.join(images_directory, "shopping_cart.ico"))
    
    my_cart_market_product_label = Label(my_cart_market_window, text="Nombre del producto: ")
    my_cart_market_product_label.grid(row=0,column=1)
    product_added = Entry(my_cart_market_window)
    product_added.grid(row = 0, column = 2)

    my_cart_market_stock_label = Label (my_cart_market_window, text= "Stock: ")
    my_cart_market_stock_label.grid(row=1, column=1)
    stock_added = Entry(my_cart_market_window)
    stock_added.grid(row = 1, column= 2)

    my_second_btn = Button(
        my_cart_market_window,
        text = "Agregar",
        fg = "snow",
        width = "20",
        height = 3,
        bd = 1,
        bg = "tomato",
        cursor = "hand2",
        command = calculate_product
        )
    my_second_btn.grid(row = 3, column = 1, padx = 10, pady = 10)


def empty_cart():
    def empty():
        store_dictionary.clear()
        my_empty_cart_window.destroy()
    global store_dictionary
    my_empty_cart_window = Tk()
    my_empty_cart_window.title("Estado del carrito")
    my_empty_cart_window.geometry("300x300")
    my_empty_cart_window.config(bg="spring green")
   
    my_empty_cart_window.iconbitmap(os.path.join(images_directory, "shopping_cart.ico"))

    for i in store_dictionary:
        print(i + " Precio: " + str(store_dictionary[i]["precio"]) + "---- stock: " + str(store_dictionary[i]["stock"]))
        my_cart_market_state_label = Label(
            my_empty_cart_window,
            text= i+" precio: " + str(store_dictionary[i]["precio"]) + "---- stock: " + str(store_dictionary[i]["stock"]))
        my_cart_market_state_label.pack()

    reset_btn = Button(my_empty_cart_window, 
                       text="Vaciar",
                       fg= "snow",
                       width=20,
                       height=20,
                       bd = 0,
                       bg="tomato",
                       cursor = "hand2",
                       command=empty
                       )
    reset_btn.pack(padx = 0, pady = 100)

def pay():
    global store_dictionary
    global product_list

    def paid():
        for i in store_dictionary:
            product_dictionary[i]["stock"] = product_dictionary[i]["stock"] - store_dictionary[i]["stock"]
        
        file = open("sells.txt", "a")
        for i in store_dictionary:
            file.write(i)
            file.write(" ")
            for j in store_dictionary[i]:
                file.write(str(store_dictionary[i][j]))
                file.write(" ")
                file.write("\n")
        file.close()

        store_dictionary.clear()
        my_pay_window.destroy()
    
    my_pay_window = Tk()
    my_pay_window.title("Pagar")
    my_pay_window.geometry("400x400")
    my_pay_window.config(bg="spring green")
    my_pay_window.resizable(0,0)

    my_pay_window.iconbitmap(os.path.join(images_directory, "shopping_cart.ico"))

    total = 0
    sum = 0
    for i in store_dictionary:
        print(i + " precio: " + str(store_dictionary[i]["precio"]) + " ---- stock: " + str(store_dictionary[i]["stock"]))
        my_cart_market_state_label = Label(
            my_pay_window,
            text= i+" precio: " + str(store_dictionary[i]["precio"]) + " ---- stock: " + str(store_dictionary[i]["stock"]))
        my_cart_market_state_label.pack()

    for i in store_dictionary:
        total = store_dictionary[i]["precio"] * store_dictionary [i]["stock"]
        sum = sum + total
    print(f"El total de su compra es: {sum}")

    pay_product = Label(my_pay_window, text= "El precio total de su compra es: " + str(sum))
    pay_product.pack(padx=0, pady=100)

    pay_btn = Button(my_pay_window, 
                    text= "Pagar",
                    fg = "snow",
                    width= 20,
                    height= 3,
                    bd = 0,
                    bg = "tomato",
                    cursor = "hand2",
                    command = paid
                    )
    pay_btn.pack(padx = 10, pady = 10)

def exit():
    root.destroy()


# Interfaz de botones y root
root = Tk()
root.title("Mini-market: 'La Sardinilla de Lewis' ")
root.geometry("720x480")
root.config(bg="spring green")
root.resizable(0,0)

# Ícono de la ventana
root.iconbitmap(os.path.join(images_directory, "shopping_cart.ico"))


#Carga de imagen del fondo y el título
wallpaper = ImageTk.PhotoImage(Image.open(os.path.join(wallpaper_img_directory, "stardew_valley_wallpaper.jpg")))
wallpaper_label = Label(image=wallpaper)
wallpaper_label.place(x=0, y=0, relwidth=1, relheight=1)

title_resized = Image.open(os.path.join(wallpaper_img_directory, "title_la_sardinilla.jpg"))

title_resized = title_resized.resize((400,200), Image.LANCZOS)
title_img = ImageTk.PhotoImage(title_resized)

title_img_label = Label(image = title_img)
title_img_label.place(x=150, y=50)

# Frame de botones
my_buttons_frame = Frame(root, width = 312, height = 50, bg = "spring green" )
my_buttons_frame.pack(side = BOTTOM)

first_frame_btn = Button(my_buttons_frame, 
                        text= "Ver stock", 
                        fg = "snow",
                        width = 20,
                        height = 3,
                        bd = 0,
                        bg = "tomato",
                        cursor = "hand2",
                        command = check_stock
                        ).grid(row = 3, column = 1, padx = 10, pady = 10)

second_frame_btn = Button(my_buttons_frame, 
                        text= "Registrar producto", 
                        fg = "snow",
                        width = 20,
                        height = 3,
                        bd = 0,
                        bg = "tomato",
                        cursor = "hand2",
                        command = add_product
                        ).grid(row = 2, column = 0, padx = 10, pady = 10)

third_frame_btn = Button(my_buttons_frame, 
                        text= "Guardar stock", 
                        fg = "snow",
                        width = 20,
                        height = 3,
                        bd = 0,
                        bg = "tomato",
                        cursor = "hand2",
                        command = write_file
                        ).grid(row = 2, column = 1, padx = 10, pady = 10)

fourth_frame_btn = Button(my_buttons_frame, 
                        text= "Cargar stock", 
                        fg = "snow",
                        width = 20,
                        height = 3,
                        bd = 0,
                        bg = "tomato",
                        cursor = "hand2",
                        command = read_file
                        ).grid(row = 2, column = 2, padx = 10, pady = 10)

fifth_frame_btn = Button(my_buttons_frame, 
                        text= "Ver productos", 
                        fg = "snow",
                        width = 20,
                        height = 3,
                        bd = 0,
                        bg = "tomato",
                        cursor = "hand2",
                        command = check_product
                        ).grid(row = 3, column = 0, padx = 10, pady = 10)

sixth_frame_btn = Button(my_buttons_frame, 
                        text= "Añadir al carrito", 
                        fg = "snow",
                        width = 20,
                        height = 3,
                        bd = 0,
                        bg = "tomato",
                        cursor = "hand2",
                        command = include_product
                        ).grid(row = 3, column = 2, padx = 10, pady = 10)

seventh_frame_btn = Button(my_buttons_frame, 
                        text= "Vaciar carrito", 
                        fg = "snow",
                        width = 20,
                        height = 3,
                        bd = 0,
                        bg = "tomato",
                        cursor = "hand2",
                        command = empty_cart
                        ).grid(row = 4, column = 0, padx = 10, pady = 10)

eighth_frame_btn = Button(my_buttons_frame, 
                        text= "Pagar", 
                        fg = "snow",
                        width = 20,
                        height = 3,
                        bd = 0,
                        bg = "tomato",
                        cursor = "hand2",
                        command = pay
                        ).grid(row = 4, column = 1, padx = 10, pady = 10)

ninth_frame_btn = Button(my_buttons_frame, 
                        text= "Salir", 
                        fg = "snow",
                        width = 20,
                        height = 3,
                        bd = 0,
                        bg = "tomato",
                        cursor = "hand2",
                        command = exit
                        ).grid(row = 4, column = 2, padx = 10, pady = 10)


root.mainloop()