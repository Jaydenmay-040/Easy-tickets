
from tkinter import *
from tkinter import messagebox


class TicketSales:
    def __init__(self, window):
        # initialise the root
        self.window = window
        self.window.title('Easy Tickets')
        self.window.geometry('450x500')
        self.window.config(bg="#31373d")

        # cell number label and entry
        self.cell_entry_label = Label(self.window, text='Enter CellNumber: ')
        self.cell_entry = Entry(self.window)
        self.cell_entry_label.place(x=30, y=10)
        self.cell_entry.place(x=250, y=10)
        self.cell_entry_label.config(bg='#a6a7a8', fg='black')

        # ticket category
        self.ticket_label = Label(self.window, text='Select Ticket Category: ')
        self.variable = StringVar()
        self.variable.set('Select Ticket')
        self.ticket_opt = OptionMenu(window, self.variable, 'Soccer', 'Movie', 'Theater')
        self.ticket_label.place(x=30, y=50)
        self.ticket_opt.place(x=250, y=45)
        self.ticket_label.config(bg='#a6a7a8', fg='black')
        self.ticket_opt.config(bg='#007ced')

        # amount of tickets
        self.ticket_no_label = Label(self.window, text='Number of Tickets Bought:')
        self.ticket_spinbox = Spinbox(self.window, width=10, from_=0, to=100)
        self.ticket_no_label.place(x=30, y=90)
        self.ticket_spinbox.place(x=250, y=90)
        self.ticket_no_label.config(bg='#a6a7a8')

        # buttons
        self.calc_button = Button(self.window, text='Calculate Ticket', command=self.calc_prepayment)
        self.clear_button = Button(self.window, text='Clear Entries', command=self.clear)
        self.calc_button.place(x=30, y=180)
        self.clear_button.place(x=250, y=180)
        self.calc_button.config(bg='#007ced')
        self.clear_button.config(bg='#007ced')

        # output
        self.amount = Label(self.window, text='')
        self.reserve = Label(self.window, text='')
        self.cell_label = Label(self.window, text='')
        self.amount.place(x=80, y=260)
        self.reserve.place(x=80, y=300)
        self.cell_label.place(x=80, y=340)
        self.amount.config(bg='#10518d')
        self.reserve.config(bg='#10518d')
        self.cell_label.config(bg='#10518d')

    def calc_prepayment(self):
        ticket_no = int(self.ticket_spinbox.get())
        vat = 0.14
        try:
            int(self.cell_entry.get())
            if len(self.cell_entry.get()) < 10 or len(self.cell_entry.get()) > 10:
                raise ValueError

            elif self.variable.get() == 'Select Ticket':
                raise ValueError

            elif int(self.ticket_spinbox.get()) == 0:
                raise ValueError

            elif self.variable.get() == 'Soccer':
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount.config(text=text)

            elif self.variable.get() == 'Movie':
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount.config(text=text)

            elif self.variable.get() == 'Theater':
                price = 100  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount.config(text=text)

            reserve_text = 'Reservation for {} for {}'.format(self.variable.get(), ticket_no)
            cell_text = 'was done by {}'.format(self.cell_entry.get())
            self.reserve.config(text=reserve_text)
            self.cell_label.config(text=cell_text)

        except ValueError:
            messagebox.showerror(message='Invalid combination')

    def clear(self):
        self.cell_entry.delete(0, END)
        self.cell_entry.focus()
        self.variable.set('Select Ticket')
        self.ticket_spinbox.delete(0, END)
        self.ticket_spinbox.insert(0, 0)
        self.amount.config(text='')
        self.reserve.config(text='')
        self.cell_label.config(text='')


window = Tk()
TicketSales(window)
window.mainloop()
