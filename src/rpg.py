from controller.menuController import MenuController
def main():
    #db
    #db.connect()
    menu = MenuController()
    menu.launchView()
    #db.discconnect()
    

if __name__ == '__main__':
    main()