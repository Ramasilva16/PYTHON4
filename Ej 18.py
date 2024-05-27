'''
Se desea automatizar el cálculo de la tarifa telefónica para una lista de clientes.

La empresainforma que cada llamado tiene un costo por conexión más un costo por el tiempo consumido en
segundos.

Se cuenta con las siguientes funciones ya implementadas.

ObtenerCantidadLlamados(nroCliente): retorna la cantidad de llamados para un cliente.

ObtenerTiempoPorLlamada(nroCliente, nroLlamada): retorna la cantidad de segundos de un
llamado de un cliente.

ObtenerCostoPorLlamada(): retorna el costo fijo por cada llamada.

ObtenerCostoPorTiempo(seg): retorna el costo de una llamada que dura seg segundos.

Realizar un programa que indique el monto de la factura para cada cliente.

'''

def CantidadLlamados(nroCliente):
    pass

def TiempoPorLlamada(nroCliente, nroLlamada):
    pass

def CostoPorLlamada():
    pass

def CostoPorTiempo (seg):
    pass

def CalcularMontoFactura (nroCliente):
    cantidad_llanmados = CantidadLlamados(nroCliente)
    costo_por_llamada = CostoPorLlamada ()
    total_factura = 0


    for llamada in range (1,Cantidad_llamados + 1):
        tiempo_llamada = TiempoPorLlamada (nroCliente, nroLlamada)
        costo_por_tiempo = CostoPorTiempo (tiempo_llamada)
        total_factura += costo_por_llamada + costo_por_tiempo
    return total_factura


#Ejemplo
clientes = [1, 2, 3] #Listado de Clientes
for cliente in clientes:
    monto_factura = CalcularMontoFactura (cliente)
    print ('Cliente', cliente, ':','Monto de la factura', monto_factura)