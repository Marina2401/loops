
def main():
    s = "молоко = 50р, хлеб = 30р, колбаса = 300р"
    products = s.split(',')
    total = 0
    for product in products:
        name, cost = product.split('=')
        cost = cost.strip().strip('р')
        cost = int(cost)
        total += cost
    print(total)


if __name__ == '__main__':
    main()