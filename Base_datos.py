import pymysql
from pymysql import cursors


class BaseDatos:
    def __init__(self, user, password):
        self.conexion = pymysql.connect(
            host="localhost",
            user=user,
            password=password,
            database="modelo_proyecto",
            cursorclass=cursors.DictCursor)  # Para obtener resultados como diccionarios

    def agregar_usuario(self, nombre, email, tipo, contrasennia, telefono): # (nombre, email, tipo, contrasennia, telefono)
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO empleado (nombre, email, tipo, contrasennia, telefono)
                    VALUES (%s, %s, %s, %s, %s)"""
            
            cursor.execute(sql, (nombre, email, tipo, contrasennia, telefono))
        self.conexion.commit()

    def modificar_usuario(self, id, nombre, email, tipo, contrasennia, telefono): # (id, nombre, email, tipo, telefono)
        with self.conexion.cursor() as cursor:
            sql = """UPDATE empleado 
                    SET nombre = %s, email = %s, tipo = %s, contrasennia = %s, telefono = %s 
                    WHERE id = %s"""
            cursor.execute(sql, (nombre, email, tipo, contrasennia, telefono, id))
        self.conexion.commit()

    def eliminar_usuario(self, id):
        with self.conexion.cursor() as cursor:
            cursor.execute("UPDATE empleado SET estado = %s WHERE id = %s", (0, id))
        self.conexion.commit()

    def obtener_usuarios(self):
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email, tipo, telefono, estado FROM empleado where estado = 1")

            return cursor.fetchall() # (id, nombre, email, tipo, telefono)
        
    def buscar_usuario_por_nombre(self, nombre):
        with self.conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, nombre, email, tipo, telefono 
                FROM empleado 
                WHERE nombre LIKE %s and estado = 1
            """, (f"%{nombre}%",))
            return cursor.fetchall()

    def obtener_contraseña(self, usuario):
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT contrasennia FROM empleado WHERE nombre = %s", (usuario,))
            resultado = cursor.fetchone()
            return resultado['contrasennia'] if resultado else None
    
    def obtener_nivel_usuario(self, usuario):
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT tipo FROM empleado WHERE nombre = %s", (usuario,))
            resultado = cursor.fetchone()
            return resultado['tipo'] if resultado else None

    def agregar_producto(self, nombre, precio, stock, descripcion, existencia_minima):
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO modelo_proyecto.producto 
                    (nombre, precio, stock, descripcion, costo, stock_minimo) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
            costo = precio - (precio * 0.15)
            cursor.execute(sql, (nombre, precio, stock, descripcion, costo, existencia_minima))
        self.conexion.commit()

    def obtener_productos(self):
        with self.conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, nombre, stock, precio, descripcion, costo, stock_minimo 
                FROM modelo_proyecto.producto WHERE estado = 1
            """)
            return cursor.fetchall()

    def obtener_productos_ventas(self):
        with self.conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, nombre, stock, precio, descripcion
                FROM modelo_proyecto.producto WHERE estado = 1
            """)
            return cursor.fetchall()

    def eliminar_producto(self, id):
        with self.conexion.cursor() as cursor:
            cursor.execute("UPDATE producto SET estado = %s WHERE id = %s", (0, id))
        self.conexion.commit()

    def buscar_producto_por_nombre(self, nombre):
        with self.conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, nombre, stock, precio, descripcion, costo, stock_minimo 
                FROM modelo_proyecto.producto 
                WHERE nombre LIKE %s and estado = 1
            """, (f"%{nombre}%",))
            return cursor.fetchall()
        
    def buscar_producto_ventas_por_nombre(self, nombre): # ID, nombre, despcripcion, existencia, precio
        with self.conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, nombre, descripcion, stock, precio 
                FROM modelo_proyecto.producto 
                WHERE nombre LIKE %s and estado = 1
            """, (f"%{nombre}%",))
            return cursor.fetchall()
        
    def modificar_producto_stock(self, id, stock):
        with self.conexion.cursor() as cursor:
            sql = """
                UPDATE producto 
                SET stock = %s 
                WHERE id = %s
            """
            cursor.execute(sql, (stock, id))
        self.conexion.commit()

    def obtener_id_ultima_venta(self):
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT id FROM venta ORDER BY id DESC LIMIT 1")
            resultado = cursor.fetchone()
            # Devolver únicamente el id de la última venta

            return resultado['id'] if resultado else None

    def modificar_producto(self, id, nombre, precio, descripcion, existencia_minima):
        with self.conexion.cursor() as cursor:
            sql = """
                UPDATE producto 
                SET nombre = %s, precio = %s, descripcion = %s, stock_minimo = %s 
                WHERE id = %s
            """
            cursor.execute(sql, (nombre, precio, descripcion, existencia_minima, id))
        self.conexion.commit()

    def agregar_venta(self, empleado_id, fecha, total_venta):
        with self.conexion.cursor() as cursor:
            sql = """
                INSERT INTO venta (Empleado_id, fecha, total_venta) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (empleado_id, fecha, total_venta))
        self.conexion.commit()

    def agregar_detalle_venta(self, producto_id, venta_id, cantidad, precio): # (Producto_id, Venta_id, cantidad, precio)
        with self.conexion.cursor() as cursor:
            sql = """
                INSERT INTO detalle_venta (Producto_id, Venta_id, cantidad, precio) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (producto_id, venta_id, cantidad, precio))
        self.conexion.commit()