


class Carrito:
    def __init__(self, request):
        self.request= request 
        self.session= request.session
        carro= self.session.get("carro") #cada sesion tiene su carro

        if not carro:                                              #si la sesion no tiene carro entonces crea uno en forma de diccionario
            carro= self.session["carro"] = {}
        else:                                                       # si la sesion tiene entonces lo usa
            self.carro= carro


    def agregar(self,producto): 
        if(str(producto.id) not in self.carro.keys()):                 #si el producto (id) no esta en el carrito agregalo
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "stock": 1,
                "imagen": producto.imagen.url
            }                                                         # entonces agrega todo esto
        else:
            for key, value in self.carro.items():
                if key== str(producto.id):
                    value["stock"]= value["stock"]+1
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carro"]= self.carro
        self.session.modified=True

    def eliminar_carrito(self, producto):
        producto.id= str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carrito()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key== str(producto.id):
                    value["stock"]= value["stock"]-1
                    if value["stock"] < 1:
                        self.eliminar_carrito(producto)
                    break
                
        self.guardar_carrito()

    def limpiar_carrito(self):
        self.session["carro"] = {}
        self.session.modified=True

        
        