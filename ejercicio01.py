#Elaborar un programa que muestre el total de la compra de un solo producto calculando el impuesto 
#sobre venta y dar un descuento solamente cuando el importe de la compra sea mayor a 10,000 el descuento 
# sera de un 25 por ciento.

Producto=int(input("Importe:"))

if Producto>=10000:
    Descuento=Producto*0.25
    Total=Producto-Descuento
    ISV=Total*0.15
    print("ISV: ",ISV)
    print("Descuento De Compra: ",Descuento)
    Total=Producto+ISV-Descuento
    print(f"Total: {Total}")
else:
    ISV=Producto*0.15
    print("Precio del Producto: ", Producto)
    print("ISV: ",ISV)
    Total=Producto+ISV
    print(f"Total: {Total}")
