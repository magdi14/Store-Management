from tkinter import *
import sqlite3
import tkinter.messagebox


conn = sqlite3.connect(r"C:\Users\Zayeef\PycharmProjects\store\db\store.db")
cur = conn.cursor()

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Add to database", font="arial 40 bold", fg="black")
        self.heading.place(x=300, y=0)


        #Form Labels
        self.product_name = Label(master, text="Product name: ", font="arial 20 bold")
        self.cost_price = Label(master, text="Product cost price: ", font="arial 20 bold")
        self.sell_price = Label(master, text="Product sell price: ", font="arial 20 bold")
        self.stock = Label(master, text="Product stock: ", font="arial 20 bold")
        self.product_name.place(x=0, y=70)
        self.cost_price.place(x=0, y=120)
        self.sell_price.place(x=0, y=170)
        self.stock.place(x=0, y=220)

        #Form Entries
        self.product_name_e = Entry(master, width=25, font='arial 18 bold')
        self.product_name_e.place(x=300, y=70)
        self.cost_price_e = Entry(master, width=25, font='arial 18 bold')
        self.cost_price_e.place(x=300, y=120)
        self.sell_price_e = Entry(master, width=25, font='arial 18 bold')
        self.sell_price_e.place(x=300, y=170)
        self.stock_e = Entry(master, width=25, font='arial 18 bold')
        self.stock_e.place(x=300, y=220)

        #Submit Button
        self.btn_add = Button(master, text="Add", width=25, height=2, bg='#86eba1', fg='#343438', command=self.getInputs)
        self.btn_add.place(x=300, y=280)

        #Reset btn
        self.btn_reset = Button(master, text="Reset", width=18, height=2, bg='#e64747', fg='#343438',
                              command=self.reset)
        self.btn_reset.place(x=490, y=280)

        #Show All Products
        self.btn_getAll = Button(master, text="Show All Products", width=25, height=2, bg='#7d65e6', fg='#343438',
                                command=self.getAll)
        self.btn_getAll.place(x=640, y=400)

        # Clear btn
        self.btn_clear = Button(master, text="Clear", width=18, height=2, bg='#e64747', fg='#343438',
                                command=self.clear)
        self.btn_clear.place(x=830, y=400)

        #TextBox for updates
        self.txBox = Text(master, width=40, height=20)
        self.txBox.place(x=640, y=70)

    def getInputs(self, *args, **kwargs):
        self.product_name = self.product_name_e.get()
        self.stock = self.stock_e.get()
        self.sell_price = self.sell_price_e.get()
        self.cost_price = self.cost_price_e.get()
        self.total_cost_price = float(self.cost_price) * float(self.stock)
        self.total_sell_price = float(self.sell_price) * float(self.stock)


        if self.product_name == '' or self.stock == '' or self.cost_price == '' or self.sell_price == '':
            tkinter.messagebox.showinfo("Error", "Please fill all the atributes!")
        else:
            q = "INSERT INTO inventory(product_name, cost_price, sell_price, stock, total_sell_price, total_cost_price) VALUES(?, ?, ?, ?, ?, ?) "
            cur.execute(q, (self.product_name, self.cost_price, self.sell_price, self.stock,
                            self.total_sell_price, self.total_cost_price))
            conn.commit()
            self.clear()
            self.txBox.insert(END, "\nInserted " + str(self.product_name) + " into db.")
            tkinter.messagebox.showinfo("Success", "Added to database successfully!")

    def reset(self, *args, **kwargs):
        self.product_name_e.delete(0, END)
        self.cost_price_e.delete(0, END)
        self.sell_price_e.delete(0, END)
        self.stock_e.delete(0, END)


    def getAll(self,*args, **kwargs):
        q = "SELECT * from inventory"
        products = cur.execute(q)
        self.clear()
        self.txBox.insert(END, "All Products:\n")
        for product in products:
            self.txBox.insert(END, "\nProduct no.: " + str(product[0])+"\n" + "Product Name: "+str(product[1])+"\n" + "Cost price: "+str(product[2])+"\n" +"Sell Price: " + str(product[3])+"\n" +"Stock: " +str(product[4])+"\n")

    def clear(self, *args, **kwargs):
        self.txBox.delete(1.0, END)



root = Tk()
master = Database(root)

root.geometry("1000x480+0+0")
root.title("Add to database")
root.mainloop()


