from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect(r"C:\Users\Zayeef\PycharmProjects\store\db\store.db")
cur = conn.cursor()


class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Update the database", font="arial 40 bold", fg="black")
        self.heading.place(x=300, y=0)

        # Form Labels
        self.id = Label(master, text="Search by ID: ", font="arial 20 bold")
        self.id.place(x=0, y=70)
        # Search button
        self.btn_search = Button(master, text="Search", width=18, height=2, bg='#87b5ed', fg='#343438',
                                 command=self.getSearchData)
        self.btn_search.place(x=390, y=110)

        # Search Entry
        self.id_en = Entry(master, width=25, font="arial 18 bold")
        self.id_en.place(x=300, y=70)

        # Log for updates
        self.txBox = Text(master, width=40, height=20)
        self.txBox.place(x=640, y=70)

        # Show All Products
        self.btn_getAll = Button(master, text="Show All Products", width=25, height=2, bg='#7d65e6', fg='#343438',
                                 command=self.getAll)
        self.btn_getAll.place(x=640, y=400)

        # Clear btn
        self.btn_clear = Button(master, text="Clear", width=18, height=2, bg='#e64747', fg='#343438',
                                command=self.clear)
        self.btn_clear.place(x=830, y=400)


        # self.choices_for_search = {'ID', 'Name'}
        # self.tkvar = StringVar(master)
        # self.tkvar.set('ID')
        # self.popupMenu = OptionMenu(master, self.tkvar, *self.choices_for_search)
        # self.popupMenu.place(x=300, y=200)

    def getSearchData(self, *args, **kwargs):
        q = "SELECT * FROM inventory WHERE id=?"
        result = cur.execute(q, (self.id_en.get(), ))
        for p in result:
            # print(p)
            self.pName = p[1]       #product Name
            self.pCostPrice = p[2]  #product cost price
            self.pSellPrice = p[3]  #product sell price
            self.pStock = p[4]      #product stock
            # Form Labels
            self.product_name = Label(self.master, text="Product name: ", font="arial 20 bold")
            self.cost_price = Label(self.master, text="Product cost price: ", font="arial 20 bold")
            self.sell_price = Label(self.master, text="Product sell price: ", font="arial 20 bold")
            self.stock = Label(self.master, text="Product stock: ", font="arial 20 bold")
            self.product_name.place(x=0, y=190)
            self.cost_price.place(x=0, y=240)
            self.sell_price.place(x=0, y=290)
            self.stock.place(x=0, y=340)

            # Form Entries
            self.product_name_e = Entry(self.master, width=25, font='arial 18 bold')
            self.product_name_e.place(x=300, y=190)
            self.cost_price_e = Entry(self.master, width=25, font='arial 18 bold')
            self.cost_price_e.place(x=300, y=240)
            self.sell_price_e = Entry(self.master, width=25, font='arial 18 bold')
            self.sell_price_e.place(x=300, y=290)
            self.stock_e = Entry(self.master, width=25, font='arial 18 bold')
            self.stock_e.place(x=300, y=340)

            self.product_name_e.insert(0, str(self.pName))
            self.cost_price_e.insert(0, str(self.pCostPrice))
            self.sell_price_e.insert(0, str(self.pSellPrice))
            self.stock_e.insert(0, str(self.pStock))

            self.btn_update = Button(self.master, text="Update Product", width=18, height=2, bg='#74e8aa', fg='#343438',
                                     command=self.update)
            self.btn_update.place(x=400, y=380)

        conn.commit()


    def getAll(self, *args, **kwargs):
        q = "SELECT * from inventory"
        products = cur.execute(q)
        self.clear()
        self.txBox.insert(END, "All Products:\n")
        for product in products:
            self.txBox.insert(END, "\nProduct no.: " + str(product[0]) + "\n" + "Product Name: " + str(
                product[1]) + "\n" + "Cost price: " + str(product[2]) + "\n" + "Sell Price: " + str(
                product[3]) + "\n" + "Stock: " + str(product[4]) + "\n")

    def clear(self, *args, **kwargs):
        self.txBox.delete(1.0, END)

    def update(self, *args, **kwargs):
        self.pName = self.product_name_e.get()
        self.pCostPrice = self.cost_price_e.get()
        self.pSellPrice = self.sell_price_e.get()
        self.pStock = self.stock_e.get()
        self.totalCost = float(self.pCostPrice) * float(self.pStock)
        self.totalSell = float(self.pSellPrice) * float(self.pStock)


        q = "UPDATE inventory SET product_name=?, cost_price=?, sell_price=?, stock=?, total_sell_price=?, total_cost_price=? WHERE id=?"
        cur.execute(q, (self.pName, self.pCostPrice, self.pSellPrice, self.pStock, self.totalSell,
                        self.totalCost, self.id_en.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Updated Successfully!")



def beginUpdate():
    root = Tk()
    master = Database(root)
    root.geometry("1000x480+0+0")
    root.title("Add to database")
    root.mainloop()


if __name__ == "__main__":
    beginUpdate()

