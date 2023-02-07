from hcl_database_connection import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection):
    def available_seats(self):
        try:
            self.cursor.callproc("get_avl_tickets")
            for r in self.cursor.stored_results():
                d=r.fetchone()
            return d
        except Exception as e:
            print(e)
        finally:
            if (self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()

    def book(self):
        pass
b1=Booking()
b1.connect("localhost","root","Manjusha@17","train_ticket")
sts=b1.available_seats()

seat_avl={}
seat_avl['Train Name']=sts[0]
seat_avl['Available Seats']=sts[1]
print(seat_avl)
