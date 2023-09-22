def memory_addressing(page_table, page_size,logical_address):
    # page_table = {0: 5, 1: 9, 2: 14}
    # page_size = 4096
    # logical_address = 7000
    page_number, offset = divmod(logical_address, page_size)
    if page_number in page_table:
        frame_number = page_table[page_number]
        physical_address = frame_number * page_size + offset
        return physical_address
        

        
def main():
    pa=-1
    page_table = {}
    for i in range(3):
        page_table[int(i)]=int(input(f"Type the number of the frame that the {i} page refers to: "))
    page_size = int(input("Type the size of the frame, or the page: "))
    logical_address = int(input("Type the logical address: "))
    pa = memory_addressing(page_table, page_size,logical_address)
    if pa!=-1:
        print(f"The physical address is {pa}")
    else:
        print("Invalid page number, address translation failed.")

if __name__ == "__main__":
    main()