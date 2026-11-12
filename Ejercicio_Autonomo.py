from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    mensaje = request.json["mensaje"].lower()
    mensaje = mensaje.replace("á", "a").replace("é", "e")
    mensaje = mensaje.replace("í", "i").replace("ó", "o")
    mensaje = mensaje.replace("ú", "u").replace("ü", "u").replace("ñ", "n")

    if "hola" in mensaje or "buenas" in mensaje or "buenos dias" in mensaje:
        respuesta = "¡Hola! Bienvenida a AliGyn Boutique. ¿Buscas algo para una ocasión especial?"

    elif "gracias" in mensaje:
        respuesta = "¡Gracias por visitar AliGyn Boutique! Esperamos verte pronto."

    elif "fiesta" in mensaje or "ocasion especial" in mensaje:
        respuesta = "Para una fiesta u ocasión especial, puedes combinar un vestido elegante con accesorios discretos. Cuéntame qué colores te gustan."

    elif "salida casual" in mensaje or "estilo casual" in mensaje:
        respuesta = "Para una salida casual, prueba jeans con una blusa cómoda y tus accesorios favoritos."

    elif "accesorio" in mensaje:
        respuesta = "Puedes combinar tu ropa con bolsos, cinturones o joyería discreta. Cuéntame qué prenda quieres complementar."

    elif "combinan" in mensaje or "combinar" in mensaje:
        respuesta = "Con jeans combinan muy bien blusas lisas, camisas y chaquetas ligeras. Elige el estilo según la ocasión."

    elif "verano" in mensaje:
        respuesta = "Para el verano, busca prendas ligeras y frescas, como blusas fluidas, vestidos y colores claros."

    elif "vestido" in mensaje and ("recomiend" in mensaje or "modelo" in mensaje):
        respuesta = "¡Claro! Tenemos distintos estilos de vestidos. Dime para qué ocasión lo buscas y qué colores prefieres."

    elif "outfit" in mensaje or "elegir" in mensaje:
        respuesta = "¡Claro! Te ayudo a armar un outfit. Cuéntame la ocasión, los colores que te gustan y qué prendas prefieres."

    elif "no me queda" in mensaje or "por otra talla" in mensaje or "cambio" in mensaje or "cambiar" in mensaje or "devolucion" in mensaje or "devolver" in mensaje:
        respuesta = "Aceptamos cambios dentro de los primeros 15 días con la prenda sin usar y su etiqueta. Conserva tu ticket; las promociones pueden tener condiciones especiales."

    elif "danad" in mensaje or "no llega" in mensaje or "no llego" in mensaje:
        respuesta = "Lamentamos el inconveniente. Escríbenos con tu número de pedido y, si llegó dañado, envíanos una foto para ayudarte."

    elif "talla" in mensaje or "medida" in mensaje or "chica" in mensaje or "mediana" in mensaje or "grande" in mensaje or "amplia" in mensaje or "reducida" in mensaje:
        respuesta = "Manejamos tallas CH, M, G y EG. Consulta la guía de medidas y, si dudas entre dos tallas, dinos qué prenda buscas."

    elif "fotografia" in mensaje or "foto" in mensaje:
        respuesta = "Con gusto te compartimos fotos de las prendas disponibles. Dinos cuál modelo te interesa."

    elif "color" in mensaje or "negro" in mensaje or "neutro" in mensaje:
        respuesta = "Tenemos distintos colores, incluidos tonos neutros según el modelo y la existencia. Dinos qué prenda buscas."

    elif "elegante" in mensaje or "casual" in mensaje:
        respuesta = "Tenemos prendas para estilos casuales y elegantes. Cuéntanos qué ocasión tienes en mente para recomendarte opciones."

    elif "stock" in mensaje or "disponible" in mensaje or "existencia" in mensaje:
        respuesta = "La disponibilidad cambia por modelo y talla. Compártenos el nombre de la prenda y la talla que necesitas."

    elif "descuento por" in mensaje or "varias prendas" in mensaje or "comprar varias" in mensaje:
        respuesta = "Las promociones por varias prendas pueden cambiar. Pregunta por la oferta vigente antes de realizar tu compra."

    elif "descuento" in mensaje or "promocion" in mensaje or "oferta" in mensaje or "economica" in mensaje:
        respuesta = "Publicamos promociones de temporada y opciones para distintos presupuestos. Pregunta por las ofertas vigentes."

    elif "costo de envio" in mensaje or "cuesta el envio" in mensaje or "precio del envio" in mensaje:
        respuesta = "El costo de envío depende de tu ubicación y se confirma antes de finalizar la compra."

    elif "cuanto tarda" in mensaje or "tiempo de entrega" in mensaje or "cuando llega" in mensaje or "tarda en llegar" in mensaje:
        respuesta = "El tiempo de entrega depende del destino. Te compartimos una fecha estimada al confirmar el pedido."

    elif "recoger" in mensaje or "entrega personal" in mensaje or "entregas personales" in mensaje:
        respuesta = "Pregunta por la opción de recoger en tienda o coordinar una entrega personal al confirmar tu compra."

    elif "lugar" in mensaje or "cobertura" in mensaje or "a donde" in mensaje:
        respuesta = "La cobertura depende del destino. Compártenos tu ciudad y revisamos si podemos enviar hasta allá."

    elif "envio" in mensaje or "entrega a domicilio" in mensaje or "domicilio" in mensaje:
        respuesta = "¡Sí! Realizamos envíos a domicilio. Compártenos tu ciudad para revisar la cobertura."

    elif "transferencia" in mensaje or "efectivo" in mensaje or "tarjeta" in mensaje or "metodo de pago" in mensaje or "pago" in mensaje:
        respuesta = "Aceptamos efectivo, transferencia y tarjetas de débito o crédito en tienda."

    elif "precio" in mensaje or "cuanto cuesta" in mensaje or "cuanto vale" in mensaje:
        respuesta = "El precio depende de la prenda y está indicado en su etiqueta. Dinos qué modelo te interesa y te orientamos."

    elif "apartar" in mensaje or "reservar" in mensaje:
        respuesta = "Puedes consultar si la prenda que te gusta se puede apartar. Indícanos el modelo y la talla."

    elif "registr" in mensaje:
        respuesta = "No necesitas registrarte para pedir información. Para comprar, escríbenos y te ayudamos con el proceso."

    elif "cancelar" in mensaje or "modificar" in mensaje:
        respuesta = "Si necesitas cancelar o modificar tu pedido, contáctanos cuanto antes con tu número de compra."

    elif "confirm" in mensaje:
        respuesta = "Te confirmamos la compra por el mismo medio de contacto que usaste al realizar el pedido."

    elif "comprar desde casa" in mensaje or "realizar un pedido" in mensaje or "hacer un pedido" in mensaje:
        respuesta = "Puedes comprar desde casa enviándonos el nombre o foto de la prenda y la talla que buscas."

    elif "pedido" in mensaje or "rastrear" in mensaje or "seguimiento" in mensaje or "paquete" in mensaje:
        respuesta = "Para consultar o rastrear tu pedido, ten a la mano tu número de compra y contáctanos."

    elif "horario" in mensaje or "abren" in mensaje or "cierran" in mensaje:
        respuesta = "Nuestro horario de ejemplo es de lunes a sábado, de 10:00 a 19:00 horas."

    elif "instagram" in mensaje or "facebook" in mensaje:
        respuesta = "Puedes encontrarnos en redes como AliGyn BOUTIQUE. Agrega aquí los enlaces oficiales de Instagram y Facebook."

    elif "comunicar" in mensaje or "contactar" in mensaje or "contacto" in mensaje:
        respuesta = "Escríbenos por mensaje directo en nuestras redes sociales. Agrega aquí el teléfono o enlace oficial de contacto."

    elif "novedad" in mensaje or "ropa nueva" in mensaje or "cada cuando" in mensaje or "temporada" in mensaje:
        respuesta = "Recibimos novedades por temporada. Síguenos en redes o pregúntanos para conocer las prendas recién llegadas."

    elif "tienda fisica" in mensaje or "presencial" in mensaje:
        respuesta = "Sí, contamos con atención en tienda. Escríbenos para confirmar la dirección y el horario antes de visitarnos."

    elif "ubicacion" in mensaje or "direccion" in mensaje or "donde se encuentra" in mensaje or "donde estan" in mensaje:
        respuesta = "Estamos en el centro de la ciudad. Escríbenos para compartirte la dirección exacta de AliGyn Boutique."

    elif "lavadora" in mensaje:
        respuesta = "Depende del material. Revisa la etiqueta; para prendas delicadas, usa ciclo suave o lavado a mano."

    elif "delicada" in mensaje or "planchar" in mensaje or "material" in mensaje or "lavar" in mensaje or "cuidado" in mensaje:
        respuesta = "Revisa la etiqueta de cada prenda para conocer su material y cuidados. Las prendas delicadas suelen requerir lavado suave y baja temperatura al planchar."

    elif "venden" in mensaje or "prenda" in mensaje or "coleccion" in mensaje or "ropa" in mensaje or "blusa" in mensaje or "vestido" in mensaje or "pantalon" in mensaje or "chamarra" in mensaje or "falda" in mensaje or "conjunto" in mensaje or "mas vendida" in mensaje:
        respuesta = "Tenemos blusas, vestidos, pantalones de mezclilla, chamarras, faldas y conjuntos. La disponibilidad depende de la temporada."

    else:
        respuesta = "No encontré esa respuesta. Puedes preguntarme por prendas, tallas, estilos, compras, pagos, envíos, cambios o cuidados."

    return jsonify({"respuesta": respuesta})


if __name__ == "__main__":
    app.run(debug=True)
