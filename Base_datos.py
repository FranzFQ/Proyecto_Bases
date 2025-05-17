import pymysql
from pymysql import cursors

class BaseDatos:
    def __init__(self, user, password):
        self.conexion = pymysql.connect(
            host="localhost",
            user=user,
            password=password,
            database="modelo_proyecto",
            cursorclass=cursors.DictCursor
        )

    # =======================
    # MÉTODOS DE USUARIOS
    # =======================

    def agregar_usuario(self, nombre, email, tipo, contrasennia, telefono):
        # Agregar usuario nuevo
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO empleado (nombre, email, tipo, contrasennia, telefono)
                    VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nombre, email, tipo, contrasennia, telefono))
        self.conexion.commit()

    def modificar_usuario(self, id, nombre, email, tipo, contrasennia, telefono):
        # Modificar datos del usuario
        with self.conexion.cursor() as cursor:
            sql = """UPDATE empleado 
                    SET nombre = %s, email = %s, tipo = %s, contrasennia = %s, telefono = %s 
                    WHERE id = %s"""
            cursor.execute(sql, (nombre, email, tipo, contrasennia, telefono, id))
        self.conexion.commit()

    def eliminar_usuario(self, id):
        # Eliminar usuario (lógica: cambiar estado)
        with self.conexion.cursor() as cursor:
            cursor.execute("UPDATE empleado SET estado = %s WHERE id = %s", (0, id))
        self.conexion.commit()

    def obtener_usuarios(self):
        # Obtener todos los usuarios activos
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email, tipo, telefono, estado FROM empleado WHERE estado = 1")
            return cursor.fetchall()

    def buscar_usuario_por_nombre(self, nombre):
        # Buscar usuarios por nombre
        with self.conexion.cursor() as cursor:
            cursor.execute("""SELECT id, nombre, email, tipo, telefono 
                            FROM empleado 
                            WHERE nombre LIKE %s AND estado = 1""", (f"%{nombre}%",))
            return cursor.fetchall()

    def obtener_id_usuario(self, usuario):
        # Obtener ID del usuario
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT id FROM empleado WHERE nombre = %s", (usuario,))
            resultado = cursor.fetchone()
            return resultado['id'] if resultado else None

    def obtener_contraseña(self, usuario):
        # Obtener contraseña del usuario
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT contrasennia FROM empleado WHERE nombre = %s", (usuario,))
            resultado = cursor.fetchone()
            return resultado['contrasennia'] if resultado else None

    def obtener_nivel_usuario(self, usuario):
        # Obtener nivel/tipo del usuario
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT tipo FROM empleado WHERE nombre = %s", (usuario,))
            resultado = cursor.fetchone()
            return resultado['tipo'] if resultado else None

    # =======================
    # MÉTODOS DE PRODUCTOS
    # =======================

    def agregar_producto(self, nombre, precio, descripcion, existencia_minima):
        # Agregar producto nuevo
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO modelo_proyecto.producto 
                    (nombre, precio, descripcion, costo, stock_minimo) 
                    VALUES (%s, %s, %s, %s, %s)"""
            costo = precio - (precio * 0.15)
            cursor.execute(sql, (nombre, precio, descripcion, costo, existencia_minima))
        self.conexion.commit()

    def obtener_productos(self):
        # Obtener productos para administración
        with self.conexion.cursor() as cursor:
            cursor.execute("""SELECT id, nombre, stock, precio, descripcion, costo, stock_minimo 
                            FROM modelo_proyecto.producto WHERE estado = 1""")
            return cursor.fetchall()

    def obtener_productos_ventas(self):
        # Obtener productos para ventas
        with self.conexion.cursor() as cursor:
            cursor.execute("""SELECT id, nombre, stock, precio, descripcion 
                            FROM modelo_proyecto.producto WHERE estado = 1""")
            return cursor.fetchall()

    def buscar_producto_por_nombre(self, nombre):
        # Buscar productos para administración
        with self.conexion.cursor() as cursor:
            cursor.execute("""SELECT id, nombre, stock, precio, descripcion, costo, stock_minimo 
                            FROM modelo_proyecto.producto 
                            WHERE nombre LIKE %s AND estado = 1""", (f"%{nombre}%",))
            return cursor.fetchall()

    def buscar_producto_ventas_por_nombre(self, nombre):
        # Buscar productos para ventas
        with self.conexion.cursor() as cursor:
            cursor.execute("""SELECT id, nombre, descripcion, stock, precio 
                            FROM modelo_proyecto.producto 
                            WHERE nombre LIKE %s AND estado = 1""", (f"%{nombre}%",))
            return cursor.fetchall()

    def modificar_producto(self, id, nombre, precio, descripcion, existencia_minima):
        # Modificar datos de producto
        with self.conexion.cursor() as cursor:
            sql = """UPDATE producto 
                    SET nombre = %s, precio = %s, descripcion = %s, stock_minimo = %s 
                    WHERE id = %s"""
            cursor.execute(sql, (nombre, precio, descripcion, existencia_minima, id))
        self.conexion.commit()

    def eliminar_producto(self, id):
        # Eliminar producto (cambiar estado)
        with self.conexion.cursor() as cursor:
            cursor.execute("UPDATE producto SET estado = %s WHERE id = %s", (0, id))
        self.conexion.commit()

    def modificar_producto_stock(self, id, stock):
        # Modificar stock del producto
        with self.conexion.cursor() as cursor:
            cursor.execute("UPDATE producto SET stock = %s WHERE id = %s", (stock, id))
        self.conexion.commit()

    def modificar_stock_producto(self, id, stock):
        # Otra variante para modificar stock
        with self.conexion.cursor() as cursor:
            cursor.execute("UPDATE modelo_proyecto.producto SET stock = %s WHERE id = %s", (stock, id))
        self.conexion.commit()

    def aumentar_stock_producto(self, id, cantidad):
        # Aumentar stock de producto
        with self.conexion.cursor() as cursor:
            cursor.execute("UPDATE modelo_proyecto.producto SET stock = stock + %s WHERE id = %s", (cantidad, id))
        self.conexion.commit()

    def obtener_stock_producto(self, id):
        # Obtener stock actual de producto
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT stock FROM modelo_proyecto.producto WHERE id = %s", (id,))
            resultado = cursor.fetchone()
            return resultado['stock'] if resultado else None

    # =======================
    # MÉTODOS DE COMPRAS
    # =======================

    def agregar_compra(self, proveedor_id, fecha, empleado_id, total_compra):
        # Registrar compra
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO compra (Proveedor_id, fecha, Empleado_id, total_compra) 
                    VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (proveedor_id, fecha, empleado_id, total_compra))
            return cursor.lastrowid
        self.conexion.commit()

    def confirmar_orden_compra(self, id):
        # Confirmar orden de compra (cambiar estado)
        with self.conexion.cursor() as cursor:
            cursor.execute("UPDATE compra SET estado = %s WHERE id = %s", (1, id))
        self.conexion.commit()

    def obtener_compras_pendientes(self):
        # Obtener compras pendientes (sin registrar en stock)
        with self.conexion.cursor() as cursor:
            cursor.execute("""SELECT c.id as IdCompra, p.nombre as Proveedor, c.fecha as Fecha, c.total_compra as Total 
                            FROM compra c
                            JOIN proveedor p ON c.Proveedor_id = p.id
                            WHERE c.estado = 0 ORDER BY c.fecha DESC""")
            return cursor.fetchall()

    def agregar_detalle_compra(self, producto_id, compra_id, cantidad, precio, cantidad_recibida):
        # Agregar detalle a la compra
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO detalle_compra (Producto_id, Compra_id, cantidad, precio_unitario, cantidad_recibida) 
                    VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (producto_id, compra_id, cantidad, precio, cantidad_recibida))
        self.conexion.commit()

    def obtener_detalle_compra(self, id):
        # Obtener detalle de una compra específica
        with self.conexion.cursor() as cursor:
            cursor.execute("""SELECT dc.id as ID, dc.Producto_id as IdProducto, p.nombre as NombreProducto, 
                                    dc.precio_unitario as PrecioUnitario, dc.cantidad as Cantidad, dc.cantidad_recibida as CantidadRecibida
                            FROM detalle_compra dc
                            JOIN producto p ON dc.Producto_id = p.id
                            WHERE dc.Compra_id = %s""", (id,))
            return cursor.fetchall()
        
    def modificar_detalle_compra(self, id, cantidad_recibida):
        # Modificar detalle de compra (cantidad recibida)
        with self.conexion.cursor() as cursor:
            sql = """UPDATE detalle_compra 
                    SET cantidad_recibida = %s 
                    WHERE id = %s"""
            cursor.execute(sql, (cantidad_recibida, id))

        self.conexion.commit()

    # =======================
    # MÉTODOS DE VENTAS
    # =======================

    def agregar_venta(self, empleado_id, fecha, total_venta):
        # Registrar venta
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO venta (Empleado_id, fecha, total_venta) 
                    VALUES (%s, %s, %s)"""
            cursor.execute(sql, (empleado_id, fecha, total_venta))
        self.conexion.commit()

    def agregar_detalle_venta(self, producto_id, venta_id, cantidad, precio):
        # Agregar detalle a la venta
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO detalle_venta (Producto_id, Venta_id, cantidad, precio) 
                    VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (producto_id, venta_id, cantidad, precio))
        self.conexion.commit()

    def obtener_id_ultima_venta(self):
        # Obtener el ID de la última venta registrada
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT id FROM venta ORDER BY id DESC LIMIT 1")
            resultado = cursor.fetchone()
            return resultado['id'] if resultado else None

    # =======================
    # MÉTODOS DE PROVEEDORES
    # =======================

    def obtener_proveedores(self):
        # Obtener proveedores activos
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, direccion, email, telefono FROM proveedor WHERE estado = 1")
            return cursor.fetchall()

    def agregar_proveedor(self, nombre, direccion, email, telefono):
        # Agregar proveedor nuevo
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO proveedor (nombre, direccion, email, telefono) 
                    VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (nombre, direccion, email, telefono))
        self.conexion.commit()

    def editar_proveedor(self, id, nombre, direccion, email, telefono): #  nombre, direccion, email, telefono
        # Editar proveedor
        with self.conexion.cursor() as cursor:
            sql = """UPDATE proveedor 
                    SET nombre = %s, direccion = %s, email = %s, telefono = %s 
                    WHERE id = %s"""
            cursor.execute(sql, (nombre, direccion, email, telefono, id))
        self.conexion.commit()