import collector

def main() : 
    try :
        collector.main()
    finally :
        print("driver")
        collector.main()

if __name__ == "__main__" :
    main()